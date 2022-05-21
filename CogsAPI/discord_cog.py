from discord.ext import commands
from dotenv import load_dotenv
from os import getenv, path, getpid
from psutil import Process, virtual_memory, cpu_percent
from CogsAPI import request, status

load_dotenv("/config.env")

class cog(commands.Cog, description="Manage your bot."):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=[], usage="<renew-whitelist>", brief="Renew your whitelist, buy a new monthly whitelist and run this command!")
    async def renew(self, ctx, *args):
        if len(args) == 0:
            return await ctx.send(f"You need to include a renew whitelist! Get this by buying a new monthly whitelist and use that as your renew whitelist\n\n{self.client.command_prefix}{ctx.command} renew-whitelist") 
        r = request.post(self.client, f"{self.client.selfbot_name}/account/renew/?whitelist={args[0]}").json()
        await ctx.cogs_send(r["message"])

    @commands.command(aliases=[], usage=None, brief="Turn your bot off.")
    async def restart(self, ctx):
        await ctx.send("Restarting!")
        await status.restart(self.client)

    @commands.command(aliases=[], usage=None, brief="Turn your bot off.")
    async def off(self, ctx):
        await ctx.send("Bot turning off!")
        status.off(self.client)

    @commands.command(aliases=[], usage=None, brief="Get bot server information.")
    async def node(self, ctx):
        identifier = getenv("SERVER_IDENTIFIER")
        process = Process(getpid())
        memory = virtual_memory()
        await ctx.send(f"Identifier: {identifier}\nAllocated RAM usage: {round(process.memory_info().rss /1024 ** 2,2)}mb/{getenv('MAX_MEM')}mb ({round(100*(process.memory_info().rss/(int(getenv('MAX_MEM'))*1000000)), 2)}%)\nTotal RAM usage: {round((memory.used // 1024 ** 2)/1024, 2)}gb/{round((memory.total // 1024 ** 2)/1024, 2)}gb ({memory.percent}%)\nCPU usage: {cpu_percent()}%\n")
        
        
def setup(client):
    client.add_cog(cog(client))