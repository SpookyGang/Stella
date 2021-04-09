from Stella import (
    StellaCli, 
    TELEGRAM_SERVICES_IDs,
    GROUP_ANONYMOUS_BOT,
    SUDO_USERS,
    BOT_ID
)
from Stella.database.connection_mongo import GetConnectedChat


ADMIN_STRINGS = [
        "creator",
        "administrator"
    ]

BOT_PERMISSIONS_STRINGS = {
    "can_delete_messages": "Looks like I haven't got the right to delete messages; mind promoting me? Thanks!",
    "can_restrict_members": "I don't have permission to restrict, ban or unban chat members.",
    "can_promote_members": "I don't have permission to promote or demote someone in this chat!",
    "can_change_info": "I don't have permission to change the chat title, photo and other settings.",
    "can_pin_messages": "I don't have permission to pin messages in this chat.",
    "can_be_edited": "I don't have enough permission to edit administrator privileges of the user."
}

USERS_PERMISSIONS_STRINGS = {
    "can_be_edited": "You don't have enough permission to edit adminstrator privileges of the user",
    "can_delete_messages": "You don't have enough permission to delete any messages in the chat.",
    "can_restrict_members": "You dont't have enough permission to restrict, ban or unban chat members.",
    "can_promote_members": "You don't have enough permission to add new administrators with a subset of his own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user).",
    "can_change_info": "You don't have enough permission to change the chat title, photo and other settings.",
    "can_invite_users": "You're not allowed to invite new users to the chat.",
    "can_pin_messages": "You're not allowed to pin messages.",
    "can_send_media_messages": "You're not allowed to send audios, documents, photos, videos, video notes and voice notes.",
    "can_send_stickers": "You're not allowed to send stickers, implies can_send_media_messages.",
    "can_send_animations": "You're not allowed to send animations (GIFs), implies can_send_media_messages.",
    "can_send_games": "You're not allowed to send games, implies can_send_media_messages.",
    "can_use_inline_bots": "You're not allowed to use inline bots, implies can_send_media_messages.",
    "can_add_web_page_previews": "You're not allowed to add web page previews to their messages.",
    "can_send_polls": "You're not allowed to send polls."
}

async def isBotAdmin(message, chat_id=None, silent=False) -> bool:

    if chat_id is None:
        chat_id = message.chat.id
    
    GetData  = await StellaCli.get_chat_member(
        chat_id=chat_id,
        user_id=BOT_ID
    )
    
    if GetData.status not in ADMIN_STRINGS:
        if not silent:
            await message.reply(
            "I'm not admin here to do that."
            )
        return False
    else:
        return True

async def isUserAdmin(message, chat_id=None, silent=False) -> bool:
    
    if message.from_user:
        user_id = message.from_user.id 
    elif message.sender_chat:
        user_id = message.sender_chat.id
        chat_id = message.chat.id
        
        if user_id == chat_id:
            return True
        else:
            return False    

    if GetConnectedChat(user_id) is not None:
        chat_id = GetConnectedChat(user_id)

    elif chat_id is not None:
        chat_id = chat_id

    else: 
        chat_id = message.chat.id 
        
        if (
            message.chat.type == 'private'
            or user_id in SUDO_USERS
        ):
            return True
    
    GetData = await StellaCli.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    
    if (
        GetData.status in ADMIN_STRINGS
        or user_id in SUDO_USERS
    ):
        return True
    else:
        if silent == False:
            await message.reply(
                "Only admins can execute this command!"
            )
        return False

async def anon_admin_checker(chat_id, user_id) -> bool:
    GetData = await StellaCli.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    if GetData.status not in ADMIN_STRINGS:
        return False
    else:
        return True


async def can_restrict_member(message, user_id, chat_id=None) -> bool:
    if chat_id is None:
        chat_id = message.chat.id 

    try:
        GetData = await StellaCli.get_chat_member(
            chat_id=chat_id,
            user_id=user_id
        )
    except:
        return True

    if (
        GetData.status in ADMIN_STRINGS
        or user_id in SUDO_USERS
    ):
        return False
    else:
        return True

async def isUserCreator(message, chat_id=None, user_id=None) -> bool:
    
    if user_id is None:
        if message.sender_chat:
            user_id = message.sender_chat.id
            chat_id = message.chat.id 
            if user_id == chat_id:
                return False
        else:
            user_id = message.from_user.id 

    if GetConnectedChat(user_id) is not None:
        chat_id = GetConnectedChat(user_id)

    elif chat_id is not None:
        chat_id = chat_id

    else: 
        chat_id = message.chat.id 
        if (
            message.chat.type == 'private'
        ):
            return True
    
    GetData = await StellaCli.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )

    if GetData.status == 'creator':
        return True
    else:
        return False

async def isBotCan(message, chat_id=None, permissions=None, silent=False) -> bool:
    
    if chat_id is None:
        chat_id = message.chat.id
    
    GetData = await StellaCli.get_chat_member(
        chat_id=chat_id,
        user_id=BOT_ID
    )
    if GetData[permissions]:
        return True
    else:
        if silent == False:
            await message.reply(
                BOT_PERMISSIONS_STRINGS[permissions]
            )
        return False

async def isUserCan(message, chat_id=None, permissions=None, silent=False) -> bool:
    if message.sender_chat:
        user_id = message.sender_chat.id
        chat_id = message.chat.id
        
        if user_id == chat_id:
            return True
        else:
            return False   

    user_id = message.from_user.id 
    if GetConnectedChat(user_id) is not None:
        chat_id = GetConnectedChat(user_id)
        
    elif chat_id is not None:
        chat_id = chat_id

    else: 
        chat_id = message.chat.id

    GetData = await StellaCli.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    if (
        GetData[permissions]
        or user_id in SUDO_USERS
    ):
        return True
    else:
        if silent == False:
            await message.reply(
                USERS_PERMISSIONS_STRINGS[permissions]
            )
        return False

async def CheckAllAdminsStuffs(message, permissions=None, silent=False) -> bool:
    if message.sender_chat:
        user_id = message.sender_chat.id
        chat_id = message.chat.id
        
        if user_id == chat_id:
            return True
        else:
            return False   

    user_id = message.from_user.id 
    if GetConnectedChat(user_id) is not None:
        chat_id = GetConnectedChat(user_id)
    else: 
        chat_id = message.chat.id 
        if (
                message.chat.type == 'private'
            ):
                await message.reply(
                    "This command is made to be used in group chats, not in pm!",
                    quote=True
                )
                return False

    if not await isBotAdmin(message, chat_id, silent):
        return False
    
    if not await isUserAdmin(message, chat_id, silent):
        return False
    
    if not await isBotCan(message, chat_id, permissions, silent):
        return False
    
    if not await isUserCan(message, chat_id, permissions, silent):
        return False
    
    return True

async def CheckAdmins(message) -> bool:
    if message.sender_chat:
        user_id = message.sender_chat.id
        chat_id = message.chat.id
        
        if user_id == chat_id:
            return True
        else:
            return False   
            
    user_id = message.from_user.id 
    if GetConnectedChat(user_id) is not None:
        chat_id = GetConnectedChat(user_id)
    else: 
        chat_id = message.chat.id 
        if (
                message.chat.type == 'private'
            ):
                await message.reply(
                    "This command is made to be used in group chats, not in pm!",
                    quote=True
                )
                return

    if not await isBotAdmin(message, chat_id):
        return False
    
    if not await isUserAdmin(message, chat_id):
        return False
    
    return True

async def isUserBanned(chat_id, user_id) -> bool:
    data_list = await StellaCli.get_chat_members(
        chat_id=chat_id,
        filter='kicked'
        )
    for user in data_list:
        if user_id == user.user.id:
            return True
    

async def check_user(message, permissions=None, silent=False):
    if not await isUserAdmin(message, silent=silent):
        return False
    
    if not await isUserCan(message, permissions=permissions, silent=silent):
        return False
    
    return True

async def check_bot(message, permissions=None, silent=False):
    if not await isBotAdmin(message, silent=silent):
        return False
    
    if not await isBotCan(message, permissions=permissions, silent=silent):
        return False
    
    return True