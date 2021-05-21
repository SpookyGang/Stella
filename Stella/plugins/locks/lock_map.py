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

from enum import Enum, auto

class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.name, cls))

class LocksMap(ExtendedEnum):
    all = auto()
    album = auto()
    audio = auto()
    bot = auto()
    button = auto()
    command = auto()
    comment = auto()
    contact = auto()
    document = auto()
    email = auto() 
    emojigame = auto()
    forward = auto() 
    forwardbot = auto() 
    forwardchannel = auto()
    forwarduser = auto() 
    game = auto()
    gif = auto()
    inline = auto() 
    invitelink = auto() 
    location = auto() 
    phone = auto()
    photo = auto()
    poll = auto()
    rtl = auto() 
    sticker = auto()
    text = auto()
    url = auto() 
    video = auto()  
    videonote = auto()  
    voice = auto() 