from CogsAPI import status
from json import loads
import __main__ as main

def on_message(ws, message):
    """
    On API message.
    """
    client = main.client    
    data = loads(message)
    
    segments = data["event"].split(".")
    if segments[0] == "status":
        if segments[1] == "off":
            status.off(client)
    elif segments[0] == "account":
        client.account = data["message"]
    elif segments[0] == "settings":
        if segments[1] == "reload":
            client.settings = data["message"]