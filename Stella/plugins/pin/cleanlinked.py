import html

from Stella import StellaCli
from Stella.database.pin_mongo import (antichannelpin_db, cleanlinked_db,
                                       get_antichannelpin, get_cleanlinked)
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs

CLEAN_LINKED_TRUE = ['on', 'yes']
CLEAN_LINKED_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands=('cleanlinked')))
async def cleanlinked(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title
    if not await CheckAllAdminsStuffs(message, permissions='can_delete_messages'):
        return
    
    if (
        len(message.command) >= 2
    ):
        args = message.command[1]
        if (
            args in CLEAN_LINKED_TRUE
        ):
            ANTICHANNEL_PIN = get_antichannelpin(chat_id)
            if ANTICHANNEL_PIN:
                await message.reply(
                    "I've disabled `/antichannelpin`. Do /pininfo to know why or you can also read the `/help`."
                )
                antichannelpin_db(chat_id, False)
                
            cleanlinked_db(chat_id, True)
            await message.reply(
                f"**Enabled** linked channel post deletion in {html.escape(chat_title)}. Messages sent from the linked channel will be deleted."
            )
        
        elif (
            args in CLEAN_LINKED_FALSE
        ):
            cleanlinked_db(chat_id, False)
            await message.reply(
                f"**Disabled** linked channel post deletion in {html.escape(chat_title)}."
            )
        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off"
            )

    else:
        IS_CLEAN_LINK = get_cleanlinked(chat_id)
        if IS_CLEAN_LINK:
            await message.reply(
                f"Linked channel post deletion is currently **enabled** in {html.escape(chat_title)}. Messages sent from the linked channel will be deleted."
            )
        
        else:
            await message.reply(
                f"Linked channel post deletion is currently **disabled** in {html.escape(chat_title)}."
            )
