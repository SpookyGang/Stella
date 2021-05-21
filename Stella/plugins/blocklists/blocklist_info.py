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


__mod_name__ = "Blocklists"

__help__ = (
    "Want to stop people asking stupid questions? or ban anyone saying censored words? Blocklists is the module for you!\n\n"
    "From blocking rude words, filenames/extensions, to specific emoji, everything is possible.\n\n"
    "**Admin commands:**\n"
    "- /addblocklist `<blocklist trigger> <reason>`: Add a blocklist trigger. You can blocklist an entire sentence by putting it in \"quotes\".\n"
    "- /rmblocklist `<blocklist trigger>`: Remove a blocklist trigger.\n"
    "- /unblocklistall: Remove all blocklist triggers - chat creator only.\n"
    "- /blocklist: List all blocklisted items.\n"
    "- /blocklistmode `<blocklist mode>`: Set the desired action to take when someone says a blocklisted item. Available: nothing/ban/mute/kick/warn/tban/tmute.\n"
    "- /blocklistdelete `<yes/no/on/off>`: Set whether blocklisted messages should be deleted. Default: (on)\n"
    "- /setblocklistreason `<reason>`: Set the default blocklist reason to warn people with.\n"
    "- /resetblocklistreason: Reset the default blocklist reason to default - nothing.\n\n"
    "Top tip:\n"
    "Blocklists allow you to use some modifiers to match \"unknown\" characters. For example, You could use the `*` modifier, which matches any number of any character. If you want to blocklist urls, this will allow you to match the full thing. It matches every character except spaces. This is cool if you want to block, for example, url shorteners."
)