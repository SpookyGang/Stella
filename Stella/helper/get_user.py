from Stella import StellaCli

async def get_user_id(message):
    if(
        message.reply_to_message
        and not message.forward_from
    ):
        if (
            len(message.command) >= 2
        ):
            user = message.command[1]
            user_info = await StellaCli.get_users(
                user_ids=user
            )
            return user_info
        else:
            user_info = message.reply_to_message.from_user
            return user_info 

    elif (
        message.forward_from
    ):
        user_info = message.forward_from
        return user_info 

    elif not (
        message.reply_to_message
        or message.forward_from
    ):
        if (
            len(message.command) == 1
        ):
            user_info = message.from_user
            return user_info

        if not (
            len(message.command) >= 2
        ):
            await message.reply(
                "I don't know who you're talking about, you're going to need to specify a user...!"
            )
            return False
            
        user = message.command[1]
        user_info = await StellaCli.get_users(
            user_ids=user
        )
        
        return user_info  

def get_text(message):
    if( 
        message.reply_to_message
    ):
        text = ' '.join(message.command[1:])
    
    elif (
        not message.reply_to_message
    ):
        text = ' '.join(message.command[2:])
    
    return text