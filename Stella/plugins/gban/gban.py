from Stella import BOT_ID, OWNER_ID, SUDO_USERS, StellaAPI, StellaCli
from Stella.database.users_mongo import GetAllChats
from Stella.helper import custom_filter
from Stella.helper.get_user import get_text, get_user_id


@StellaCli.on_message(custom_filter.command(commands=('gban')))
async def Gban(client, message):

    if not (
        message.from_user.id in SUDO_USERS
        or message.from_user.id in OWNER_ID
    ):
        return 
    
    admin_id = message.from_user.id 
    user_info = await get_user_id(message)
    GbannedUser = user_info.id 
    
    reason = get_text(message)

    operation, request_message = StellaAPI.gban_protocol(admin_id, GbannedUser, reason)
    if operation:
        CHATS_LIST = GetAllChats()
        BannedChats = []
        for chat_id in CHATS_LIST:
            GetData = await StellaCli.get_chat_member(
                chat_id=chat_id,
                user_id=BOT_ID
            )
            if GetData['can_restrict_members']:
                try:
                    if await StellaCli.kick_chat_member(
                        chat_id,
                        GbannedUser
                    ):
                        BannedChats.append(chat_id)
                except:
                    continue
            else:
                continue
        
        await message.reply(
            text=(
                "New banned user:\n"
                f"Admin: `{admin_id}`\n"
                f"GBanned user: `{GbannedUser}`\n"
                f"Reason: `{reason}`\n"
                f"Affected chat: `{len(BannedChats)}`"
            )
        )
    else:
        await message.reply(
            request_message
        )
    