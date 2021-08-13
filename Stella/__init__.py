#    Stella (Development)
#    Copyright (C) 2021 - meanii (Anil Chauhan)
#    Copyright (C) 2021 - SpookyGang (Neel Verma, Anil Chauhan)

#    This program is free software; you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by 
#    the Free Software Foundation; either version 3 of the License, or 
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pymongo import MongoClient
from pyrogram import Client
from pyromod import listen
from aiohttp import ClientSession

from Stella.config import Config
from Stella.StellaGban import StellaClient

#from stellagban import StellaClient


APP_ID = Config.API_ID
API_HASH = Config.API_HASH
OWNER_ID = Config.OWNER_ID
BOT_TOKEN = Config.BOT_TOKEN
BOT_ID = Config.BOT_ID
BOT_NAME = Config.BOT_NAME
BOT_USERNAME = Config.BOT_USERNAME
LOG_CHANNEL = Config.LOG_CHANNEL
SUDO_USERS = Config.SUDO_USERS
PREFIX = Config.PREFIX
DATABASE_URI = Config.DATABASE_URI
BACKUP_CHAT = Config.BACKUP_CHAT
StellaGbanAPI = Config.StellaGbanAPI


StellaCli = Client(
    session_name='StellaSession',
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

pbot = StellaCli

aiohttpsession = ClientSession()

StellaAPI = StellaClient(api_key=StellaGbanAPI)

scheduler = AsyncIOScheduler()

try:
    StellaMongoClient = MongoClient(DATABASE_URI)
    StellaDB = StellaMongoClient.stella_mongo
except:
    sys.exit(f"{BOT_NAME}'s database is not running!")

TELEGRAM_SERVICES_IDs = (
    [
        777000, # Telegram Service Notifications
        1087968824 # GroupAnonymousBot
    ]
)

GROUP_ANONYMOUS_BOT = 1087968824
