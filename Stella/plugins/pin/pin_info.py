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