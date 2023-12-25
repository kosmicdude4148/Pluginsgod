import os
import time

from PIL import Image
from pyrogram.enums import MessageMediaType
from pyrogram.types import Message

from Hellbot.functions.convert import tgs_to_png, video_to_png
from Hellbot.functions.formatter import readable_time
from Hellbot.functions.images import draw_meme
from Hellbot.functions.media import get_metedata
from Hellbot.functions.paste import post_to_telegraph
from Hellbot.functions.tools import progress, runcmd

from . import Config, HelpMenu, hellbot, on_message


@on_message("mediainfo", allow_stan=True)
async def mediaInfo(_, message: Message):
    if not message.reply_to_message or not message.reply_to_message.media:
        return await hellbot.delete(message, "Reply to a media file")

    media = message.reply_to_message.media
    hell = await hellbot.edit(message, "Getting media info...")

    if media == MessageMediaType.ANIMATION:
        media_file = message.reply_to_message.animation
    elif media == MessageMediaType.AUDIO:
        media_file = message.reply_to_message.audio
    elif media == MessageMediaType.DOCUMENT:
        media_file = message.reply_to_message.document
    elif media == MessageMediaType.PHOTO:
        media_file = message.reply_to_message.photo
    elif media == MessageMediaType.STICKER:
        media_file = message.reply_to_message.sticker
    elif media == MessageMediaType.VIDEO:
        media_file = message.reply_to_message.video
    else:
        return await hellbot.delete(message, "Unsupported media type")

    metadata = await get_metedata(media_file)
    if not metadata:
        return await hellbot.delete(message, "Failed to get media info")

    await hell.edit(f"Fetched metadata, now fetching extra mediainfo...")

    start_time = time.time()
    try:
        file_path = await message.reply_to_message.download(
            Config.DWL_DIR,
            progress=progress,
            progress_args=(hell, start_time, "⬇️ Downloading"),
        )
    except Exception:
        return await hell.edit(
            f"**Failed to download media check the metadata instead!**\n\n{metadata}"
        )

    out, _, _, _ = await runcmd(f"mediainfo '{file_path}'")
    if not out:
        return await hell.edit(
            f"Failed to get mediainfo, check the metadata instead!\n\n{metadata}"
        )

    await hell.edit(f"Uploading mediainfo to telegraph...")

    to_paste = f"<h1>💫 HellBot Media Info:</h1><br>{metadata}<br><b>📝 MediaInfo:</b><br><code>{out}</code>"
    link = post_to_telegraph("HellBotMediaInfo", to_paste)

    await hell.edit(f"**📌 Media Info:** [Here]({link})")
    os.remove(file_path)


@on_message(["mmf", "memify"], allow_stan=True)
async def memify(_, message: Message):
    if len(message.command) < 2:
        return await hellbot.delete(message, "Enter some text!")

    if not message.reply_to_message or not message.reply_to_message.media:
        return await hellbot.delete(message, "Reply to a media file")

    start_time = time.time()
    hell = await hellbot.edit(message, "Memifying...")
    file = await message.reply_to_message.download(
        Config.DWL_DIR,
        progress=progress,
        progress_args=(hell, start_time, "⬇️ Downloading"),
    )

    text = await hellbot.input(message)
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text, lower_text = text, ""

    if file and file.endswith(".tgs"):
        await hell.edit("Looks like an animated sticker, converting to image...")
        pic = await tgs_to_png(file)
    elif file and file.endswith((".webp", ".png")):
        pic = Image.open(file).save(file, "PNG", optimize=True)
    elif file:
        await hell.edit("Converting to image...")
        pic, status = await video_to_png(file, 0)
        if status == False:
            return await hellbot.error(hell, pic)
    else:
        return await hellbot.delete(message, "Unsupported media type")

    await hell.edit("Adding text...")
    memes = await draw_meme(file, upper_text, lower_text)

    await hell.edit("Done!")
    await message.reply_sticker(memes[1])
    await message.reply_photo(
        memes[0],
        caption=f"**🍀 𝖬𝖾𝗆𝗂𝖿𝗂𝖾𝖽 𝗎𝗌𝗂𝗇𝗀 𝖧𝖾𝗅𝗅𝖡𝗈𝗍!**",
    )

    os.remove(pic)
    os.remove(file)
    os.remove(memes[0])
    os.remove(memes[1])


@on_message("rename", allow_stan=True)
async def renameMedia(_, message: Message):
    if not message.reply_to_message or not message.reply_to_message.media:
        return await hellbot.delete(message, "Reply to a media file to rename it!")

    media = message.reply_to_message.media
    if media not in [
        MessageMediaType.AUDIO,
        MessageMediaType.DOCUMENT,
        MessageMediaType.PHOTO,
        MessageMediaType.VIDEO,
        MessageMediaType.VOICE,
    ]:
        return await hellbot.delete(message, "Unsupported media type!")

    if len(message.command) < 2:
        return await hellbot.delete(
            message, "You need to provide a new filename with extention!"
        )

    new_name = await hellbot.input(message)
    hell = await hellbot.edit(message, f"Renaming to `{new_name}` ...")

    strart_time = time.time()
    renamed_file = await message.reply_to_message.download(
        Config.DWL_DIR + new_name,
        progress=progress,
        progress_args=(hell, strart_time, "⬇️ Downloading"),
    )

    dwl_time = readable_time(int(strart_time - time.time()))
    await hell.edit(f"**Downloaded and Renamed in** `{dwl_time}`**,** __uploading...__")

    start2 = time.time()
    await message.reply_document(
        renamed_file,
        caption=f"**📁 File Name:** `{new_name}`",
        file_name=new_name,
        force_document=True,
        progress=progress,
        progress_args=(hell, start2, "⬆️ Uploading"),
    )

    end_time = readable_time(int(start2 - time.time()))
    total_time = readable_time(int(strart_time - time.time()))
    await hell.edit(
        f"**📁 File Name:** `{new_name}`\n\n**⬇️ Downloaded in:** `{dwl_time}`\n**⬆️ Uploaded in:** `{end_time}`\n**💫 Total time taken:** `{total_time}`"
    )
    os.remove(renamed_file)


HelpMenu("media").add(
    "mediainfo",
    "<reply to media message>",
    "Get the metadata and detailed media info of replied media file.",
    "mediainfo",
).add(
    "memify",
    "<reply to media message> <upper text>;<lower text>",
    "Add text to a media file and make it a meme.",
    "memify Hello World",
    "When ';' is used, the text before it will be the upper text and the text after it will be the lower text.",
).add(
    "rename",
    "<reply to media message> <new file name>",
    "Rename a media file with the provided name.",
    "rename HellBot.jpg",
    "The file name must have an extention.",
).info(
    "Media utils"
).done()
