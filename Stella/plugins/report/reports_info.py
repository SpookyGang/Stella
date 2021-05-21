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

__mod_name__ = "Reports"

__help__ = (
    "We're all busy people who don't have time to monitor our groups 24/7. But how do you react if someone in your group is spamming?\n\n"
    "Presenting reports; if someone in your group thinks someone needs reporting, they now have an easy way to call all admins.\n\n"
    "**User commands:**\n"
    "- /report: Reply to a message to report it for admins to review.\n"
    "- admin: Same as /report\n\n"
    "**Admin commands:**\n"
    "- /reports `<yes/no/on/off>`: Enable/disable user reports.\n\n"
    "To report a user, simply reply to his message with @admin or /report; Stella will then reply with a message stating that admins have been notified. This message tags all the chat admins; same as if they had been @'ed.\n\n"
    "Note that the report commands do not work when admins use them; or when used to report an admin. Stella assumes that admins don't need to report, or be reported!"
)