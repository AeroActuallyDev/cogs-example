from os import getenv
from . import on_close, on_message, on_open
import websocket

websocket.enableTrace(False)

def connect(client):
    """
    Connects to the CogsAPI server and registers the bot to the whitelist.
    """
    ws = websocket.WebSocketApp(f"{getenv('WEBSOCKET_SCHEME')}://{getenv('MASTER_SERVER')}/{client.selfbot_name}/gateway/register/bot/",
                              on_open=on_open.on_open,
                              on_message=on_message.on_message,
                              on_close=on_close.on_close,
                              header={"Authorization": client.whitelist, "server": getenv("SERVER_IDENTIFIER")})
    client.cogs_ws = ws
    ws.run_forever()

    
