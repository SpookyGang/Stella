from Stella import StellaDB

notes = StellaDB.notes

notes_data = notes.find({})

def __stats__():
    TOTAL_NOTES = []
    TOTAL_CHATS = notes.count_documents({})     

    notes_data = notes.find()
    for chat_notes in notes_data:
        num_of_notes = len(chat_notes['notes'])
        TOTAL_NOTES.append(num_of_notes)
    text = f"Minna has saved `{sum(TOTAL_NOTES)}` notes and the number of chats that have saved is `{TOTAL_CHATS}`.\n"
    return text