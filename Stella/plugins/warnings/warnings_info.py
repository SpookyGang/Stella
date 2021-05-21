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

__mod_name__ = "Warnings"

__help__ = (
    "Keep your members in check with warnings; stop them getting out of control!\n\n"
    "If you're looking for automated warnings, go read about the blacklist module.\n\n"
    "**Admin commands:**\n"
    "- /warn `<reason>`: Warn a user.\n"
    "- /dwarn `<reason>`: Warn a user by reply, and delete their message.\n"
    "- /swarn `<reason>:` Silently warn a user, and delete your message.\n"
    "- /warns: See a user's warnings.\n"
    "- /rmwarn: Remove a user's latest warning.\n"
    "- /resetwarn: Reset all of a user's warnings to 0.\n"
    "- /resetallwarns: Delete all the warnings in a chat. All users return to 0 warns.\n"
    "- /warnings: Get the chat's warning settings.\n"
    "- /setwarnmode `<ban/kick/mute/tban/tmute>`: Set the chat's warn mode.\n"
    "- /setwarnlimit `<number>`: Set the number of warnings before users are punished.\n\n"
    "**Examples:**\n"
    "- Warn a user.\n"
    "-> `/warn @user For disobeying the rules`"
)