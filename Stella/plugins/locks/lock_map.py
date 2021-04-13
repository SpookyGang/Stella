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