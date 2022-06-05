from CogsAPI import status, cogs, logs
from json import loads

def on_message(ws, message):
    """
    On API message.
    """
    logs.process("Recieved message from gateway.")
    client = cogs.client
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