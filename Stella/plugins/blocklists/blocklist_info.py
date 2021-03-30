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