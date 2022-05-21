from . import settings
from os import path

def define(client):
    client.selfbot = "/".join(path.dirname(path.abspath(__file__)).replace("\\", "/").split("/")[0:-1]) #Path of selfbot
    client.version = client.selfbot.split("/")[len(client.selfbot.split("/"))-2]+"."+client.selfbot.split("/")[len(client.selfbot.split("/"))-2] #Eg name.version
    client.selfbot_name = client.version.split(".")[0] #Name of selfbot.

    client.account = settings.fetch_account(client)
    client.settings = settings.fetch_settings(client)

    client.token = client.settings["bot"]["token"]