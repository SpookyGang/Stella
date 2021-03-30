from Stella.helper.convert import convert_time

async def get_time(message):
    if(
        message.reply_to_message
    ):
        if not (
            len(message.command) >= 2
        ):
            await message.reply(
                "You haven't specified a time to mute this user for!"
            )
            return

        args = message.command[1]
        if await check_time(message, args):
            return args
        
    elif not (
        message.reply_to_message
    ):
        if not len(message.command) >= 3:
            await message.reply(
                "You haven't specified a time to mute this user for!"
            )
            return

        args = message.command[2]
        if await check_time(message, args):
            return args
            

async def check_time(message, args) -> bool:
    if len(args) == 0:
        await message.reply(
            f"failed to get specified time: You didn't provide me time"
        )
        return
        
    if (
        len(args) == 1
    ):
        await message.reply(
            (
                f"failed to get specified time: '{args[-1]}' does not follow the expected time patterns.\n"
                "Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks."
            )
        )
        return False

    elif len(args) > 1:
        if not args[-2].isdigit():
            await message.reply(
                f"failed to get specified time: '{args[-2]}' is not a valid number"
            )
            return False

        elif args[-1] in ['w', 'd', 'h', 'm']:
            check_time_limit = convert_time(int(args[:-1]), args[-1])
            if check_time_limit >= 31622400: #  31622400 ( seconds ) is 366 days 
                await message.reply(
                    "failed to get specified time: temporary actions have to be between 1 minute and 366 days"
                )
                return False
            return True
        else:
            await message.reply(
                    f"failed to get specified time: '{args[-1]}' is not a valid time char; expected one of w/d/h/m (weeks, days, hours, minutes)"
                )
            return False

def time_string_helper(time_args):
    time_limit = int(time_args[:-1])
    if time_args[-1] == 'w':
        time_format = 'weeks'
    elif time_args[-1] == 'd':
        time_format = 'days'
    elif time_args[-1] == 'h':
        time_format = 'hours'
    elif time_args[-1] == 'm':
        time_format = 'mintues'
    return time_limit, time_format
