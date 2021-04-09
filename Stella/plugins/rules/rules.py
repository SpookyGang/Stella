import html

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Stella import StellaCli, BOT_USERNAME

from Stella.helper import custom_filter
from Stella.helper.get_data import GetChat
from Stella.helper.button_gen import button_markdown_parser
from Stella.helper.note_helper.note_fillings import NoteFillings as rules_filler
from Stella.helper.disable import disable

from Stella.database.rules_mongo import (
    get_rules,
    get_rules_button,
    get_private_note
)

@StellaCli.on_message(custom_filter.command(commands=('rules'), disable=True))
@disable
async def rules(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title 
    rules_text = get_rules(chat_id)
    if rules_text is None:
        await message.reply(
            "This chat doesn't seem to have had any rules set yet... I wouldn't take that as an invitation though.",
            quote=True
        )
        return
    
    if not get_private_note(chat_id):
        rules_text, buttons = button_markdown_parser(rules_text)
        button_markdown = None
        if len(buttons) > 0:
            button_markdown = InlineKeyboardMarkup(buttons)

        rules_text = rules_filler(message, rules_text)

        await message.reply(
            (
                f"The rules for `{html.escape(chat_title)}` are:\n\n"
                f"{rules_text}"
            ),
            reply_markup=button_markdown,
            quote=True
        )
    else:
        button_text = get_rules_button(chat_id)
        button = [[InlineKeyboardButton(text=button_text, url=f'http://t.me/{BOT_USERNAME}?start=rules_{chat_id}')]]

        await message.reply(
            "Click on the button to see the chat rules!",
            reply_markup=InlineKeyboardMarkup(button),
            quote=True
        )

async def rulesRedirect(message):
    chat_id = int(message.command[1].split('_')[1])
    chat_title = await GetChat(chat_id)
    rules_text = get_rules(chat_id)
    
    rules_text, buttons = button_markdown_parser(rules_text)
    button_markdown = None
    if len(buttons) > 0:
        button_markdown = InlineKeyboardMarkup(buttons)

    rules_text = rules_filler(message, rules_text)
    await message.reply(
        (
            f"The rules for `{html.escape(chat_title)}` are:\n\n"
            f"{rules_text}"
        ),
        reply_markup=button_markdown,
        quote=True
    )
