from Stella import StellaCli
from Stella.database.blocklists_mongo import get_blocklist, rmblocklist_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin
from Stella.helper.get_data import get_text_reason


@StellaCli.on_message(custom_filter.command(commands=['rmblocklist', 'rmblacklist']))
async def add_blocklist(client, message):

    chat_id = message.chat.id 
    if not await isUserAdmin(message):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You need to specify the blocklist filter to remove"
        )
        return
    
    blocklist_word = ' '.join(message.command[1:])

    BLOCKLIST_DATA = get_blocklist(chat_id)
    if (
        BLOCKLIST_DATA is None
        or len(BLOCKLIST_DATA) == 0
    ):
        return

    BLOCKLIST_ITMES = []
    for blocklist_array in BLOCKLIST_DATA:
        BLOCKLIST_ITMES.append(blocklist_array['blocklist_text'])
    
    if blocklist_word in BLOCKLIST_ITMES:
        rmblocklist_db(chat_id, blocklist_word)
        await message.reply(
            f"I will no longer blocklist '`{blocklist_word}`'."
        )
    else:
        await message.reply(
            f"`{blocklist_word}` hasn't been blocklisted, and so couldn't be stopped. Use the /blocklist command to see the current blocklist."
        )
