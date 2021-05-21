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


__mod_name__ = "Filters"

__help__ = (
    "Make your chat more lively with filters; The bot will reply to certain words!\n\n"
    "Filters are case insensitive; every time someone says your trigger words, Rose will reply something else! can be used to create your own commands, if desired.\n\n"
    "**Commands**:\n"
    "- /filter `<trigger> <reply>`: Every time someone says \"trigger\", the bot will reply with \"sentence\". For multiple word filters, quote the trigger.\n"
    "- /filters: List all chat filters.\n"
    "- /stop `<trigger>`: Stop the bot from replying to \"trigger\"."
    "- /stopall: Stop **ALL** filters in the current chat. This cannot be undone.\n\n"
    "**Examples**:\n"
    "- Set a filter:\n"
    "-> `/filter hello Hello there! How are you?`\n"
    "- Set a multiword filter:\n"
    "-> `/filter \"hello friend\" Hello back! Long time no see!`\n"
    "- Set a filter that can only be used by admins:\n"
    "-> `/filter \"example\" This filter wont happen if a normal user says it {admin}`\n"
    "- To save a file, image, gif, or any other attachment, simply reply to file with:\n"
    "-> `/filter trigger`\n"
)