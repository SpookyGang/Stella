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


from Stella import StellaCli

async def get_user_id(message):
    if(
        message.reply_to_message
        and not message.forward_from
    ):
        if (
            len(message.command) >= 2
        ):
            args = message.command[1]
            if (
                args.startswith('@')
                or (
                    args.isdigit()
                    and (
                        len(args) >= 5
                        or len(args) <=15
                    )
                )
            ):
                user_info = await StellaCli.get_users(
                    user_ids=args
                )
                return user_info
            else:
                user_info = message.reply_to_message.from_user
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
        if (
            len(message.command) >= 2
            and (
                message.command[1].startswith('@')
                or (
                        message.command[1].isdigit()
                        and (
                            len(message.command[1]) >= 5
                            or len(message.command[1]) <=15
                        )
                )
            )
        ):
            text = ' '.join(message.command[2:])
        else:
            text = ' '.join(message.command[1:])
    
    elif (
        not message.reply_to_message
    ):
        text = ' '.join(message.command[2:])
    
    return text