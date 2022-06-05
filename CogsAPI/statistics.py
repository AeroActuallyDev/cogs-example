from json import dumps
from psutil import Process
from os import getpid, getenv
from threading import Thread
from . import cogs, utility
from datetime import datetime
from time import sleep

def loop_message():
    while True:
        process = Process(getpid())
        try:
            cogs.client.cogs_ws.send(dumps({"event": "bot.information", "payload": {"memory": round(process.memory_info().rss /1024 ** 2,2), "percentage": round(100*(process.memory_info().rss/(int(getenv('MAX_MEM'))*1000000)), 2), "pid": getpid(), "discordid": cogs.client.user.id, "start_time": cogs.client.start_time.strftime('%Y-%m-%dT%H:%M:%SZ'), "total_seconds": utility.s_between(datetime.now(), cogs.client.start_time)}}))
        except:
            pass
        sleep(60)
    
def start_loop():
    Thread(target=loop_message).start()