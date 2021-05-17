from pyrogram.errors import BadRequest
from pyrogram.types import ChatPermissions
from Stella import StellaCli
from Stella.database.locks_mongo import lock_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import check_bot, check_user

from . import lock_map


@StellaCli.on_message(custom_filter.command(commands=('lock')))
async def lock(client, message):
    
    chat_id = message.chat.id

    if not await check_bot(message, permissions=['can_delete_messages', 'can_restrict_members']):
        return

    if not await check_user(message, permissions='can_change_info'):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You haven't specified a type to lock."
        )
        return

    LOCKS_LIST = lock_map.LocksMap.list()

    lock_args = message.command[1:]
    
    LOCK_ITMES = []
    INCORRECT_ITEMS = []

    for lock in lock_args:
        if lock not in LOCKS_LIST:
            INCORRECT_ITEMS.append(lock)
        else:
            LOCK_ITMES.append(lock)
    
    if (
        len(INCORRECT_ITEMS) != 0
    ):
        text = (
            "Unknown lock types:\n"
        )
        for item in INCORRECT_ITEMS:
            text += f'- {item}\n'
        text += "Check /locktypes!"
        await message.reply(
                text
            )
        return
    
    for item in LOCK_ITMES:
        lock_value = lock_map.LocksMap[item].value
        lock_db(chat_id, lock_value)

    text = 'Locked:\n'
    for lock_arg in LOCK_ITMES:
        if len(LOCK_ITMES) != 1:
            text += f'- `{lock_arg}`\n'
        else:
            text = (
                f"Locked `{lock_arg}`."
            )

    if 'all' in LOCK_ITMES:
        try:
            await StellaCli.set_chat_permissions(
                chat_id,
                ChatPermissions()
            )
        except BadRequest:
            await message.reply(
                (
                    "Non-admins already can't send messages. What are you even trying to do m8?"
                )
            )
            return

    await message.reply(
        text
    )
