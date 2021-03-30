import asyncio
from requests import get
from Stella import StellaCli

async def getData(chat_id, message_id, GetWord, CurrentPage):
    UDJson = get(
            f'http://api.urbandictionary.com/v0/define?term={GetWord}').json()

    if not 'list' in UDJson:
        CNMessage = await StellaCli.send_message(
            chat_id=chat_id,
            reply_to_message_id=message_id,
            text=(
                f"Word: {GetWord}\n"
                "Results: Sorry could not find any matching results!"
            )
        )
        await asyncio.sleep(5)
        await CNMessage.delete()
        return
    try:
        index = int(CurrentPage - 1)
        PageLen = len(UDJson['list'])
        
        UDReasult = (
            f"**Definition of {GetWord}**\n"
            f"{UDJson['list'][index]['definition']}\n\n"
            "**📌 Examples**\n"
            f"__{UDJson['list'][index]['example']}__"
        )
        
        INGNORE_CHAR = "[]"
        UDFReasult = ''.join(i for i in UDReasult if not i in INGNORE_CHAR)
        
        return (
        UDFReasult,
        PageLen
        )

    except (
        IndexError
        or KeyError
    ):
        CNMessage = await StellaCli.send_message(
            chat_id=chat_id,
            reply_to_message_id=message_id,
            text=(
                f"Word: {GetWord}\n"
                "Results: Sorry could not find any matching results!"
            )
        )
        await asyncio.sleep(5)
        await CNMessage.delete()


    

