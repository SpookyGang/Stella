import time

from pyrogram.types import ChatPermissions

from Stella import StellaCli
from Stella.database.blocklists_mongo import (
    getblocklistmode,
    getblocklistMessageDelete,
    get_blocklist_reason
)
from Stella.plugins.warnings.warn import warn

async def blocklist_action(message, blocklist_word):

    chat_id = message.chat.id 
    user_id = message.from_user.id 

    reason = get_blocklist_reason(chat_id, blocklist_word)

    blocklist_mode, blocklist_time, dreason = getblocklistmode(chat_id)
    if reason is None:
        if dreason is None:
            reason = f'Automated blocklist action, due to a match on: {blocklist_word}'
        else:
            reason = dreason
    
    if blocklist_mode == 1:
        if getblocklistMessageDelete(chat_id):
            await message.delete()
        return
    
    elif blocklist_mode == 2:
        await StellaCli.kick_chat_member(
            chat_id,
            user_id
        )
        await message.reply(
            (
                f"User {message.from_user.mention} was banned.\n"
                f"**Reason:**\n{reason}"
            )
        )

        if getblocklistMessageDelete(chat_id):
            await message.delete()

    elif blocklist_mode == 3:
        await StellaCli.restrict_chat_member(
            chat_id,
            user_id,
            ChatPermissions(
                can_send_messages=False
            )
        )
        await message.reply(
            (
                f"User {message.from_user.mention} is mutted now.\n"
                f"**Reason:**\n{reason}"
            )
        )

        if getblocklistMessageDelete(chat_id):
            await message.delete()

    elif blocklist_mode == 4:
        await StellaCli.kick_chat_member(
            chat_id,
            user_id,
            int(time.time()) + 60 # wait 60 seconds in case of server goes down at unbanning time
        )
        await message.reply(
            (
                f"User {message.from_user.mention} is kicked.\n"
                f"**Reason:**\n{reason}"
            )
        )

        if getblocklistMessageDelete(chat_id):
            await message.delete()

        # Unbanning proceess and wait 5 sec to give server to kick user first
        await asyncio.sleep(5) 
        await StellaCli.unban_chat_member(chat_id, user_id)
    
    elif blocklist_mode == 5:
        await warn(message, reason, warn_user=message)

        if getblocklistMessageDelete(chat_id):
            await message.delete()
    
    elif blocklist_mode == 6:
        until_time = int(time.time() + int(blocklist_time))
        await StellaCli.kick_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            until_date=until_time
            )
        await message.reply(
            (
                f"User {message.from_user.mention} was temporarily banned.\n"
                f"**Reason:**\n{reason}"
            )
        )

        if getblocklistMessageDelete(chat_id):
            await message.delete()
    
    elif blocklist_mode == 7:
        until_time = int(time.time() + int(blocklist_time))
        await StellaCli.restrict_chat_member(
            chat_id,
            user_id,
            ChatPermissions(
            can_send_messages=False
            ),
            until_date=until_time
        )
        await message.reply(
            (
                f"User {message.from_user.mention} was temporarily muted.\n"
                f"**Reason:**\n{reason}"
            )
        )

        if getblocklistMessageDelete(chat_id):
            await message.delete()