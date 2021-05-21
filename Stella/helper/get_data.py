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


from emojis import decode
from pyrogram.types import Message
from Stella import StellaCli
from Stella.database.users_mongo import GetChatName


async def GetChat(chat_id: int):
    """This function return chat_title of the given chat_id from the database of the bot.

    Args:
        chat_id (int): chat_id: message.chat.id

    Returns:
        [type]: chat's title
    """
    if GetChatName(chat_id) is not None:
        chat_title = GetChatName(chat_id)
        return chat_title
    else:
        await StellaCli.send_message(
            chat_id=chat_id,
            text=(
                "I couldn't find the `{chat_title}` in my database. Please execute /forcecachechat here to make me be able to store your chat's data!"
            )
        )
        return

def get_text_reason(message: Message) -> str:
    """This function returns text, and the reason of the user's arguments

    Args:
        message (Message): Message

    Returns:
        [str]: text, reason
    """
    text = decode(message.text)
    index_finder = [x for x in range(len(text)) if text[x] == '"']
    if len(index_finder) >= 2:
        text = text[index_finder[0]+1: index_finder[1]]
        reason = text[index_finder[1] + 2:]
        if not reason:
            reason = None
    else:
        text = message.command[1]
        reason = ' '.join(message.command[2:])
        if not reason:
            reason = None
    
    return (
        text,
        reason
        )
