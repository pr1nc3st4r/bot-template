import sqlite3
import disnake
from disnake.ext import commands
from disnake.ext.commands import CommandInvokeError
from sqlite3 import connect
import os

def __init__(self, client):
    self.client = client
    self.db = connect("database.db")

# This allows your commands to be called by mentioning your bot, or ysing the prefix you choose
bot_prefix = commands.when_mentioned_or("PUT THE PREFIX YOU WANT IN HERE")

# If you want to use test servers, insert this into the client line instead of None
test_guild = [SERVER_ID1, SERVER_ID2]

# Depending on what you want your bot to do, you need to set the intents to allow those things
intents = disnake.Intents.all()
intents.members = True
intents.presences = True
intents.message_content = True
intents.guilds = True
intents.reactions = True

# This sets the activity of your bot when it first goes online, currently set to "watching"
activity = "PUT YOUR ACTIVITY TEXT HERE"

client = commands.AutoShardedBot(intents = intents, command_prefix = bot_prefix, case_insensitive = True, test_guilds = None, reload = True, sync_commands_debug=False, help_command=None, activity = disnake.Activity(type=disnake.ActivityType.watching, name=activity))

# This prevents you from getting an error message everytime someone calls a command that doesn't exist
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandInvokeError):
        return

# This prints a message to your console letting you know your bot has connected successfully
@client.event
async def on_ready():
    print(f'We have logged in {client.user}! ID: {client.user.id}')
    print("------")
    print("Startup tasks completed.")

# These commands let you unload/load/reload cog files. This is handy if you are running the bot locally and doing updates to your cogs.
@client.command(hidden=True)
@commands.has_guild_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Loaded')

@client.command(hidden=True)
@commands.has_guild_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Unloaded')

@client.command(hidden=True)
@commands.has_guild_permissions(administrator=True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Reloaded')

# This is how your bot loads your cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# This is how your bot looks up its key
f = open("key.txt", "r")
token = f.read()

# Run the bot
client.loop.run_until_complete(client.start(token))