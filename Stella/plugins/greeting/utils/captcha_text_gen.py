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


from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def ButtonGen(CaptchaStringList: list, new_chat_id: int):
    keyboard = ([[
        InlineKeyboardButton(text=CaptchaStringList[0], callback_data=f"textc_{CaptchaStringList[0]}_{new_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[1], callback_data=f"textc_{CaptchaStringList[1]}_{new_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[2], callback_data=f"textc_{CaptchaStringList[2]}_{new_chat_id}")]])
    keyboard += ([[
        InlineKeyboardButton(text=CaptchaStringList[3], callback_data=f"textc_{CaptchaStringList[3]}_{new_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[4], callback_data=f"textc_{CaptchaStringList[4]}_{new_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[5], callback_data=f"textc_{CaptchaStringList[5]}_{new_chat_id}")]])
    keyboard += ([[
        InlineKeyboardButton(text=CaptchaStringList[6], callback_data=f"textc_{CaptchaStringList[6]}_{new_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[7], callback_data=f"textc_{CaptchaStringList[7]}_{new_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[8], callback_data=f"textc_{CaptchaStringList[8]}_{new_chat_id}")]])
    keyboard += ([[
        InlineKeyboardButton(text=CaptchaStringList[9], callback_data=f"textc_{CaptchaStringList[9]}_{new_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[10], callback_data=f"textc_{CaptchaStringList[10]}_{new_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[11], callback_data=f"textc_{CaptchaStringList[11]}_{new_chat_id}")]])
    
    return keyboard
