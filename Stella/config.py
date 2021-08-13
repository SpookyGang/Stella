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

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("stella.env"):
    load_dotenv("stella.env")

class Config:
    API_ID =  int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")

    OWNER_ID = int(getenv("OWNER_ID"))
    
    BOT_TOKEN = getenv("BOT_TOKEN")
    BOT_NAME = getenv("BOT_NAME")
    BOT_USERNAME= getenv("BOT_USERNAME")
    BOT_ID = getenv("BOT_ID")
    PREFIX = getenv("PRRFIX")

    DATABASE_URI = getenv("DATABASE_URI")
    BACKUP_CHAT = getenv("BACKUP_CHAT")

    LOG_CHANNEL = getenv("LOG_CHANNEL", None)

    SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

    # APIs 
    StellaGbanAPI = getenv("StellaGbanAPI", None)
    
