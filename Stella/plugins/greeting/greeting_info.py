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