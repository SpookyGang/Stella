from Stella import StellaDB

notes = StellaDB.notes

def SaveNote(chat_id, note_name, content, text, data_type):
    GetNotes = notes.find_one(
        {
            'chat_id': chat_id
        }
    )
    totalNote = notes.count_documents({})
    NotesIDs = totalNote + 1

    if GetNotes == None:
        NoteData = {
            '_id': NotesIDs,
            'chat_id': chat_id,
            'notes': [
                {   
                    '_id': 1,
                    'note_name': note_name,
                    'content': content,
                    'text': text,
                    'data_type': data_type
                }
            ]
        }

        notes.insert_one(
            NoteData
        )
    else:
        NotesNamesList = []
        if 'notes' in GetNotes:
            totalNote = len(GetNotes['notes'])
            NotesIDs = totalNote + 1

            notesDict = GetNotes['notes']

            for get_notes in notesDict:
                note = get_notes['note_name']
                NotesNamesList.append(note)

            if note_name in NotesNamesList:
                notes.update(
                    {
                        'chat_id': chat_id,
                        'notes.note_name' : note_name 
                    },
                    {
                        "$set": {
                            'notes.$.note_name': note_name,
                            'notes.$.content': content,
                            'notes.$.text': text,
                            'notes.$.data_type': data_type
                            }
                        },
                        False,
                        True
                    )
        
            else:
                notes.update_one(
                    {
                        'chat_id': chat_id
                    },
                    {
                        "$push": {
                            'notes': {
                                '_id': NotesIDs,
                                'note_name': note_name,
                                'content': content,
                                'text': text,
                                'data_type': data_type
                            }
                        }
                    },
                    upsert=True
                )
        else:
            notes.update_one(
                {
                    'chat_id': chat_id
                },
                {
                    "$set": {
                        'notes': [
                            {
                                '_id': NotesIDs,
                                'note_name': note_name,
                                'content': content,
                                'text': text,
                                'data_type': data_type
                            }
                        ]
                    }
                }
            )
def GetNote(chat_id, note_name):
    GetNoteData = notes.find_one(
        {
            'chat_id': chat_id
        }
    )

    if not GetNoteData == None:
        Getnotes = GetNoteData['notes']
        for note in Getnotes:
            GetNote = note['note_name']
            if GetNote == note_name:
                content = note['content']
                text = note['text']
                data_type = note['data_type']
                return (
                    content,
                    text,
                    data_type
                )
    else:
        return None 

def isNoteExist(chat_id, note_name) -> bool:
    GetNoteData = notes.find_one(
        {
                'chat_id': chat_id
            }
        )
    if (
        GetNoteData is not None
        and 'notes' in GetNoteData
    ):
        gnotes = GetNoteData['notes']
        notes_list = []
        for Getnotes in gnotes:
            n_name = Getnotes['note_name']
            notes_list.append(n_name)
        if note_name in notes_list: 
            return True 
        else:
            return False
    return False

def NoteList(chat_id) -> list:
    NotesNamesList = []
    GetNoteData = notes.find_one(
        {
            'chat_id': chat_id
        }
    )
    if not GetNoteData == None:
        if 'notes' in GetNoteData:
            Getnotes = GetNoteData['notes']
            for note in Getnotes:
                NoteText = note['text']
                NoteNames = note['note_name']
                if '{admin}' in NoteText:
                        NoteNames = NoteNames + ' ' + '__{admin}__'
                NotesNamesList.append(NoteNames)
            return NotesNamesList
        else:
            return NotesNamesList
    else:
        return NotesNamesList


def ClearNote(chat_id, note_name):
    notes.update(
        {
            'chat_id': chat_id
        },
        {
            "$pull": {
                'notes': {
                    'note_name': note_name
                }
            }
        }
    )

def set_private_note(chat_id, private_note):
    notes.update_one(
        {
            'chat_id': chat_id
        },
        {
            "$set": {
                'private_note': private_note
            }
        },
        upsert=True
    )

def is_pnote_on(chat_id) -> bool:
    GetNoteData = notes.find_one(
        {
                'chat_id': chat_id
            }
        )
    if not GetNoteData == None:
        if 'private_note' in GetNoteData:
            private_note = GetNoteData['private_note']
            return private_note
        else:
            return False 
    else: 
        return False 

def ClearAllNotes(chat_id):
    notes.update(
        {
            'chat_id': chat_id
        },
        {
            "$unset": {
                'notes': []
            }
        }
    )
