from pyrogram import filters
from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.note_helper.note_send_message import exceNoteMessageSender
from Stella.helper.note_helper.note_misc_helper import private_note_and_admin_checker

from Stella.database.notes_mongo import (
    isNoteExist,
    is_pnote_on,
    GetNote
)
from Stella.plugins.notes.private_notes import PrivateNoteButton
from Stella.plugins.connection.connection import connection

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

    NoteName = message.command[1]
    if not isNoteExist(chat_id, NoteName):
        await message.reply(
            'Note not found!'
        )
        return
        
    await send_note(message, NoteName)
    

@StellaCli.on_message(filters.regex(pattern=(r"^#[^\s]+")))
async def regex_get_note(client, message):
    chat_id = message.chat.id
    if message.from_user:
        NoteName = message.text.split()[0].replace('#', '')
        if isNoteExist(chat_id, NoteName):
            await send_note(message, NoteName)


async def send_note(message, NoteName):
    if await connection(message) is not None:
        chat_id = await connection(message)
        Content, Text, DataType = GetNote(chat_id, NoteName)
        await exceNoteMessageSender(message, NoteName)
        return

    else:
        chat_id = message.chat.id

    Content, Text, DataType = GetNote(chat_id, NoteName)
    
    PRIVATE_NOTE, ALLOW = await private_note_and_admin_checker(message, Text)
    
    if ALLOW: 
        if PRIVATE_NOTE == None:
            if is_pnote_on(chat_id):
                await PrivateNoteButton(message, chat_id, NoteName)
            else:
                await exceNoteMessageSender(message, NoteName)
            
            return
        
        elif PRIVATE_NOTE is not None:
            if (
                is_pnote_on(chat_id)
            ):
                if PRIVATE_NOTE:
                    await PrivateNoteButton(message, chat_id, NoteName)
                else:
                    await exceNoteMessageSender(message, NoteName)
            else: 
                if PRIVATE_NOTE:
                    await PrivateNoteButton(message, chat_id, NoteName)
                else:
                    await exceNoteMessageSender(message, NoteName)

