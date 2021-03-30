import json
import datetime

from Stella import StellaDB
from Stella.helper import custom_filter
from Stella import (
    StellaCli,
    scheduler,
    OWNER_ID,
    SUDO_USERS,
    BACKUP_CHAT
)

COLLECTIONS_NAMES = StellaDB.list_collection_names()

@StellaCli.on_message(custom_filter.command(commands=('dbexport')))
async def StellaExport(client, message):
    user_id = message.from_user.id

    if not user_id in OWNER_ID:
        return

    if (
        user_id in SUDO_USERS
    ):
        await message.reply(
            "This command is mode for only my kami-samas!"
        )
        return
    
    collect_collections()
    await StellaCli.send_document(
        chat_id=BACKUP_CHAT,
        document='Stella_Backup.json',
        caption='exported!'
    )

async def export_scheduler():
    collect_collections()
    await StellaCli.send_document(
        chat_id=BACKUP_CHAT,
        document='Stella_Backup.json',
        caption='exported!'
    )

# Async scheduler for auto export at 3 A.M
scheduler.add_job(export_scheduler, "cron", day_of_week ='mon-sun', hour=3, minute=00)

def exports_in_json(COLLECTIONS_LIST):
    with open('Stella_Backup.json', 'w') as backup_file:
        json.dump(COLLECTIONS_LIST, backup_file, indent=4, sort_keys=True, cls=DateTimeEncoder)

def collect_collections():
    COLLECTIONS_LIST  = {
        'collections': [],
        'exports_data': []
    }

    for collection in COLLECTIONS_NAMES:
        COLLECTIONS_LIST['collections'].append(collection)
        all_collec = list(StellaDB[collection].find({}))
        #print(all_collec)
        COLLECTIONS_LIST['exports_data'].append(
            {
                collection: all_collec
            }
        )
    exports_in_json(COLLECTIONS_LIST)
  
class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)