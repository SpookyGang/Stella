from pyrogram import filters
from Stella import StellaCli 

from Stella.plugins.users.logging import logger
from Stella.plugins.federation.checker import fed_checker
from Stella.plugins.blocklists.blocklist_message_checker import blocklist_checker

@StellaCli.on_message(filters.all & filters.group, group=-1)
async def NewMessageHandler(client, message):
    
    # New users and chat logger 
    await logger(message)

    # fed ban user checker 
    await fed_checker(message)

    # Blocklist message checker 
    await blocklist_checker(message)