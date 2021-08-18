#    Stella (Development)
#    Copyright (C) 2021 - meanii (Anil Chauhan)
#    Copyright (C) 2021 - SpookyGang (Neel Verma, Anil Chauhan)

#    This program is free software; you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by 
#    the Free Software Foundation; either version 3 of the License, or 
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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

    except (IndexError, KeyError):
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


    

