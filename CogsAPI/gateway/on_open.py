from CogsAPI import logs
import __main__ as main

def on_open(ws):
    """
    Triggers when API connection starts.
    """
    logs.send_console_message(f"Bot <blue>{main.client.user} ({main.client.whitelist})</><yellow> connected to API.")