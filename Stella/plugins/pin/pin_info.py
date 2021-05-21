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

__mod_name__ = "Pin"

__help__ = (
    "All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!\n\n"
    "**User commands:**\n"
    "- /pinned: Get the current pinned message.\n\n"
    "**Admin commands:**\n"
    "- /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.\n"
    "- /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.\n"
    "- /unpinall: Unpins all pinned messages.\n"
    "- /antichannelpin `<yes/no/on/off>`: Don't let telegram auto-pin linked channels. If no arguments are given, shows current setting.\n"
    "- /cleanlinked `<yes/no/on/off>`: Delete messages sent by the linked channel.\n\n"
    "Note: `/antichannelpin` and `/cleanlinked` can't be enabled at the same time because there's no point in doing so.\n"
    "As `/cleanlinked` automatically deletes messages sent by the linked channel and it's removed from the pin."
)