from discord.ext import commands
from os import getenv, getpid
from psutil import Process, virtual_memory, cpu_percent
from CogsAPI import request, status
from . import CogsMessager, utility

class cog(commands.Cog, description="Manage your bot."):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=[], usage=None, brief="Get latency to cogs and discord")
    async def ping(self, ctx):
        latency = round(self.client.latency*1000, 1)
        await CogsMessager.send_plain(ctx, f"Discord: {latency}ms")

    @commands.command(aliases=[], usage="<renew-whitelist>", brief="Renew your whitelist, buy a new monthly whitelist and run this command!")
    async def renew(self, ctx, *args):
        if len(args) == 0:
            return await CogsMessager.send_plain(ctx, f"You need to include a renew whitelist! Get this by buying a new monthly whitelist and use that as your renew whitelist\n{self.client.command_prefix}{ctx.command} renew-whitelist", "Error!")
        r = request.post(self.client, f"{self.client.selfbot_name}/account/renew/?whitelist={args[0]}").json()
        await CogsMessager.send_plain(ctx, r["message"])

    @commands.command(aliases=[], usage=None, brief="Turn your bot off.")
    async def restart(self, ctx):
        await CogsMessager.send_plain(ctx, "Restarting")
        await status.restart(self.client)

    @commands.command(aliases=[], usage=None, brief="Turn your bot off.")
    async def off(self, ctx):
        await CogsMessager.send_plain(ctx, "Bot turning off!")
        status.off(self.client)

    @commands.command(aliases=[], usage=None, brief="Get bot server information.")
    async def node(self, ctx):
        identifier = getenv("SERVER_IDENTIFIER")
        process = Process(getpid())
        memory = virtual_memory()       
        with open("/sys/fs/cgroup/memory/memory.limit_in_bytes") as file:
            max_mem = int(file.read())
            max_mem_mb = utility.convert_size(max_mem)
        await CogsMessager.send_plain(ctx, f"Identifier: {identifier}\nAllocated RAM usage: {round(process.memory_info().rss /1024 ** 2,2)}mb/{max_mem_mb} ({round(100*(process.memory_info().rss/max_mem), 2)}%)\nTotal RAM usage: {round((memory.used // 1024 ** 2)/1024, 2)}gb/{round((memory.total // 1024 ** 2)/1024, 2)}gb ({memory.percent}%)\nCPU usage: {cpu_percent()}%\n")
        
        
def setup(client):
    client.add_cog(cog(client))