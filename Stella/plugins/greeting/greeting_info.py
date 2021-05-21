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


__mod_name__ = "Greetings"

__help__ = """
Give your members a warm welcome with the greetings module! Or a sad goodbye... Depends!

Admin commands:
- /welcome `<yes/no/on/off>`: Enable/disable welcomes messages.
- /goodbye `<yes/no/on/off>`: Enable/disable goodbye messages.
- /setwelcome `<text>`: Set a new welcome message. Supports markdown, buttons, and fillings.
- /resetwelcome: Reset the welcome message.
- /setgoodbye `<text>`: Set a new goodbye message. Supports markdown, buttons, and fillings.
- /resetgoodbye: Reset the goodbye message.
- /cleanservice `<yes/no/on/off>`: Delete all service messages. Those are the annoying 'x joined the group' notifications you see when people join.
- /cleanwelcome `<yes/no/on/off>`: Delete old welcome messages. When a new person joins, or after 5 minutes, the previous message will get deleted.

Examples:
- Get the welcome message without any formatting
-> `/welcome noformat`
"""