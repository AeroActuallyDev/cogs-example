from CogsAPI import logs, cogs
from . import start
from time import sleep


def on_close(ws, close_status_code, close_msg):
    """
    Triggers when API connection closes.
    """
    logs.process(f"Closed gateway for reason <red>{close_status_code} {close_msg}.</>")
    logs.send_console_message(f"Bot <blue>{cogs.client.user} ({cogs.client.whitelist})</><yellow> disconnected to API.")
    for x in range(1, 11):
        sleep(1)
    start.connect(cogs.client)
    
