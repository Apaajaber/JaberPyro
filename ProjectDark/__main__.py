# Credits: @tracemoepy
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/tracemoepy/DarkPyro-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/tracemoepy/DarkPyro-Userbot/blob/main/LICENSE/>.
#
# t.me/DiscussionDark & t.me/fuckdvck

import importlib

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from ProjectDark import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from ProjectDark.helpers.misc import create_botlog, heroku
from ProjectDark.modules import ALL_MODULES

MSG_ON = """
**Darkpyro-Userbot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk Mengecek Status Bot**
━━
"""


async def main():
    for all_module in ALL_MODULES:
        importlib.import_module(f"ProjectDark.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("fuckdvck")
            await bot.join_chat("DiscussionDark")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("ProjectDark").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("ProjectDark").info(f"Darkpyro-UserBot v{BOT_VER} [BERHASIL DIAKTIFKAN!]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("ProjectDark").info("Starting Darkpyro-UserBot")
    install()
    heroku()
    LOOP.run_until_complete(main())
