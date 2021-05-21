from pyrogram import filters
from pyrogram.types import Message
from Stella import StellaCli
from Stella.database.notes_mongo import GetNote, is_pnote_on, isNoteExist
from Stella.helper import custom_filter
from Stella.helper.note_helper.note_misc_helper import \
    privateNote_and_admin_checker
from Stella.helper.note_helper.note_send_message import exceNoteMessageSender
from Stella.plugins.connection.connection import connection

from .private_notes import PrivateNoteButton


@StellaCli.on_message(custom_filter.command(commands=('get')))
async def getNote(client, message):

    chat_id = message.chat.id
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You need to give the note a name!"
        )
        return  

    note_name = message.command[1]
    if not isNoteExist(chat_id, note_name):
        await message.reply(
            'Note not found!'
        )
        return
        
    await send_note(message, note_name)
    

@StellaCli.on_message(filters.regex(pattern=(r"^#[^\s]+")))
async def regex_get_note(client, message):
    chat_id = message.chat.id
    if message.from_user:
        note_name = message.text.split()[0].replace('#', '')
        if isNoteExist(chat_id, note_name):
            await send_note(message, note_name)


async def send_note(message: Message, note_name: str):
    
    chat_id = message.chat.id  
    content, text, data_type = GetNote(chat_id, note_name)
    privateNote, allow = await privateNote_and_admin_checker(message, text)
    
    if allow:
        if privateNote == None:
            if is_pnote_on(chat_id):
                await PrivateNoteButton(message, chat_id, note_name)
            else:
                await exceNoteMessageSender(message, note_name)
            
        elif privateNote is not None:
            if is_pnote_on(chat_id):
                if privateNote:
                    await PrivateNoteButton(message, chat_id, note_name)
                else:
                    await exceNoteMessageSender(message, note_name)
            else: 
                if privateNote:
                    await PrivateNoteButton(message, chat_id, note_name)
                else:
                    await exceNoteMessageSender(message, note_name)

