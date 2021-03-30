from pyrogram.types import InlineKeyboardMarkup
from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAdmins
from Stella.helper.welcome_helper.welcome_send_message import SendWelcomeMessage
from Stella.helper.welcome_helper.welcome_fillings import Welcomefillings
from Stella.helper.button_gen import button_markdown_parser
from Stella.helper.anon_admin import anonadmin_checker

from Stella.database.welcome_mongo import (
    GetWelcome,
    SetWelcomeMessageOnOff,
    GetWelcomemessageOnOff,
    GetCaptchaSettings,
    isGetCaptcha,
    isWelcome,
    GetCleanService,
    DEFAUT_WELCOME
)

from Stella.plugins.connection.connection import connection


WELCOME_TRUE = ['on', 'yes']
WELCOME_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands=('welcome')))
async def Welcome(client, message):

    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id

    if not await CheckAdmins(message):
        return

    if len(message.command) >= 2:
        GetWelcomeArg = message.command[1]
        if (
            GetWelcomeArg in WELCOME_TRUE
        ):
            SetWelcomeMessageOnOff(chat_id, welcome_message=True)  
            await message.reply(
                "I'll be welcoming all new members from now on!",
                quote=True
            )
        
        elif (
            GetWelcomeArg in WELCOME_FALSE
        ):
            SetWelcomeMessageOnOff(chat_id, welcome_message=False)
            await message.reply(
                "I'll stay quiet when new members join.",
                quote=True
            )
        
        elif (
            GetWelcomeArg == 'noformat'
        ):
            await welcomeformat(message, chat_id, noformat=True)

        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off",
                quote=True
            )

    elif len(message.command) == 1:
        await welcomeformat(message, chat_id, noformat=False)

async def welcomeformat(message, chat_id, noformat=True):
    if GetWelcomemessageOnOff(chat_id):
        WelcomeMessage = 'true'
    else:
        WelcomeMessage = 'false' 
    
    if GetCleanService(chat_id):
        CleanService = 'true'
    else:
        CleanService = 'false'

    if isGetCaptcha(chat_id):
        captcha_mode, captcha_text, captcha_kick_time = GetCaptchaSettings(chat_id)

        if captcha_mode == None:
            captcha_mode = 'button'
        
        if captcha_text == None:
            captcha_text = "Click here to prove you're human"
        
        if captcha_kick_time == None:
            captcha_kick_time = "disabled"
        
        captcha = (
            f"The current CAPTCHA mode is: `{captcha_mode}`\n"
            f"The CAPTCHA button will say: `{captcha_text}`\n"
            f"CAPTCHA kicks are currently: `{captcha_kick_time}`\n\n"
        )
    else:
        captcha = "CAPTCHAs are disabled.\n"

    WELCOME_MESSAGE = (
        f"I am currently welcoming users: `{WelcomeMessage}`\n"
        f"I am currently deleting services: `{CleanService}`\n"
        f"{captcha}"
        "Members are currently welcomed with:"
    )

    WelcomeSentMessage = await message.reply(
        WELCOME_MESSAGE,
        quote=True
    )

    if isWelcome(chat_id):
        Content, Text, DataType = GetWelcome(chat_id)
        Text, buttons = button_markdown_parser(Text)

        reply_markup = None
        if len(buttons) > 0:
            reply_markup = InlineKeyboardMarkup(buttons)
        if noformat:
            WelcomeSentMessage = await SendWelcomeMessage(WelcomeSentMessage, None, Content, Text, DataType, reply_markup=reply_markup)
        else:
            WelcomeSentMessage = await SendWelcomeMessage(WelcomeSentMessage, message.from_user, Content, Text, DataType, reply_markup=reply_markup)
    else:
        if noformat:
            await WelcomeSentMessage.reply(
                DEFAUT_WELCOME
            )
        else:
            welcome_message = Welcomefillings(message, DEFAUT_WELCOME, message.from_user)
            await WelcomeSentMessage.reply(
                welcome_message
            )