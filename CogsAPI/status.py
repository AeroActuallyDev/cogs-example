from os import _exit, system
from . import logs, cogs

def off(client):
    cogs.send_client_message(client, bot="Bot turning off!")
    logs.send_console_message(f"Bot <blue>{client.user} ({client.whitelist})</><yellow> turning off.")
    client.cogs_ws.close()
    _exit(1)

async def restart(client):
    cogs.send_client_message(client, bot="Bot restarting!")
    logs.send_console_message(f"Bot <blue>{client.user} ({client.whitelist})</><yellow> restarting.")
    client.cogs_ws.close()
    system(f"sudo shutdown -r now")