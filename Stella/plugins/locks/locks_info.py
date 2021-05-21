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

__mod_name__ = "Locks"

__help__ = (
    "Do stickers annoy you? or want to avoid people sharing links? or pictures? You're in the right place!\n\n"
    "The locks module allows you to lock away some common items in the telegram world; the bot will automatically delete them!\n\n"
    "**Admin commands**:\n"
    "- /lock `<item(s)>`: Lock one or more items. Now, only admins can use this type!\n"
    "- /unlock `<item(s)>`: Unlock one or more items. Everyone can use this type again!\n"
    "- /locks: List currently locked items.\n"
    "- /lockwarns `<yes/no/on/off>`: Enabled or disable whether a user should be warned when using a locked item.\n"
    "- /locktypes: Show the list of all lockable items.\n"
    "- /allowlist `<url/id/@channelname(s)>`: Allowlist a URL, group ID, channel @, or bot @ to stop them being deleted by URL, forward, invitelink, and inline locks. Separate with a space to add multiple items at once. If no arguments are given, returns the current allowlist.\n"
    "- /rmallowlist `<url/id/@channelname(s)>`: Remove an item from the allowlist - url, and forward locking will now take effect on messages containing it again. Separate with a space to remove multiple items.\n"
    "- /rmallowlistall: Remove all allowisted items.\n\n"
    "**Examples**:\n"
    "- Lock stickers with:\n"
    "-> `/lock sticker`\n"
    "- You can lock/unlock multiple items by chaining them:\n"
    "-> `/lock sticker photo gif video`\n"
    "- To allow forwards from a specific channel, eg `@StellaUpdates`, you can allowlist it. You can also use the ID:\n"
    "-> `/allowlist @StellaUpdates`"
    )