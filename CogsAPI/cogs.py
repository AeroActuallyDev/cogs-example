from CogsAPI.gateway import start
from threading import Thread
from . import request

global client
client = None

def init(DiscordClient):
    """
    Connect to the websocket for CogsAPI, allows users to turn off the bot.
    """
    global client
    client = DiscordClient
    Thread(target=lambda: start.connect(DiscordClient)).start()

def send_client_message(client, server:str=None, bot:str=None, message=None):
    """
    This sends messages to the webbrowser of the client. Eg... 'Token invalid' etc etc.

    Use:
    ServerConsole to send a message regarding the server (server crash),
    Botconsole for messages regarding the bot (token errors),

    """
    if message is None:
        message = {"ServerConsole": server, "BotConsole": bot}
    request.post(client=client, url=f"/{client.selfbot_name}/gateway/update/", json=message)