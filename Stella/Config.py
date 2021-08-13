import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("stella.env"):
    load_dotenv("stella.env")

class config:
    api_id =  int(getenv("api_id"))
    api_hash = getenv("api_hash")

    owner_id = int(getenv("owner_id"))
    
    bot_token = getenv("bot_token")
    bot_name = getenv("bot_name")
    bot_username= getenv("bot_username")
    bot_id = getenv("bot_id")
    prefix = getenv("prrfix")

    database_uri = getenv("database_uri")
    backup_chat = getenv("backup_chat")

    log_channel = getenv("log_channel", none)

    sudo_users = list(map(int, getenv("sudo_users").split()))

    # apis 
    stellagbanapi = none
    
