from os import getenv, path, getpid
from dotenv import load_dotenv
from threading import Thread
from psutil import Process
from time import sleep
from . import request, cogs, logs

load_dotenv("/config.env")

def _limit(client, cap=500):
    """
    Start limiting memory of the selfbot, paramater 'cap' in mb.
    """
    process = Process(getpid())
    while True:
        sleep(1)
        if process.memory_info().rss /1024 ** 2 > float(cap):
            logs.send_console_message(f"Bot <blue>{client.user} ({client.whitelist})<yellow> Above memory threshold! {round(process.memory_info().rss /1024 ** 2, 2)}mb/{cap}mb. Giving it 60 seconds to reduce memory!</>")
            cogs.send_client_message(client, bot=f"Exceeded maximum memory! Giving 60 seconds to lower below the threshold of {round(process.memory_info().rss /1024 ** 2, 2)}mb/{cap}mbmb!.")
            sleep(30)
            if process.memory_info().rss /1024 ** 2 > float(cap):
                cogs.send_client_message(client, bot=f"Failed to get below the threshold ({round(process.memory_info().rss /1024 ** 2, 2)}mb/{cap}mb)! Restarting.")
                logs.send_console_message(f"Bot <blue>{client.user} ({client.whitelist})<yellow> Failed to get below memory threshold! {round(process.memory_info().rss /1024 ** 2, 2)}mb/{cap}mb. Restarting!</>")
                request.post(client, f"/{self.client.selfbot_name}/account/status/restart/")
            else:
                cogs.send_client_message(client, bot=f"Successfully below memory threshold! ({round(process.memory_info().rss /1024 ** 2, 2)}mb/{cap}mb)")
                logs.send_console_message(f"Bot <blue>{client.user} ({client.whitelist})<yellow> Successfully below memory threshold! {round(process.memory_info().rss /1024 ** 2, 2)}mb/{cap}mb.</>")       

def limit(client):
    Thread(target=lambda: _limit(client, getenv("MAX_MEM"))).start()

