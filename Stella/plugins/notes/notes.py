import html

from Stella import StellaCli
from Stella.database.notes_mongo import NoteList
from Stella.helper import custom_filter
from Stella.helper.disable import disable
from Stella.helper.get_data import GetChat
from Stella.plugins.connection.connection import connection


@StellaCli.on_message(custom_filter.command(commands=(['notes', 'saved']), disable=True))
@disable
async def Notes(client, message):
    if await connection(message) is not None:
        chat_id = await connection(message)
        chat_title = await GetChat(chat_id)
    else:    
        chat_id = message.chat.id
        chat_title = message.chat.title

        if (
            message.chat.type == 'private'
        ):
            chat_title = 'local'

    Notes_list = NoteList(chat_id)
    
    NoteHeader = f"List of notes  in {html.escape(chat_title)}:\n"
    if (
        len(Notes_list) != 0
    ): 
        for notes in Notes_list:
            NoteName = f" • `#{notes}`\n"
            NoteHeader += NoteName
        await message.reply(
            (
                f"{NoteHeader}\n"
                "You can retrieve these notes by using `/get notename`, or `#notename`"
            ),
            quote=True
        )
        
    else:
        await message.reply(
            f"No notes in {chat_title}.",
            quote=True
        )
