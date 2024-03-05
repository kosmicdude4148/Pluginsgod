from . import *

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.enums import ChatAction

from asyncio import sleep

global x = True

@on_message("stopgalispam")
async def stopgspam(c: Client, m: Message):
    await c.send_chat_action(m.chat.id, ChatAction.CANCEL)
    await m.reply_text("Stopped gali spam")
    global x
    x = False


@on_message("galispam")
async def start_galispam(c: Client, m: Message):
    global x
    x = True
    xn = await m.reply_text("Startting galispam")
    await sleep(0.4)
    await xn.delete()
    await c.send_chat_action(m.chat.id,ChatAction.TYPING)
    while x == True:
        await m.delete()
        chat = m.chat.id
        await hellbot.send_message(chat, "TERIIIIII")
        await hellbot.send_message(chat, "MAAA KIIII")
        await hellbot.send_message(chat, "CHUTT MARUUUU")
        await hellbot.send_message(chat, "MADERRCHODD")
        await hellbot.send_message(chat, "BEHENN KEE LODEEE")
        await hellbot.send_message(chat, "TERIII MAAA")
        await hellbot.send_message(chat, "KOO AISAA CHODAAA")
        await hellbot.send_message(chat, "MADEERCHODD")
        await hellbot.send_message(chat, "KAALAAP GYII")
        await hellbot.send_message(chat, "TERII MAAA")
        await hellbot.send_message(chat, "TERAAA")
        await hellbot.send_message(chat, "KHANDAANN KO")
        await hellbot.send_message(chat, "ANDARRRR TKK")
        await hellbot.send_message(chat, "CHOD DALAAA")
        await hellbot.send_message(chat, "TERIIII")
        await hellbot.send_message(chat, "BEHENNN")
        await hellbot.send_message(chat, "ABHII MEREE")
        await hellbot.send_message(chat, "SEEEE")
        await hellbot.send_message(chat, "CHUDD RHI HAIII")
        await hellbot.send_message(chat, "MADERRCHODDD")
        await hellbot.send_message(chat, " TERIII")
        await hellbot.send_message(chat, "MAAA KIII")
        await hellbot.send_message(chat, "CHUTT MEE")
        await hellbot.send_message(chat, "HATHII KAA")
        await hellbot.send_message(chat, "LAUDAA")
        await hellbot.send_message(chat, "GHUSAA DIYAA")
        await hellbot.send_message(chat, "MADEERRCHODDD")
        await hellbot.send_message(chat, "RANDII")
        await hellbot.send_message(chat, "KAA")
        await hellbot.send_message(chat, "PILLAAA")
        await hellbot.send_message(chat, "BEHENCHODDD")
        await hellbot.send_message(chat, "TERIII")
        await hellbot.send_message(chat, "BEHENN")
        await hellbot.send_message(chat, "KIII")
        await hellbot.send_message(chat, "CHUTTT")
        await hellbot.send_message(chat, "MEEE")
        await hellbot.send_message(chat, "TOWERRR")
        await hellbot.send_message(chat, "GHUSAA DIYAA")
        await hellbot.send_message(chat, "MADERRRCHODD")
        await hellbot.send_message(chat, "TERAAA")
        await hellbot.send_message(chat, "BAAAP")
        await hellbot.send_message(chat, "HUINN")
        await hellbot.send_message(chat, "BSDKKKK")
        await hellbot.send_message(chat, "GANDD")
        await hellbot.send_message(chat, "MARR")
        await hellbot.send_message(chat, "MARRR")
        await hellbot.send_message(chat, "KEEE")
        await hellbot.send_message(chat, "ZINDAGIIII")
        await hellbot.send_message(chat, "ANDHERIII")
        await hellbot.send_message(chat, "KARRRR")
        await hellbot.send_message(chat, "DUGAAA")
        await hellbot.send_message(chat, "MADERRRCHODDD")
        await hellbot.send_message(chat, "BEHENNN")
        await hellbot.send_message(chat, "KEEE")
        await hellbot.send_message(chat, "LODEEE")
        await hellbot.send_message(chat, "AISAAA")
        await hellbot.send_message(chat, "CHODUGAAA")
        await hellbot.send_message(chat, "BSDKKK")
        await hellbot.send_message(chat, "PHIRRR")
        await hellbot.send_message(chat, "SEEE")
        await hellbot.send_message(chat, "KISIII")
        await hellbot.send_message(chat, "SEEE GANDD")
        await hellbot.send_message(chat, " MARANEE")
        await hellbot.send_message(chat, "KEE")
        await hellbot.send_message(chat, "LAYAKKK")
        await hellbot.send_message(chat, "NAHII BACHEGAAA")
        await hellbot.send_message(chat, "BAAAP")
        await hellbot.send_message(chat, "SEEE")
        await hellbot.send_message(chat, "PANGAA")
        await hellbot.send_message(chat, "LIYA HAIII")
        await hellbot.send_message(chat, "BSDKK TUUU")
        await hellbot.send_message(chat, "ANDARRR TAK")
        await hellbot.send_message(chat, "CHUDEGGAAA")
        await hellbot.send_message(chat, "TERIII")
        await hellbot.send_message(chat, "MAAAA")
        await hellbot.send_message(chat, "KAAA RAPEE")
        await hellbot.send_message(chat, "KARR DIYAA")
        await hellbot.send_message(chat, "MADERRCHODDD")
        await hellbot.send_message(chat, "BEHENCHODD")
        await hellbot.send_message(chat, "TERAAA")
        await hellbot.send_message(chat, "ASLIII")
        await hellbot.send_message(chat, "BAAAP MAINN")
        await hellbot.send_message(chat, "HI HUINNN")
        await hellbot.send_message(chat, "BSDKK")
        await hellbot.send_message(chat, "TERI MAA")
        await hellbot.send_message(chat, "KOO KOTHEE")
        await hellbot.send_message(chat, "PE CHODAA")
        await hellbot.send_message(chat, "THAA GHODII BANAKEE")
        await hellbot.send_message(chat, "JAKEEE")
        await hellbot.send_message(chat, "PUCHHH APNI")
        await hellbot.send_message(chat, "APNI")
        await hellbot.send_message(chat, "SAMJHAA LAWDE")
        await hellbot.send_message(chat, "MAAA SEE��")
        await hellbot.send_message(chat, "TERI ASLII")
        await hellbot.send_message(chat, "BAAAP")
        await hellbot.send_message(chat, "MAIN HI HUINN")
        await hellbot.send_message(chat, "MERAA NAJAYAZ�不")
        await hellbot.send_message(chat, "BETA HAI TUU")


HelpMenu("galispam").add(
    "galispam", None, "Start Gaali Spam!"
).add(
    "stopgalispam", None, "Gaali spam stop!"
).info(
    "Spammer Module\nMay get floodwait!"
).done()