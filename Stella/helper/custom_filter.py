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


import re
from typing import List, Union

from pyrogram.filters import create
from pyrogram.types import Message
from Stella import BOT_USERNAME, PREFIX

# Global variables for dmins commands, connection admin commands & connection user commands 
DISABLE_COMMANDS = []
COMMANDS_LIST = []

def command_lister(commands: Union[str, List[str]], disable: bool = False) -> list:
    if isinstance(commands, str):
        if disable:
            DISABLE_COMMANDS.append(commands)

    if isinstance(commands, list):
        if disable:
            for command in commands:
                DISABLE_COMMANDS.append(command)

def commandsHelper(commands: Union[str, List[str]]) -> list:
    if isinstance(commands, str):
        username_command = f"{commands}@{BOT_USERNAME}"
        COMMANDS_LIST.append(commands)
        COMMANDS_LIST.append(username_command)

    if isinstance(commands, list):
        for command in commands:
            username_command = f"{command}@{BOT_USERNAME}"
            COMMANDS_LIST.append(command)
            COMMANDS_LIST.append(username_command)
    
    return COMMANDS_LIST


def command(
    commands: Union[str, List[str]],
    prefixes: Union[str, List[str]] = PREFIX,
    case_sensitive: bool = False,
    disable: bool = False,
    ):
    
    command_lister(commands, disable)
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
