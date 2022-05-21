from os import _exit, system, getenv
from . import logs, cogs
from threading import Thread
from asyncio import sleep
from dotenv import load_dotenv

load_dotenv("config.env")

def off(client):
    cogs.send_client_message(client, bot="Bot turning off!")
    logs.send_console_message(f"Bot <blue>{client.user} ({client.whitelist})</><yellow> turning off.")
    _exit(1)

def start(client):
    system(f"{getenv('PYTHON')} {client.selfbot}/index.py {client.whitelist}")

async def restart(client):
    Thread(target=lambda: start(client)).start()
    await sleep(0.5)
    off(client)