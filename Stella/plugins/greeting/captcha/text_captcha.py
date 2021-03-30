import random
import string
import os

from pyrogram import filters
from pyrogram.types import ChatPermissions
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery
)
from captcha.image import ImageCaptcha

from Stella import StellaCli, BOT_USERNAME
from Stella.helper.button_gen import button_markdown_parser
from Stella.helper.chat_status import isUserAdmin

from Stella.database.welcome_mongo import (
    GetWelcome,
    GetCaptchaSettings,
    CaptchaChanceUpdater,
    GetChance,
    DeleteUsercaptchaData,
    AppendVerifiedUsers,
    isWelcome,
    SetCaptchaTextandChances,
    GetUserCaptchaMessageIDs,
    isUserVerified
)


CAPTCHA_START_STRINGS = [
(
    "Please complete the above CAPTCHA!\n\n"
    "You will be given `3` tries in order to get yourself verified and gain access to the chat."
),
(
    "CAPTCHA is not matched -  you've `2` tries left."
),
(
    "AGAIN incorrect - you now only have `1` try left.\n\n"
)
]

async def textCaptcha(chat_id, user_id):
    captcha_mode, captcha_text, captcha_kick_time = GetCaptchaSettings(chat_id)
    if captcha_mode == 'text':
        Captcha_button = (
            [
                [
                    InlineKeyboardButton(text=captcha_text, url=f'http://t.me/{BOT_USERNAME}?start=captcha_text_{user_id}_{chat_id}')
                ]
            ]
        )

        return Captcha_button


async def textCaptchaRedirect(message):
    user_id = message.from_user.id 
    if message.command[1].split('_')[1] == 'text':
        New_user_id = int(message.command[1].split('_')[2])
        New_chat_id = int(message.command[1].split('_')[3])
    
    if New_user_id == user_id:

        # Already Verified users
        if isUserVerified(New_chat_id, New_user_id):
            await message.reply(
                "You already passed the CAPTCHA, You don't need to verify yourself again.",
                quote=True
            )
            return

        # Admins captcha message
        if await isUserAdmin(message, chat_id=New_chat_id):
            await message.reply(
                "You are admin, You don't have to complete CAPTCHA.",
                quote=True
            )
            return

        # Captcha stuffs 
        CaptchaStringList = RandomStringGen()
        CaptchaString = random.choice(CaptchaStringList)

        CaptchaLoc = f"Stella/plugins/greeting/captcha/CaptchaDump/StellaCaptcha_text_{New_user_id}_{New_chat_id}.png"
        image = ImageCaptcha(width=1240, height=900, fonts=['path/font_03.ttf'], font_sizes=(240, 240))
        image.generate(CaptchaString)
        image.write(CaptchaString, CaptchaLoc)

        chance = GetChance(New_chat_id, New_user_id)
        if (
            chance == 0 
            or chance == None
        ):
            chance = 0 

        SetCaptchaTextandChances(New_chat_id, New_user_id, CaptchaString, chance, CaptchaStringList)
        keyboard = ButtonGen(CaptchaStringList, New_chat_id)
        
        await StellaCli.send_photo(
            chat_id=New_user_id,
            photo=CaptchaLoc,
            caption=CAPTCHA_START_STRINGS[chance],
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        os.remove(CaptchaLoc)

    else:
        # Admins captcha message
        if await isUserAdmin(message, chat_id=New_chat_id, silent=True):
            await message.reply(
                "You are admin, You don't have to complete CAPTCHA.",
                quote=True
            )
            return

        else:
            await message.reply(
                "This wasn't for you.",
                quote=True
            )
        

@StellaCli.on_callback_query(filters.create(lambda _,__, query: 'textc_' in query.data))
async def textCaptchaCallBack(client: StellaCli, callback_query: CallbackQuery):
    RandomString = callback_query.data.split('_')[1]
    chat_id = int(callback_query.data.split('_')[2])
    user_id = callback_query.from_user.id
    user_mention = callback_query.from_user.mention
    message_id, correct_captcha, chances, captcha_list = GetUserCaptchaMessageIDs(chat_id, user_id)

    if not RandomString == correct_captcha:
        chances += 1
        CaptchaChanceUpdater(chat_id, user_id, chances)
        
        await StellaCli.edit_message_caption(
            chat_id=user_id,
            message_id=callback_query.message.message_id,
            caption=CAPTCHA_START_STRINGS[chances],
            reply_markup=InlineKeyboardMarkup(ButtonGen(captcha_list, chat_id))
        )
    if chances == 3:
        await callback_query.edit_message_caption(
            caption="You failed this captcha"
        )
        await StellaCli.kick_chat_member(
                            chat_id=chat_id,
                            user_id=user_id
                        )
        
        await StellaCli.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=(
                f"User {user_mention} has failed the CAPTCHAs!"
            )
        )

    if RandomString == correct_captcha:
        str_chat_id = str(chat_id).replace('-100', '')
        PassedButton = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text='Go Back to the chat', url=f'http://t.me/c/{str_chat_id}/{message_id}')
                    ]
                ]
            )

        DeleteUsercaptchaData(chat_id, user_id)
        AppendVerifiedUsers(chat_id, user_id)
        
        await StellaCli.edit_message_caption(
            chat_id=user_id,
            message_id=callback_query.message.message_id,
            caption="you passed the captcha.",
            reply_markup=PassedButton
        )

        await StellaCli.restrict_chat_member(
                chat_id,
                user_id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_stickers=True,
                    can_send_animations=True,
                    can_send_games=True,
                    can_use_inline_bots=True,
                    can_add_web_page_previews=True,
                    can_send_polls=True
                )
            )
        
        if isWelcome(chat_id):
            Content, Text, DataType = GetWelcome(chat_id)
            Text, buttons = button_markdown_parser(Text)
            reply_markup = None
            if len(buttons) > 0:
                reply_markup = InlineKeyboardMarkup(buttons)
        else:
            reply_markup = None

        await StellaCli.edit_message_reply_markup(
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=reply_markup
        )


def ButtonGen(CaptchaStringList, New_chat_id):
    keyboard = ([[
        InlineKeyboardButton(text=CaptchaStringList[0], callback_data=f"textc_{CaptchaStringList[0]}_{New_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[1], callback_data=f"textc_{CaptchaStringList[1]}_{New_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[2], callback_data=f"textc_{CaptchaStringList[2]}_{New_chat_id}")]])
    keyboard += ([[
        InlineKeyboardButton(text=CaptchaStringList[3], callback_data=f"textc_{CaptchaStringList[3]}_{New_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[4], callback_data=f"textc_{CaptchaStringList[4]}_{New_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[5], callback_data=f"textc_{CaptchaStringList[5]}_{New_chat_id}")]])
    keyboard += ([[
        InlineKeyboardButton(text=CaptchaStringList[6], callback_data=f"textc_{CaptchaStringList[6]}_{New_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[7], callback_data=f"textc_{CaptchaStringList[7]}_{New_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[8], callback_data=f"textc_{CaptchaStringList[8]}_{New_chat_id}")]])
    keyboard += ([[
        InlineKeyboardButton(text=CaptchaStringList[9], callback_data=f"textc_{CaptchaStringList[9]}_{New_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[10], callback_data=f"textc_{CaptchaStringList[10]}_{New_chat_id}"),
        InlineKeyboardButton(text=CaptchaStringList[11], callback_data=f"textc_{CaptchaStringList[11]}_{New_chat_id}")]])
    
    return keyboard

def RandomStringGen() -> list:
    CaptchaStringList = []
    for x in range(12):
        CaptchaString = ''.join(
                random.SystemRandom().choice(
                string.ascii_letters + string.digits
                ) for _ in range(7)
                ).lower()
        CaptchaStringList.append(CaptchaString)
    return CaptchaStringList