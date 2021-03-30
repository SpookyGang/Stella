__mod_name__ = "Log Channels"

__help__ = (
    "Recent actions are nice, but they don't help you log every action taken by the bot. This is why you need log channels!\n\n"
    "Log channels can help you keep track of exactly what the other admins are doing. Bans, Mutes, warns, notes - everything can be moderated.\n\n"
    "Setting a log channel is done by the following steps:\n"
    "- Add Stella to your channel, as an admin. This is done via the \"add administrators\" tab.\n"
    "- Send /setlog to your channel.\n"
    "- Forward the /setlog command to the group you wish to be logged.\n"
    "- Congrats! all done :)\n\n"
    "**Admin commands:**\n"
    "- /logchannel: Get the name of the current log channel.\n"
    "- /setlog: Set the log channel for the current chat.\n"
    "- /unsetlog: Unset the log channel for the current chat.\n"
    "- /log `<category>`: Enable a log category - actions of that type will now be logged.\n"
    "- /nolog `<category>`: Disable a log category - actions of that type will no longer be logged.\n"
    "- `/logcategories`: List all support categories, with information on what they refer to."
)