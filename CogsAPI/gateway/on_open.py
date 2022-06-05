from CogsAPI import logs, cogs, statistics

def on_open(ws):
    """
    Triggers when API connection starts.
    """
    statistics.start_loop()
    logs.send_console_message(f"Bot <blue>{cogs.client.user} ({cogs.client.whitelist})</><yellow> connected to API.")