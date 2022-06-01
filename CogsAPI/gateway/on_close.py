from CogsAPI import logs
from . import start
from time import sleep
import __main__ as main

def on_close(ws, close_status_code, close_msg):
    """
    Triggers when API connection closes.
    """
    logs.send_console_message(f"Bot <blue>{main.client.user} ({main.client.whitelist})</><yellow> disconnected to API.")
    for x in range(1, 11):
        sleep(1)
    start.connect(main.client)
