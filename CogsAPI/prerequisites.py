from . import settings
from os import path, getenv

def define(client):
    client.version = getenv("VERSION")
    client.branch = getenv("BRANCH")
    client.selfbot_name = getenv("SELFBOT")

    client.cogs_ws = None

    client.account = settings.fetch_account(client)
    client.settings = settings.fetch_settings(client)

    client.token = client.settings["bot"]["token"]