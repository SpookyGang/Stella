import os
import random
import string

from pyrogram import filters
from pyrogram.types import (CallbackQuery, ChatPermissions,
                            InlineKeyboardButton, InlineKeyboardMarkup)
from Stella import BOT_USERNAME, StellaCli
from Stella.database.welcome_mongo import (AppendVerifiedUsers,
                                           CaptchaChanceUpdater,
                                           DeleteUsercaptchaData,
                                           GetCaptchaSettings, GetChance,
                                           GetUserCaptchaMessageIDs,
                                           GetWelcome,
                                           SetCaptchaTextandChances,
                                           isReCaptcha, isRuleCaptcha,
                                           isUserVerified, isWelcome)
from Stella.helper.button_gen import button_markdown_parser
from Stella.helper.chat_status import isUserAdmin

from captcha.image import ImageCaptcha

from ..utils.actions import failedAction, passedAction
from ..utils.captcha_text_gen import ButtonGen
from ..utils.random_string_gen import RandomStringGen, mathCaptchaGen
from .captcharules_button import ruleCaptchaButton

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
    if captcha_mode in [
        'text',
        'math'
    ]:
        Captcha_button = (
            [
                [
                    InlineKeyboardButton(text=captcha_text, url=f'http://t.me/{BOT_USERNAME}?start=captcha_{captcha_mode}_{user_id}_{chat_id}')
                ]
            ]
        )

        return Captcha_button


async def textCaptchaRedirect(message):
    user_id = message.from_user.id 
    chat_id = message.chat.id
    _match = message.command[1].split('_')[1]

    if _match in [
        'text',
        'math'
    ]:
        new_user_id = int(message.command[1].split('_')[2])
        new_chat_id = int(message.command[1].split('_')[3])
    
        if new_user_id == user_id:

            # Already Verified users
            if not isReCaptcha(chat_id=new_chat_id):
                if isUserVerified(new_chat_id, new_user_id):
                    await message.reply(
                        "You already passed the CAPTCHA, You don't need to verify yourself again.",
                        quote=True
                    )
                    return

            # Admins captcha message
            if await isUserAdmin(message, pm_mode=True, chat_id=new_chat_id, user_id=new_user_id, silent=True):
                await message.reply(
                    "You are admin, You don't have to complete CAPTCHA.",
                    quote=True
                )
                return

            
            # Captcha generating 
            if _match == 'text':
                CaptchaStringList = RandomStringGen()
                CaptchaString = random.choice(CaptchaStringList)

            elif _match == 'math':
                answer_dict, CaptchaStringList = mathCaptchaGen()
                print(answer_dict)
                CaptchaString = f"{answer_dict.get('num01')} + {answer_dict.get('num02')} = ?"
            

            CaptchaLoc = f"Stella/plugins/greeting/captcha/CaptchaDump/StellaCaptcha_text_{new_user_id}_{new_chat_id}.png"
            image = ImageCaptcha(width=270, height=90, fonts=['path/font_03.ttf'], font_sizes=(50, 50))
            image.generate(CaptchaString)
            image.write(CaptchaString, CaptchaLoc)

            chance = GetChance(new_chat_id, new_user_id)
            
            if chance is None:
                chance = 0

            if chance >= 3:
                message_id, correct_captcha, chances, captcha_list = GetUserCaptchaMessageIDs(chat_id=new_chat_id, user_id=new_user_id)
                await failedAction(message=message, user_id=new_user_id, chat_id=new_chat_id, message_id=message_id)
                await message.reply(
                    'You have lost your\'ll 3 CAPTCHA\'s chances'
                )
                return

            if _match == 'math':
                CaptchaString = answer_dict.get('answer')

            SetCaptchaTextandChances(new_chat_id, new_user_id, str(CaptchaString), chance, CaptchaStringList)
            keyboard = ButtonGen(CaptchaStringList, new_chat_id)
            
            await StellaCli.send_photo(
                chat_id=new_user_id,
                photo=CaptchaLoc,
                caption=CAPTCHA_START_STRINGS[chance],
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
            os.remove(CaptchaLoc)

        else:
            # Admins captcha message
            if await isUserAdmin(message, pm_mode=True, chat_id=new_chat_id, user_id=new_user_id, silent=True):
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
    
    if (
        not isReCaptcha(chat_id=chat_id)
        and isUserVerified(chat_id=chat_id, user_id=user_id)
    ):
        await StellaCli.edit_message_caption(
            chat_id=user_id,
            message_id=callback_query.message.message_id,
            caption='You\'ve already completed the CAPTCHA!'
            )

    if GetUserCaptchaMessageIDs(chat_id=chat_id, user_id=user_id) is None:
        await StellaCli.edit_message_caption(
            chat_id=user_id,
            message_id=callback_query.message.message_id,
            caption='Something went wrong, try agian.'
            )
        return
    
    message_id, correct_captcha, chances, captcha_list = GetUserCaptchaMessageIDs(chat_id, user_id)
    
    # if chances is 3 reached 
    if chances >= 2:
        await callback_query.edit_message_caption(
            caption="You failed this captcha"
        )
        await failedAction(message=callback_query, user_id=user_id, chat_id=chat_id, message_id=message_id)
        
    # When user clicked on wrong button
    elif (
        RandomString != correct_captcha
    ):
        chances += 1
        CaptchaChanceUpdater(chat_id, user_id, chances)
        
        await StellaCli.edit_message_caption(
            chat_id=user_id,
            message_id=callback_query.message.message_id,
            caption=CAPTCHA_START_STRINGS[chances],
            reply_markup=InlineKeyboardMarkup(ButtonGen(captcha_list, chat_id))
        )

        await callback_query.answer(
            text=(
                'You have clicked on wrong CAPTCHA button.'
            )
        )

    # When use click on correct CAPTCHA button
    elif RandomString == correct_captcha:

        # Check in re CAPTCHA is enable
        if isRuleCaptcha(chat_id=chat_id):
            await StellaCli.delete_messages(
                chat_id=user_id, 
                message_ids=callback_query.message.message_id
                )
            await ruleCaptchaButton(message=callback_query, chat_id=chat_id, message_id=message_id)
        else:
            str_chat_id = str(chat_id).replace('-100', '')
            PassedButton = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text='Go Back to the chat', url=f'http://t.me/c/{str_chat_id}/{message_id}')
                        ]
                    ]
                )

            await StellaCli.edit_message_caption(
                chat_id=user_id,
                message_id=callback_query.message.message_id,
                caption="you passed the captcha.",
                reply_markup=PassedButton
            )

            await callback_query.answer(
                text=(
                    'You  have passed the CAPTCHA.'
                )
            )

            await passedAction(chat_id=chat_id, user_id=user_id, message_id=message_id)
