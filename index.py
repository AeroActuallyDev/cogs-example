from CogsAPI import cogs, logs, prerequisites
from discord.ext import commands
from os import getenv

client = commands.Bot(command_prefix="!", self_bot=True)

client.whitelist = getenv("WHITELIST")
prerequisites.define(client)

@client.event
async def on_ready():
    logs.send_console_message(f"Bot <blue>{client.user} ({client.whitelist})</><yellow> connected to Discord.")
    cogs.init(client)

#Example/optional cog to add to your bot.
client.load_extension(f'CogsAPI.discord_cog')

client.run(client.token, bot=False)