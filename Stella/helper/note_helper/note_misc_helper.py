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


from pyrogram.types import Message
from Stella.helper.chat_status import isUserAdmin

async def privateNote_and_admin_checker(message, text: str):
    privateNote = True
    if '{noprivate}' in text:
        privateNote = False 
    elif '{private}' in text:
        privateNote = True 
    else:
        privateNote = None

    allow = True
    if '{admin}' in text:
        if not await isUserAdmin(message, silent=True):
            allow = False 
        else:
            allow = True 
    
    return (
        privateNote,
        allow
    )

def preview_text_replace(text):
        if '{preview}' in text:
            text = text.replace('{preview}', '')
            preview =  False
        else:
            preview = True
        
        if '{admin}' in text:
            text = text.replace('{admin}', '')
        
        if '{private}' in text:
            text = text.replace('{private}', '')
        elif '{noprivate}' in text:
            text = text.replace('{noprivate}', '')
        
        return (
            preview, text
        )