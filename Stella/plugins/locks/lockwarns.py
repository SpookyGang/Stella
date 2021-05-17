import html

from Stella import StellaCli
from Stella.database.locks_mongo import lockwarns_db, set_lockwarn_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import check_user

LOCKWARN_TRUE = ['on', 'yes']
LOCKWARN_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands=('lockwarns')))
async def lockwarns(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title
    if (
        len(message.command) >= 2
    ):
        args = message.command[1]
        if (
            args in LOCKWARN_TRUE
        ):
            set_lockwarn_db(chat_id, True)
            await message.reply(
                "Lock warns have been enabled. Any user using locked messages will be warned, as well has have their message deleted."
            )
        
        elif (
            args in LOCKWARN_FALSE
        ):
            set_lockwarn_db(chat_id, False)
            await message.reply(
                "Lock warns have been disabled. Any user using locked messages will no longer be warned, and will only have their message deleted."
            )
        
        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off"
            )
    else:
        if lockwarns_db(chat_id):
            await message.reply(
                f"I am currently warning all users who try to use locked message types in {html.escape(chat_title)}."
            )
        else:
            await message.reply(
                f"I am NOT warning all users who try to use locked message types in {html.escape(chat_title)}. I will simply delete the messages."
            )
