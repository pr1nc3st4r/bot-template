import disnake
from disnake.ext import commands
from disnake import Option, OptionChoice, OptionType, ApplicationCommandInteraction
import asyncio
from sqlite3 import connect

class Commands_Cog(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.db = connect("database.db")

    #commands
    @commands.slash_command(
        name="profile",
        description="See your profile")
    async def profile(self, ctx):
        # Put your command code here
        return

def setup(client):
    client.add_cog(Commands_Cog(client))