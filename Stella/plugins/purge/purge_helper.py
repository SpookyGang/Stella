
def PurgeDictDataUpdater(chat_id, purge_from=None, purge_to=None, first_messageID=None, purge_from_messageID=None):
    PurgeData = PurgeDictData.PurgeDict
    if purge_to == None:
        PurgeData.update(
            {
                chat_id: {
                    "purge_from": purge_from,
                    "first_messageID": first_messageID,
                    "purge_from_messageID": purge_from_messageID
                }
            }
        )
    elif purge_from == None:
        PurgeData[chat_id].update(
            {
                "purge_to": purge_to
            }
        )
    
    

class PurgeDictData:
    PurgeDict = dict()