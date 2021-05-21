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


__mod_name__ = "Bans"

__help__ = (
    "Some people need to be publicly banned; spammers, annoyances, or just trolls.\n\n"
    "This module allows you to do that easily, by exposing some common actions, so everyone will see!\n\n"
    "**User commands::**\n"
    "- /kickme: Users that use this, kick themselves.\n\n"
    "Admin commands:\n"
    "- /ban: Ban a user.\n"
    "- /dban: Ban a user by reply, and delete their message.\n"
    "- /sban: Silently ban a user, and delete your message.\n"
    "- /tban: Temporarily ban a user.\n"
    "- /unban: Unban a user.\n"
    "- /mute: Mute a user.\n"
    "- /dmute: Mute a user by reply, and delete their message.\n"
    "- /smute: Silently mute a user, and delete your message.\n"
    "- /tmute: Temporarily mute a user.\n"
    "- /unmute: Unmute a user.\n"
    "- /kick: Kick a user.\n"
    "- /dkick: Kick a user by reply, and delete their message.\n"
    "- /skick: Silently kick a user, and delete your message\n\n"
    "**Examples:**\n"
    "- Mute a user for two hours.\n"
    "-> `/tmute @username 2h`"
)