import re
import html
from Stella.__main__ import HELPABLE
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Stella import StellaCli, BOT_USERNAME
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
    if message.chat.type != "private":
        buttons = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text='help', url=f"t.me/{BOT_USERNAME}?start=help")]])
        await message.reply('start me in PM', reply_markup=buttons)
    else:
        await help_parser(client, message.chat.id, HELP_TEXT)


async def help_button_callback(_, __, query):
    if re.match(r"help_", query.data):
        return True


@StellaCli.on_callback_query(filters.create(help_button_callback))
async def help_button(_client, query):
    
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    if mod_match:
        module = mod_match.group(1)
        text = f"**{HELPABLE[module].__mod_name__}**\n\n"
        text += HELPABLE[module].__help__

        await query.message.edit(
            text=html.escape(text),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text='Back ', callback_data="help_back")]])
            )

    elif back_match:
        await query.message.edit(text=HELP_TEXT,
                    reply_markup=InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help")))