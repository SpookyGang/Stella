from typing import List , Union
import re 

from pyrogram.filters  import create
from pyrogram.types import Message

from Stella import PREFIX, BOT_USERNAME

# Global variables for dmins commands, connection admin commands & connection user commands 
ADMIN_COMMANDS = []
CONNECTIONS_ADMIN_COMMANDS = []
CONNECTION_USER_COMMANDS = []

def command_lister(commands, admin, connection_admin, connection_user) -> list:
    if isinstance(commands, str):
        if admin:
            ADMIN_COMMANDS.append(commands) 
        if connection_admin:
            CONNECTIONS_ADMIN_COMMANDS.append(commands)
        if connection_user:
            CONNECTION_USER_COMMANDS.append(commands)

    if isinstance(commands, list):
        if admin:
            ADMIN_COMMANDS.append(commands[0])
        if connection_admin:
            CONNECTIONS_ADMIN_COMMANDS.append(commands)
        if connection_user:
            CONNECTION_USER_COMMANDS.append(commands)
    


def commandsHelper(commands: Union[str, List[str]]) -> list:
    commands_list = []
    if isinstance(commands, str):
        username_command = f"{commands}@{BOT_USERNAME}"
        commands_list.append(commands)
        commands_list.append(username_command)

    if isinstance(commands, list):
        for command in commands:
            username_command = f"{command}@{BOT_USERNAME}"
            commands_list.append(command)
            commands_list.append(username_command)
    
    return commands_list


def command(
    commands: Union[str, List[str]],
    prefixes=PREFIX,
    case_sensitive: bool = False,
    admin: bool = False,
    connection_admin: bool = False,
    connection_user: bool = False
    ):
    
    command_lister(commands, admin, connection_admin, connection_user)
    commands = commandsHelper(commands)
    
    command_re = re.compile(r"([\"'])(.*?)(?<!\\)\1|(\S+)")
    async def func(flt, _, message: Message):
        text = message.text or message.caption
        message.command = None

        if not text:
            return False

        pattern = r"^{}(?:\s|$)" if flt.case_sensitive else r"(?i)^{}(?:\s|$)"

        for prefix in flt.prefixes:
            if not text.startswith(prefix):
                continue

            without_prefix = text[len(prefix):]

            for cmd in flt.commands:
                if not re.match(pattern.format(re.escape(cmd)), without_prefix):
                    continue

                # match.groups are 1-indexed, group(1) is the quote, group(2) is the text
                # between the quotes, group(3) is unquoted, whitespace-split text

                # Remove the escape character from the arguments
                message.command = [cmd] + [
                    re.sub(r"\\([\"'])", r"\1", m.group(2) or m.group(3) or "")
                    for m in command_re.finditer(without_prefix[len(cmd):])
                ]

                return True

        return False

    commands = commands if isinstance(commands, list) else [commands]
    commands = {c if case_sensitive else c.lower() for c in commands}

    prefixes = [] if prefixes is None else prefixes
    prefixes = prefixes if isinstance(prefixes, list) else [prefixes]
    prefixes = set(prefixes) if prefixes else {""}

    return create(
        func,
        "CommandFilter",
        commands=commands,
        prefixes=prefixes,
        case_sensitive=case_sensitive
    )
