from Stella.helper.custom_filter import (
    COMMANDS_LIST,
    DISABLE_COMMANDS
)

def disable(fun):

    async def wrapper(client, message):
        pass