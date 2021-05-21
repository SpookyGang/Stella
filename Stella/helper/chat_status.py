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


from typing import List, Union

from pyrogram.types import Message
from Stella import (BOT_ID, GROUP_ANONYMOUS_BOT, SUDO_USERS, StellaCli,
                    TELEGRAM_SERVICES_IDs)
from Stella.database.connection_mongo import GetConnectedChat

ADMIN_STRINGS = [
        "creator",
        "administrator"
    ]

BOT_PERMISSIONS_STRINGS = {
    "can_delete_messages": "Looks like I haven't got the right to delete messages; mind promoting me? Thanks!",
    "can_restrict_members": "could not set telegram chat permissions, so locks have all been unlocked: unable to setChatPermissions: Bad Request: not enough rights to change chat permissions",
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
    "can_add_web_page_previews": "You'rWe not allowed to add web page previews to their messages.",
    "can_send_polls": "You're not allowed to send polls."
}

async def isBotAdmin(message: Message, chat_id=None, silent=False) -> bool:
    """This function returns the bot admin status in the chat. 

    Args:
        message (Message): Message
        chat_id ([type], optional): pass chat_id: message.chat.id  Defaults to None.
        silent (bool, optional): if True bot will be silent when isBotAdmin returned False. Defaults to False.

    Returns:
        bool: True when bot has chat status is admin
    """
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

async def isUserAdmin(message: Message, pm_mode: bool = False, user_id: int = None, chat_id: int = None, silent: bool = False) -> bool:
    """ This function returns users chat status in the chat.

    Args:
        message (Message): Message
        chat_id (int, optional): chat_id: message.chat.id . Defaults to None.
        silent (bool, optional): if True bot will be silent when its isUserAdmin = returned False. Defaults to False.

    Returns:
        bool: True when user has chat status is admin | creator of the chat.
    """

    if user_id is None:
        user_id = message.from_user.id

    if chat_id is None:
        chat_id = message.chat.id 

    if not pm_mode: 
        if message.chat.type == 'private':
            return True  

    GetData = await StellaCli.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    
    if (
        GetData.status in ADMIN_STRINGS
    ):
        return True
    else:
        if not silent:
            await message.reply(
                "Only admins can execute this command!"
            )
        return False

async def anon_admin_checker(chat_id: int, user_id: int) -> bool:
    """ This function returns user_id chat status

    Returns:
        bool: True when user_id has chat status is admin | creator of chat.
    """
    GetData = await StellaCli.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    if GetData.status not in ADMIN_STRINGS:
        return False
    else:
        return True


async def can_restrict_member(message: Message, user_id: int, chat_id: int = None) -> bool:
    """This function returns can bot restrict member in the given chat.

    Returns:
        Bool: True is bot can restrict the member.
    """
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

async def isUserCreator(message: Message, chat_id: int = None, user_id: int = None) -> bool:
    """ This function returns the creator status of the given chat.

    Returns:
        bool: True when user's chat status is creator.
    """
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

async def isBotCan(message: Message, chat_id: int = None, permissions: str = 'can_change_info', silent: bool = False) -> bool:
    """This function returns permissions of the bot in the  given chat.

    Args:
        message (Message): Message
        chat_id (int, optional): pass chat_id: message.chat.id . Defaults to None.
        permissions (str, optional): Pass permission . Defaults to can_change_info.
        silent (bool, optional): if True bot will be silent if isBotCan returned False. Defaults to False.

    Returns:
        bool: True when Bot has permission of given permission in the chat.
    """
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

async def isUserCan(message, user_id: int = None, chat_id: int = None, permissions: str = None, silent: bool = False) -> bool:
    """This function returns permissions of the user in the chat.

    Returns:
        bool: True when user has permission of given permission in the chat.
    """
    if user_id is None:
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

async def CheckAllAdminsStuffs(message: Message, permissions: Union[str, List[str]] = 'can_change_info', silent=False) -> bool:
    """This function checks both bot & user permissions and chat status is the chat.

    Args:
        message (Message): Message
        permissions (Union[str, List[str]], optional): pass permission list or str. Defaults to 'can_change_info'.
        silent (bool, optional): if True bot will remain silent in chat. Defaults to False.

    Returns:
        bool: True when user and bot both has chat status is admin.
    """
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

    if not await isBotAdmin(message, chat_id=chat_id, silent=silent):
        return False
    
    if not await isUserAdmin(message, chat_id=chat_id, silent=silent):
        return False

    if isinstance(permissions, list):
        for permission in permissions:
            if not await isBotCan(message, chat_id=chat_id, permissions=permission, silent=silent):
                return False
        
            if not await isUserCan(message, chat_id=chat_id, permissions=permission, silent=silent):
                return False

    elif isinstance(permissions, str):
        if not await isBotCan(message, chat_id=chat_id, permissions=permissions, silent=silent):
            return False
    
        if not await isUserCan(message, chat_id=chat_id, permissions=permissions, silent=silent):
            return False
    return True

async def CheckAdmins(message: Message, silent: bool = False) -> bool:
    """This function checks both bot & user chat status in the chat.

    Args:
        message (Message): Message

    Returns:
        bool: True when both are admins.
    """
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

    if not await isBotAdmin(message, chat_id=chat_id, silent=silent):
        return False
    
    if not await isUserAdmin(message, chat_id=chat_id, silent=silent):
        return False
    
    return True

async def isUserBanned(chat_id: int, user_id: int) -> bool:
    """This function check is user is banned in this given chat or not.

    Args:
        chat_id (int): chat_id: message.chat.id
        user_id (int): pass the user_id 

    Returns:
        bool: True when user is banned in the given chat.
    """
    data_list = await StellaCli.get_chat_members(
        chat_id=chat_id,
        filter='kicked'
        )
    for user in data_list:
        if user is not None:
            if user_id == user.user.id:
                return True
    

async def check_user(message: Message, permissions: Union[str, List[str]] = 'can_change_info', silent: bool = False) -> bool:
    """This function check user's chat status as well as user's permissions in the chat.

    Returns:
        bool: True when user's chat status is admin or creator and user has permissions in the chat.
    """
    if not await isUserAdmin(message, silent=silent):
        return False
    
    if isinstance(permissions, list):
        for permission in permissions:
            if not await isUserCan(message, permissions=permission, silent=silent):
                return False

    elif isinstance(permissions, str):
        if not await isUserCan(message, permissions=permissions, silent=silent):
            return False
    
    return True

async def check_bot(message: Message, permissions: Union[str, List[str]] = 'can_change_info', silent: bool = False) -> bool:
    """This function check bot's chat status as well as user's permissions in the chat.

    Returns:
        bool: True when bot's chat status is admin and bot has permissions in the chat.
    """
    if not await isBotAdmin(message, silent=silent):
        return False
    
    if isinstance(permissions, list):
        for permission in permissions:
            if not await isBotCan(message, permissions=permission, silent=silent):
                return False
    else:        
        if not await isBotCan(message, permissions=permissions, silent=silent):
            return False
    
    return True
