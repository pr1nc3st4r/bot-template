import sqlite3
import disnake
from disnake.ext import commands
from disnake.ext.commands import CommandInvokeError
from sqlite3 import connect
import os

intents = disnake.Intents.all()

def __init__(self, client):
    self.client = client
    self.db = connect("database.db")

Database = connect("database.db")
Cursor = Database.cursor()

client = disnake.Client()
bot_prefix = ["BOT PREFIX FOR NON-SLASH COMMANDS"]

test_guild = [SERVER_ID1, SERVER_ID2]
intents = disnake.Intents.all()
intents.members = True
intents.presences = True
intents.message_content = True
intents.guilds = True
intents.reactions = True

client = commands.AutoShardedBot(intents = intents, command_prefix = bot_prefix, case_insensitive = True, test_guilds = test_guild, reload = True, sync_commands_debug=False, help_command=None, activity = disnake.Activity(type=disnake.ActivityType.watching, name="I'm online!"))

class database:
    def field(command, *values):
        Cursor.execute(command, tuple(values))
        fetch = Cursor.fetchone()
        if fetch is not None:
            return fetch[0]
        return
    
    def one_record(command, *values):
        Cursor.execute(command, tuple(values))
        return Cursor.fetchone()

    def records(command, *values):
        Cursor.execute(command, tuple(values))
        return Cursor.fetchall()
    
    def column(command, *values):
        Cursor.execute(command, tuple(values))
        return [item[0] for item in Cursor.fetchall()]
    
    def execute(command, *values):
        Cursor.execute(command, tuple(values))
        return
    
    def commit():
        Database.commit()
        return

    def disconnect():
        Database.close()
        return

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandInvokeError):
        return

@client.event
async def on_ready():
    print(f'We have logged in {client.user}! ID: {client.user.id}')
    print("------")
    print("Startup tasks completed.")

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

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

f = open("key.txt", "r")
token = f.read()

# run the bot
client.loop.run_until_complete(client.start(token))