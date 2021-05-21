import html
import re

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Stella import BOT_USERNAME, StellaCli
from Stella.__main__ import HELPABLE
from Stella.helper import custom_filter
from Stella.helper.pagination_buttons import paginate_modules

HELP_TEXT = (
    "Here you can find information regarding how to use me. I'll guide you through all the modules I have to offer.\n\n"
    "**Pro-tip**: you can use either \"`/`\" or \"`!`\" to command me!\n\n"
    "» If you encounter any bugs, please feel free to report them in my support chat - @StellaSupportChat ^^"
)

async def help_parser(client, chat_id, text, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    await client.send_message(chat_id, text, reply_markup=keyboard)


@StellaCli.on_message(custom_filter.command(commands=('help')))
async def help_command(client, message):

    module_name = None
    if len(message.command) >= 2:
        module_name = message.command[1].lower()

    if message.chat.type != "private":

        button_text = 'Click me here for help!'
        text = 'Contact me in PM for help!'
        redirect_url = f"t.me/{BOT_USERNAME}?start=help_"

        if module_name is not None:

            try:
                module_name = HELPABLE[module_name].__mod_name__
                text = f"Help for `{module_name.capitalize()}` module!" 
                button_text = 'Click here!'
                redirect_url = f"t.me/{BOT_USERNAME}?start=help_{module_name.lower()}"
            except KeyError:
                pass
        
        buttons = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=button_text, url=redirect_url)]])
        await message.reply(text, reply_markup=buttons)
    else:
        if module_name is not None:
            await module_page(message, module=module_name)
        else:
            await help_parser(client, message.chat.id, HELP_TEXT)


@StellaCli.on_message(custom_filter.command('start'), group=9)
async def redirectHelp(client, message):
    if (
        len(message.command) >= 2
        and message.command[1].split('_')[0] == 'help'
    ):
        if len(message.command) >= 2:
            module_name = message.command[1].split('_')[1]
            await module_page(message, module=module_name)
        else:
            await help_parser(StellaCli, message.chat.id, HELP_TEXT)

async def help_button_callback(_, __, callback_query):
    if re.match(r"help_", callback_query.data):
        return True


@StellaCli.on_callback_query(filters.create(help_button_callback))
async def help_button(client, callback_query):

    mod_match = re.match(r"help_module\((.+?)\)", callback_query.data)
    back_match = re.match(r"help_back", callback_query.data)
    if mod_match:
        module = mod_match.group(1)
        text = f"**{HELPABLE[module].__mod_name__}**\n\n"
        text += HELPABLE[module].__help__
        await callback_query.message.edit(
            text=html.escape(text),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text='Back ', callback_data="help_back")]])
        )

    elif back_match:
        await callback_query.message.edit(text=HELP_TEXT,
                    reply_markup=InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help")))

async def module_page(message: str, module: str):
    try:
        text = f"**{HELPABLE[module].__mod_name__}**\n\n"
        text += HELPABLE[module].__help__
    except KeyError:
        await help_parser(StellaCli, message.chat.id, HELP_TEXT)
        return 

    await message.reply(
        text=html.escape(text),
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text='Back ', callback_data="help_back")]]),
        quote=True
        )