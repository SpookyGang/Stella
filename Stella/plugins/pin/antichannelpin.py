import html

from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs

from Stella.database.pin_mongo import (
    antichannelpin_db,
    get_antichannelpin,
    get_cleanlinked
)

ANTICHANNELPIN_TRUE = ['on', 'yes']
ANTICHANNELPIN_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands=('antichannelpin')))
async def antichannelpin(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title
    if not await CheckAllAdminsStuffs(message, permissions='can_pin_messages'):
        return
    
    if (
        len(message.command) >= 2
    ):
        args = message.command[1]
        if (
            args in ANTICHANNELPIN_TRUE
        ):
            CLEAN_LINKED = get_cleanlinked(chat_id)
            if not CLEAN_LINKED:
                antichannelpin_db(chat_id, True)
                await message.reply(
                    f"**Enabled** anti channel pins. Automatic pins from a channel will now be replaced with the previous pin."
                )
            else:
                await message.reply(
                    (
                        "`/antichannelpin` and `/cleanlinked` can't be enabled at the same time because there's no point in doing so.\n\n"
                        "As `/cleanlinked` automatically deletes messages sent by the linked channel and it's removed from the pin."
                    )
                )
        
        elif (
            args in ANTICHANNELPIN_FALSE
        ):
            antichannelpin_db(chat_id, False)
            await message.reply(
                f"**Disabled** anti channel pins. Automatic pins from a channel will not be removed."
            )
        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off"
            )
            
    else:
        IS_ANITICHANNEL = get_antichannelpin(chat_id)
        if IS_ANITICHANNEL:
            await message.reply(
                f"Anti channel pins are currently **enabled** in {html.escape(chat_title)}. All channel posts that get auto-pinned by telegram will be replaced with the previous pin."
            )
        
        else:
            await message.reply(
                f"Anti channel pins are currently **disabled** in {html.escape(chat_title)}."
            )