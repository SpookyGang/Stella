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


import html

from pyrogram import filters
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup
from Stella import BOT_ID, LOG_CHANNEL, OWNER_ID, SUDO_USERS, StellaCli
from Stella.database.federation_mongo import (get_fed_from_chat,
                                              get_fed_reason, is_user_fban)
from Stella.database.welcome_mongo import (DEFAUT_WELCOME, GetCaptchaSettings,
                                           GetCleanService, GetCleanWelcome,
                                           GetCleanWelcomeMessage, GetWelcome,
                                           GetWelcomemessageOnOff,
                                           SetCleanWelcomeMessage,
                                           SetUserCaptchaMessageIDs,
                                           isGetCaptcha, isReCaptcha,
                                           isUserVerified, isWelcome)
from Stella.helper.button_gen import button_markdown_parser
from Stella.helper.chat_status import isBotCan, isUserAdmin
from Stella.helper.welcome_helper.welcome_fillings import Welcomefillings
from Stella.helper.welcome_helper.welcome_send_message import \
    SendWelcomeMessage
from Stella.plugins.greeting.captcha import button_captcha, text_captcha


@StellaCli.on_message(filters.new_chat_members)
async def NewMemeber(client, message):
    
    chat_id = message.chat.id
    chat_title = html.escape(message.chat.title)
    message_id = message.message_id
    fed_id = get_fed_from_chat(chat_id)

    # Check if bot is admin to delete services messages 
    if GetCleanService(chat_id):
        if await isBotCan(message, permissions='can_delete_messages', silent=True):
            await message.delete()
        else:
            await message.reply(
                "I dont have much permssion in this chat to clean service messages."
            )
        
    if GetCleanWelcome(chat_id):
        CleanWelcomeMessageID = GetCleanWelcomeMessage(chat_id)
        if not CleanWelcomeMessageID is None:
            await StellaCli.delete_messages(
                    chat_id=chat_id,
                    message_ids=CleanWelcomeMessageID
                )
                
    for NewUserJson in message.new_chat_members:
        user_id = NewUserJson.id

        # Stella Welcome stuffs
        if user_id == BOT_ID:
            await message.reply(
                (
                    "Thank you for adding me! — Checkout my support channel for updates and support chat to seek help.\n\n"
                    "**Channel:** @StellaUpdates\n"
                    "**Support Chat:** @StellaSupportChat\n\n"
                    "See you on the other side ^^"
                )
            )
            await StellaCli.send_message(
                chat_id=LOG_CHANNEL,
                text=(
                    f"I've been added to `{chat_title}` with ID: `{chat_id}`\n"
                    f"Added by: @{message.from_user.username} ( `{message.from_user.id}` )"
                )
            )
            return 
        
        # Stella's Special welcome for kami-samas!
        if user_id in OWNER_ID:
            await message.reply(
                "Omfg, the old man's here. I'm scared! >.<"
            )
            return 
        
        # Stella's Special welcome for her onii-chan gang!
        if user_id in SUDO_USERS:
            await message.reply(
                "Onii-chan is here owo!"
            )
            return

        # New Join memebers Scan Banned users 
        if is_user_fban(fed_id, user_id):
                fed_reason = get_fed_reason(fed_id, user_id)
                text = (
                        "**This user is banned in the current federation:**\n\n"
                        f"User: {NewUserJson.mention} (`{NewUserJson.id}`)\n"
                        f"Reason: `{fed_reason}`"
                    )

                if await isBotCan(message, permissions='can_restrict_members'):
                    if await StellaCli.kick_chat_member(chat_id, user_id): 
                        text += '\nAction: `Banned`'
                        
                await message.reply(
                    text
                )
                return 
        
        
        # Captcha stuffs 
        if isGetCaptcha(chat_id):
            if await isBotCan(message, permissions='can_restrict_members'):
                
                if not isReCaptcha(chat_id):
                    # Already Verified users  
                    if not (
                        isUserVerified(chat_id, user_id)
                        or await isUserAdmin(message, chat_id=chat_id, silent=True)
                    ):
                        await StellaCli.restrict_chat_member(
                                chat_id,
                                user_id,
                                ChatPermissions(
                                    can_send_messages=False
                                )
                            )
                else:
                    if not await isUserAdmin(message, chat_id=chat_id, silent=True):
                        await StellaCli.restrict_chat_member(
                                chat_id,
                                user_id,
                                ChatPermissions(
                                    can_send_messages=False
                                )
                            )
            else:
                await message.reply(
                    "I haven't got the rights to mute people."
                )
            
            # Captcha modes button/text/math
            captcha_mode, captcha_text, captcha_kick_time = GetCaptchaSettings(chat_id)
            if (
                captcha_mode is None
                or captcha_mode == 'button'
            ):
                CaptchaButton = await button_captcha.CaptchaButton(chat_id, user_id)
            
            elif captcha_mode in [
                'text',
                'math'
            ]:
                CaptchaButton = await text_captcha.textCaptcha(chat_id, user_id)
            
        else:
            CaptchaButton = None
        
        # If user welcome set welcome 
        if isWelcome(chat_id):
            # If welcome: ON 
            if GetWelcomemessageOnOff(chat_id):
                Content, Text, DataType = GetWelcome(chat_id)
                Text, buttons = button_markdown_parser(Text)

                if CaptchaButton is None:
                    reply_markup = None

                # If welcome message has button greater than 0
                if len(buttons) > 0:
                    if not CaptchaButton is None:
                        reply_markup = InlineKeyboardMarkup(buttons + CaptchaButton)
                        # Already Verified users
                        if not isReCaptcha(chat_id):
                            if isUserVerified(chat_id, user_id):
                                reply_markup = InlineKeyboardMarkup(buttons)

                        # Admins captcha message
                        if await isUserAdmin(message, chat_id=chat_id, silent=True):
                            reply_markup = InlineKeyboardMarkup(buttons)
                    else:
                        reply_markup = InlineKeyboardMarkup(buttons)
                else:
                    reply_markup = None
                    if not CaptchaButton is None:
                        reply_markup = InlineKeyboardMarkup(CaptchaButton)
                        # Already Verified users
                        if not isReCaptcha(chat_id):
                            if isUserVerified(chat_id, user_id):
                                reply_markup = None
                        else:
                            reply_markup = InlineKeyboardMarkup(CaptchaButton)
                            
                        # Admins captcha message
                        if await isUserAdmin(message, chat_id=chat_id, silent=True):
                            reply_markup = None

                WelcomeSentMessage = await SendWelcomeMessage(message, NewUserJson, Content, Text, DataType, reply_markup=reply_markup)
                message_id = WelcomeSentMessage.message_id

                # Saved current welcome sent message_id in Db which is use in for deleted old message if /cleanwelcome: ON
                SetNewMemMessageIDs(chat_id, user_id, message_id)
        else:
            # If welcome has No any messages set 
            Text = Welcomefillings(message, DEFAUT_WELCOME, NewUserJson)

            if CaptchaButton is None:
                reply_markup = None
            else:
                reply_markup = InlineKeyboardMarkup(CaptchaButton)

            WelcomeSentMessage = await StellaCli.send_message(
                chat_id=chat_id,
                text=Text,
                reply_to_message_id=message_id,
                reply_markup=reply_markup
                )

            message_id = WelcomeSentMessage.message_id
            SetNewMemMessageIDs(chat_id, user_id, message_id)

def SetNewMemMessageIDs(chat_id, user_id, message_id):
    print(isGetCaptcha(chat_id))
    if isGetCaptcha(chat_id):
        captcha_mode, captcha_text, captcha_kick_time = GetCaptchaSettings(chat_id)
        if (
            captcha_mode in [
                'text',
                'button',
                'math'
            ]
        ):
            SetUserCaptchaMessageIDs(chat_id, user_id, message_id)

    if GetCleanWelcome(chat_id):
        SetCleanWelcomeMessage(chat_id, message_id)
            