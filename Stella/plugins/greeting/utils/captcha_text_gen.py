from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

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
