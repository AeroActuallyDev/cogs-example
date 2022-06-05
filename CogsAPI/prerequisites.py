from . import settings, utility
from os import environ, getenv, path

def define(client):
    client.version = getenv("VERSION")
    client.branch = getenv("BRANCH")
    client.selfbot_name = getenv("SELFBOT")

    client.cogs_ws = None

    client.account = settings.fetch_account(client)
    client.settings = settings.fetch_settings(client)

    client.token = client.settings["bot"]["token"]

    if path.exists("/sys/fs/cgroup/memory/memory.limit_in_bytes"):
        with open("/sys/fs/cgroup/memory/memory.limit_in_bytes") as file:
            environ["MAX_MEM"] = str(utility.convert_size_mb(int(file.read())))
    elif str(getenv("MAX_MEM")).upper() == "NONE":
        environ["MAX_MEM"] = "1000"