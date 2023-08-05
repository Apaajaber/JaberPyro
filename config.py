# Credits: @tracemoepy
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/tracemoepy/DarkPyro-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/tracemoepy/DarkPyro-Userbot/blob/main/LICENSE/>.
#
# t.me/DiscussionDark & t.me/fuckdvck

from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("API_HASH", "b18441a1ff607e10a989891a5462e627")
API_ID = int(getenv("API_ID", "2040"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", None).split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "0.1@beta"
BRANCH = getenv("BRANCH", "master")
CHANNEL = getenv("CHANNEL", "fuckdvck")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "postgresql://user:password@db:5432/pyrodark")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "DiscussionDark")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
REPO_URL = getenv("REPO_URL", "https://github.com/2R-Dark-Kanger-Pro/DarkPyro-REV")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", None).split()))
