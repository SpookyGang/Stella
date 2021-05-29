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


from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup)
from Stella import StellaCli
from Stella.database.federation_mongo import (fed_promote,
                                              get_fed_from_ownerid,
                                              get_fed_name, is_user_fban)
from Stella.helper import custom_filter
from Stella.helper.get_user import get_user_id


@StellaCli.on_message(custom_filter.command(commands=('fedpromote')))
async def FedPromote(client, message):
    user_info = await get_user_id(message)
    user_id = user_info.id 
    
    owner_id = message.from_user.id 
    fed_id = get_fed_from_ownerid(owner_id)
    fed_name = get_fed_name(owner_id=owner_id)
    user = await StellaCli.get_users(
        user_ids=user_id
    )

    if (
        message.chat.type == 'private'
    ):
        await message.reply(
            "This command is made to be run in a group where the person you would like to promote is present."
        )
        return
    
    if (
        fed_id == None
    ):
        await message.reply(
            "Only federation creators can promote people, and you don't even seem to have a federation to promote to!"
        )
        return
    
    if (
        is_user_fban(fed_id, user_id)
    ):
        await message.reply(
            f"User {user.mention} is fbanned in {fed_name}. You have to unfban them before promoting."
        )
        return

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='Confirm', callback_data=f'fedpromote_promote_{user_id}_{owner_id}'),
                    InlineKeyboardButton(text='Cancel', callback_data=f'fedpromote_cancel_{user_id}_{owner_id}')
                ]
            ]
        )

    await message.reply(
        f"Please get {user.mention} to confirm that they would like to be fed admin for {fed_name}.",
        reply_markup=keyboard
    )


@StellaCli.on_callback_query(filters.create(lambda _, __, query: 'fedpromote_' in query.data))
async def fedpromote_callback(client: StellaCli, callback_query: CallbackQuery):
    
    query_data = callback_query.data.split('_')[1]
    user_id = int(callback_query.data.split('_')[2])
    owner_id = int(callback_query.data.split('_')[3])
    fed_id = get_fed_from_ownerid(owner_id)
    fed_name = get_fed_name(owner_id=owner_id)
    user = await StellaCli.get_users(
        user_ids=user_id
    )
    owner = await StellaCli.get_users(
        user_ids=owner_id
    )

    if query_data == 'promote':
        if user_id == callback_query.from_user.id:
            fed_promote(fed_id, user_id)
            await callback_query.edit_message_text(
                text=(
                    f"User {user.mention} is now admin of {fed_name} ({fed_id})"
                )
            )
        else:
            await callback_query.answer(
                text=(
                    "You aren't the user being promoted."
                )
            )

    elif query_data == 'cancel':
        if user_id == callback_query.from_user.id:
            await callback_query.edit_message_text(
                text=(
                    f"Fedadmin promotion has been refused by {user.mention}."
                )
            )

        elif owner_id == callback_query.from_user.id:
            await callback_query.edit_message_text(
                text=(
                    f"Fedadmin promotion cancelled by {owner.mention}."
                )
            )
        else:
            await callback_query.answer(
                text=(
                    "You aren't the user being promoted."
                )
            )
        