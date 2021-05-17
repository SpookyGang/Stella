from Stella import StellaDB

welcome = StellaDB.welcome

DEFAUT_WELCOME = "Hey there {first}, and welcome to {chatname}! How are you?"
DEFAUT_GOODBYE = "{first}, left the chat!"


def SetWelcome(chat_id, Content, Text, DataType):
    
    WelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    WelcomeDataCount = welcome.count_documents({})
    WelcomeIDs = WelcomeDataCount + 1

    if WelcomeData == None:
        WelcomeSetData = {
            '_id': WelcomeIDs,
            'welcome': True,
            'chat_id': chat_id,
            'welcome_message': {
                'content': Content,
                'text': Text,
                'data_type': DataType,
            },
            'clean_service': False
        }

        welcome.insert_one(
            WelcomeSetData
        )

    else:
        welcome.update_one(
            {
                'chat_id': chat_id
            },
            {
                "$set": {
                    'welcome_message.content': Content,
                    'welcome_message.text': Text,
                    'welcome_message.data_type': DataType
                }
            }
        )

def UnSetWelcome(chat_id):
    WelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    if not WelcomeData == None:
        if 'text' in WelcomeData['welcome_message']:
            welcome.update_one(
                {
                    'chat_id': chat_id
                },
                {
                    "$unset":{
                        'welcome_message.content': None,
                        'welcome_message.text': None,
                        'welcome_message.data_type': None
                    }
                }
            )

def GetWelcome(chat_id):

    GetWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    if not (
        GetWelcomeData == None
    ):
        if 'text' in GetWelcomeData['welcome_message']:
            Content = GetWelcomeData['welcome_message']['content']
            Text = GetWelcomeData['welcome_message']['text']
            DataType = GetWelcomeData['welcome_message']['data_type']
            return (
                Content,
                Text,
                DataType
            )


def SetWelcomeMessageOnOff(chat_id, welcome_message):
    
    welcome.update_one(
            {
                'chat_id': chat_id
            },
            {
                "$set": {
                    'welcome': welcome_message
                    }
            }
        )

def GetWelcomemessageOnOff(chat_id) -> bool:
    GetWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    if not GetWelcomeData == None:
        if 'welcome' in GetWelcomeData:
            return GetWelcomeData['welcome']
        else:
            return True 
    else:
        return True

def isWelcome(chat_id) -> bool:
    GetWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    if (
        GetWelcomeData == None
        or not (
            'welcome_message' in GetWelcomeData
            and 'text' in GetWelcomeData['welcome_message']
        )
    ):
        return False    
    else:
        return True

def SetGoodBye(chat_id, Content, Text, DataType):
    
    WelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    WelcomeDataCount = welcome.count_documents({})
    WelcomeIDs = WelcomeDataCount + 1

    if WelcomeData == None:
        WelcomeSetData = {
            '_id': WelcomeIDs,
            'welcome': True,
            'chat_id': chat_id,
            'goodbye_message': {
                'content': Content,
                'text': Text,
                'data_type': DataType,
            },
            'clean_service': False
        }

        welcome.insert_one(
            WelcomeSetData
        )

    else:
        welcome.update_one(
            {
                'chat_id': chat_id
            },
            {
                "$set": {
                    'goodbye_message.content': Content,
                    'goodbye_message.text': Text,
                    'goodbye_message.data_type': DataType
                }
            }
        )

def UnSetGoodbye(chat_id):
    WelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    if not WelcomeData == None:
        if 'text' in WelcomeData['goodbye_message']:
            welcome.update_one(
                {
                    'chat_id': chat_id
                },
                {
                    "$unset":{
                        'goodbye_message.content': None,
                        'goodbye_message.text': None,
                        'goodbye_message.data_type': None
                    }
                }
            )

def GetGoobye(chat_id):

    GetWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    if not (
        GetWelcomeData == None
    ):
        if 'text' in GetWelcomeData['goodbye_message']:
            Content = GetWelcomeData['goodbye_message']['content']
            Text = GetWelcomeData['goodbye_message']['text']
            DataType = GetWelcomeData['goodbye_message']['data_type']
            return (
                Content,
                Text,
                DataType
            )


def SetGoodbyeMessageOnOff(chat_id, goodbye_message):
    
    welcome.update_one(
            {
                'chat_id': chat_id
            },
            {
                "$set": {
                    'goodbye': goodbye_message
                    }
            }
        )

def GetGoodbyemessageOnOff(chat_id) -> bool:
    GetWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    if not GetWelcomeData == None:
        if 'goodbye' in GetWelcomeData:
            return GetWelcomeData['goodbye']
        else:
            return True 
    else:
        return True


def isGoodbye(chat_id) -> bool:
    GetWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    if (
        GetWelcomeData == None
        or not (
            'goodbye_message' in GetWelcomeData
            and 'text' in GetWelcomeData['goodbye_message']
        )
    ):
        return False    
    else:
        return True

def SetCleanService(chat_id, clean_service):
    
    WelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    
    WelcomeDataCount = welcome.count_documents({})
    WelcomeIDs = WelcomeDataCount + 1

    if not (
        WelcomeData == None
    ):
        welcome.update_one(
                {
                    'chat_id': chat_id
                },
                {
                    "$set": {
                        'clean_service': clean_service
                        }
                },
                upsert=True
            )
    else:
        welcome.insert_one(
            {   '_id': WelcomeIDs,
                'chat_id': chat_id,
                'clean_service': clean_service
            }
        )

def GetCleanService(chat_id) -> bool:
    GetWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    if not GetWelcomeData == None:
        if 'clean_service' in GetWelcomeData:
            return GetWelcomeData['clean_service']
        else:
            return False
    else:
        return False

def SetCleanWelcome(chat_id, clean_welcome):
    WelcomeDataCount = welcome.count_documents({})
    WelcomeIDs = WelcomeDataCount + 1

    GetWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    if not GetWelcomeData == None:
        welcome.update_one(
                {
                    'chat_id': chat_id
                },
                {
                    "$set": {
                        'clean_welcome': clean_welcome,
                        'clean_welcome_message': None
                        }
                },
                upsert=True
            )
    else:
        welcome.insert_one(
            {   '_id': WelcomeIDs,
                'chat_id': chat_id,
                'clean_welcome': clean_welcome,
                'clean_welcome_message': None
            }
        )

def SetCleanWelcomeMessage(chat_id, message_id):
    GetWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    if not GetWelcomeData == None:
        if 'clean_welcome_message' in GetWelcomeData:
            welcome.update_one(
                {
                    'chat_id': chat_id
                },
                {
                    "$set": {
                        'clean_welcome_message': message_id
                    }
                }
            )

def GetCleanWelcome(chat_id) -> bool:
    GetWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    if not GetWelcomeData == None:
        if 'clean_welcome' in GetWelcomeData:
            return GetWelcomeData['clean_welcome']
        else:
            return True
    else:
        return True

def GetCleanWelcomeMessage(chat_id):
    GetWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    if not GetWelcomeData == None:
        if 'clean_welcome_message' in GetWelcomeData:
            clean_message = GetWelcomeData['clean_welcome_message']
            return clean_message
        else:
            return None
    return None

def SetCaptcha(chat_id, captcha):
    WelcomeDataCount = welcome.count_documents({})
    WelcomeIDs = WelcomeDataCount + 1

    GetCaptchaData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    if not GetCaptchaData == None:
        welcome.update_one(
                    {
                        'chat_id': chat_id
                    },
                    {
                        "$set": {
                            'captcha': {
                                '_captcha': captcha,
                                'captcha_mode': None,
                                'captcha_text': None,
                                'captcha_kick_time': None,
                                'users_welcomeIDs': [],
                                'verified_users': []
                            },
                            }
                    },
                    upsert=True
                )
            
    else:
        welcome.insert_one(
            {
                '_id': WelcomeIDs,
                'chat_id': chat_id,
                'captcha': {
                    '_captcha': captcha,
                    'captcha_mode': None,
                    'captcha_text': None,
                    'captcha_kick_time': None,
                    'users_welcomeIDs': [],
                    'verified_users': []
                }
            }
        )

def isGetCaptcha(chat_id) -> bool:
    GetCaptchaData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    if not GetCaptchaData == None:
        if 'captcha' in GetCaptchaData:
            return GetCaptchaData['captcha']['_captcha']
        return False
    else:
        return False

def GetCaptchaSettings(chat_id):
    GetCaptchaData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    captcha_text_de = "Click here to prove you're human" 

    if not GetCaptchaData == None:
        if 'captcha' in GetCaptchaData:
            captcha_mode = GetCaptchaData['captcha']['captcha_mode']
            captcha_text = GetCaptchaData['captcha']['captcha_text']
            captcha_kick_time = GetCaptchaData['captcha']['captcha_kick_time']
            
            if captcha_text is None:
                captcha_text = captcha_text_de

            if captcha_mode is None:
                captcha_mode = 'button'
                
            return (
                captcha_mode,
                captcha_text,
                captcha_kick_time
            )
        else:
            return (
                'button',
                captcha_text_de,
                None
            )
    else:
        return (
            'button',
            captcha_text_de,
            None
        )

def SetCaptchaText(chat_id, captcha_text):
    WelcomeDataCount = welcome.count_documents({})
    WelcomeIDs = WelcomeDataCount + 1

    GetCaptchaData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    if not GetCaptchaData == None:
        if 'captcha' in GetCaptchaData:
            welcome.update_one(
                {
                    'chat_id': chat_id
                },
                {
                    "$set": {
                        "captcha.captcha_text": captcha_text
                    }
                },
                upsert=True
            )
        else:
            welcome.update_one(
                    {
                        'chat_id': chat_id
                    },
                    {
                        "$set": {
                            'captcha': {
                                '_captcha': False,
                                'captcha_mode': None,
                                'captcha_text': captcha_text,
                                'captcha_kick_time': None,
                                'users_welcomeIDs': [],
                                'verified_users': []
                            },
                            }
                    },
                    upsert=True
                )
    else:
        welcome.insert_one(
            {
                '_id': WelcomeIDs,
                'chat_id': chat_id,
                'captcha': {
                    '_captcha': False,
                    'captcha_mode': None,
                    'captcha_text': captcha_text,
                    'captcha_kick_time': None,
                    'users_welcomeIDs': [],
                    'verified_users': []
                }
            }
        )

def SetCaptchaMode(chat_id, captcha_mode):
    WelcomeDataCount = welcome.count_documents({})
    WelcomeIDs = WelcomeDataCount + 1

    GetCaptchaData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    if not GetCaptchaData == None:
        if 'captcha' in GetCaptchaData:
            welcome.update_one(
                {
                    'chat_id': chat_id
                },
                {
                    "$set": {
                        "captcha.captcha_mode": captcha_mode
                    }
                },
                upsert=True
            )
        else:
            welcome.update_one(
                    {
                        'chat_id': chat_id
                    },
                    {
                        "$set": {
                            'captcha': {
                                '_captcha': False,
                                'captcha_mode': captcha_mode,
                                'captcha_text': None,
                                'captcha_kick_time': None,
                                'users_welcomeIDs': [],
                                'verified_users': []
                            },
                            }
                    },
                    upsert=True
                )
    else:
        welcome.insert_one(
            {
                '_id': WelcomeIDs,
                'chat_id': chat_id,
                'captcha': {
                    '_captcha': False,
                    'captcha_mode': captcha_mode,
                    'captcha_text': None,
                    'captcha_kick_time': None,
                    'users_welcomeIDs': [],
                    'verified_users': []
                }
            }
        )
        
def SetUserCaptchaMessageIDs(chat_id, user_id, message_id):
    welcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    userD = welcomeData['captcha']['users_welcomeIDs']

    for user in userD:
        x = user['user_id']
        if x == user_id:
            DeleteUsercaptchaData(chat_id, user_id)

    welcome.update_one(
        {
            'chat_id': chat_id
        },
        {
            "$push": {
                'captcha.users_welcomeIDs': {
                    'user_id': user_id,
                    'message_id': message_id,
                    'chances': None,
                    'correct_captcha': None,
                    'captcha_list': []
                }
            }
        },
        upsert=True
    )

def SetCaptchaTextandChances(chat_id, user_id, captcha_text, chances, captcha_list):
    welcome.update(
        {
            'chat_id': chat_id,
            'captcha.users_welcomeIDs.user_id' : user_id 
        },
        {
            "$set": {
                'captcha.users_welcomeIDs.$.correct_captcha': captcha_text,
                'captcha.users_welcomeIDs.$.chances': chances,
                'captcha.users_welcomeIDs.$.captcha_list': captcha_list
                }
        },
        upsert=True
    )

def CaptchaChanceUpdater(chat_id, user_id, chances):
    welcome.update(
        {
            'chat_id': chat_id,
            'captcha.users_welcomeIDs.user_id' : user_id 
        },
        {
            "$set": {
                'captcha.users_welcomeIDs.$.chances': chances
                }
        },
        False,
        True
    )

def GetChance(chat_id, user_id):
    GetCaptchaData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    users_welcomeIDs = GetCaptchaData['captcha']['users_welcomeIDs']
    for user in users_welcomeIDs:
        userID = user['user_id']
        chances = user['chances']

        if userID == user_id:
            return chances

def GetUserCaptchaMessageIDs(chat_id: int, user_id: int):
    GetCaptchaData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    users_welcomeIDs = GetCaptchaData['captcha']['users_welcomeIDs']
    for user in users_welcomeIDs:
        userIDs = user['user_id']

    for user in users_welcomeIDs:
        userIDs = user['user_id']
        message_id = user['message_id']
        correct_captcha = user['correct_captcha']
        chances = user['chances']
        captcha_list = user['captcha_list']

        if userIDs == user_id:
            return (
                message_id,
                correct_captcha,
                chances,
                captcha_list
            )
        
def DeleteUsercaptchaData(chat_id, user_id):
    welcome.update(
        {
            'chat_id': chat_id,
            'captcha.users_welcomeIDs.user_id' : user_id 
        },
        {
            "$pull": {
                'captcha.users_welcomeIDs': {
                    'user_id': user_id
                }
            }
        }
    )

def AppendVerifiedUsers(chat_id, user_id):
    GetVData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    verifiedList = GetVData['captcha']['verified_users']

    if user_id in verifiedList:
        return

    welcome.update_one(
        {
            'chat_id': chat_id
        },
        {
            "$push": {
                'captcha.verified_users': user_id
                }
        }
    )

def isUserVerified(chat_id, user_id) -> bool:
    GetData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    if user_id in GetData['captcha']['verified_users']:
        return True 
    else:
        return False

def setReCaptcha(chat_id: int, reCaptcha: bool):
    getWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    
    if getWelcomeData is None:
        _id = welcome.count_documents({}) + 1
        welcome.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'reCaptcha': reCaptcha
            }
        )
    else:
        welcome.update(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'reCaptcha': reCaptcha
                }
            },
            upsert=True
        )

def isReCaptcha(chat_id: int) -> bool:
    getWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    if (
        getWelcomeData is not None
        and 'reCaptcha' in getWelcomeData
    ):
        return getWelcomeData['reCaptcha']
    else:
        return False
    
def setRuleCaptcha(chat_id: int, rule_captcha: bool):
    getWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )
    
    if getWelcomeData is None:
        _id = welcome.count_documents({}) + 1
        welcome.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'rule_captcha': rule_captcha
            }
        )
    else:
        welcome.update(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'rule_captcha': rule_captcha
                }
            },
            upsert=True
        )

def isRuleCaptcha(chat_id: int) -> bool:
    getWelcomeData = welcome.find_one(
        {
            'chat_id': chat_id
        }
    )

    if (
        getWelcomeData is not None
        and 'rule_captcha' in getWelcomeData
    ):
        return getWelcomeData['rule_captcha']
    else:
        return False