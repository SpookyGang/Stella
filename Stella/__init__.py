import sys

from Stella.config import Config

from pyrogram import Client
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from pymongo import MongoClient
from pyromod import listen

from Stella.StellaGban import StellaClient
#from stellagban import StellaClient


APP_ID = Config.API_ID
API_HASH = Config.API_HASH
OWNER_ID = Config.OWNER_ID
BOT_TOKEN = Config.BOT_TOKEN
BOT_NAME = Config.BOT_NAME
BOT_USERNAME = Config.BOT_USERNAME
BOT_ID = Config.BOT_ID
LOG_CHANNEL = Config.LOG_CHANNEL
SUDO_USERS = Config.SUDO_USERS
PREFIX = Config.PREFIX
DATABASE_URI = Config.DATABASE_URI
BACKUP_CHAT = Config.BACKUP_CHAT
StellaGbanAPI = Config.StellaGbanAPI

StellaCli = Client(
    'StellaSession',
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

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
        1087968824 #GroupAnonymousBot
    ]
)

GROUP_ANONYMOUS_BOT = 1087968824