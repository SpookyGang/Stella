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


from Stella import BOT_ID, StellaCli
from Stella.database.federation_mongo import (get_connected_chats,
                                              get_fed_admins,
                                              get_fed_from_chat, get_fed_name,
                                              get_fed_reason, is_user_fban,
                                              update_reason, user_fban)
from Stella.helper import custom_filter
from Stella.helper.get_user import get_user_id


@StellaCli.on_message(custom_filter.command(commands=('fban')))
async def fed_ban(client, message):
    chat_id = message.chat.id
    user_info = await get_user_id(message)
    userID = user_info.id 
    
    bannerMention = message.from_user.mention 
    banner_name = message.from_user.first_name
    bannedID = message.from_user.id

    fed_id = get_fed_from_chat(chat_id)
    fed_name = get_fed_name(fed_id=fed_id)
    get_user = await StellaCli.get_users(
                user_ids=userID
            )

    FED_ADMINS = get_fed_admins(fed_id)
    
    if userID == BOT_ID:
        await message.reply(
            "Hahahaha no. I am not going to fban myself."
        )
        return
    
    if bannedID not in FED_ADMINS:
        await message.reply(
            f"You aren't a federation admin of {fed_name}."
        )
        return

    if (
        message.reply_to_message 
        and len(message.command) >= 2
    ):
        reason_text = ' '.join(message.text.split()[1:])   
    
    elif (
        len(message.command) >= 3
    ):
        reason_text = ' '.join(message.text.split()[2:])  

    else:
        reason_text = 'No reason was given'
     
    
    reason = f"{reason_text} // Fbanned by {banner_name} id {bannedID}"
    if is_user_fban(fed_id, userID):
        old_reason = get_fed_reason(fed_id, userID)
        if not old_reason == reason:
            update_reason(fed_id, userID, reason)
            fed_message = (
            f'**This user was already banned in the** "{fed_name}" **federation, I\'ll update the reason:**\n\n'
            f"Fed Administrator: {bannerMention}\n"
            f"User: {get_user.mention}\n"
            f"User ID: `{userID}`\n"
            f"Old Reason: `{old_reason}`\n"
            f"Updated Reason: `{reason}`"
        )
        else:
            fed_message = (
                f"User {get_user.mention} has already been fbanned, with the exact same reason."
            )
    else:
        user_fban(fed_id, userID, reason)
        connected_chats = get_connected_chats(fed_id)
        BannedChats = []
        for chat_id in connected_chats:
            GetData = await StellaCli.get_chat_member(
                chat_id=chat_id,
                user_id=BOT_ID
            )
            if GetData['can_restrict_members']:
                if await StellaCli.kick_chat_member(
                    chat_id,
                    userID
                ):
                    BannedChats.append(chat_id)
            else:
                continue

        fed_message = (
                f'**New Federation Ban in the** "{fed_name}" **federation:**\n\n'
                f"Fed Administrator: {bannerMention}\n"
                f"User: {get_user.mention}\n"
                f"User ID: `{userID}`\n"
                f"Reason: {reason}\n"
                f"Affected Chats: `{len(BannedChats)}`"
            )

    await message.reply(
        fed_message
    )

