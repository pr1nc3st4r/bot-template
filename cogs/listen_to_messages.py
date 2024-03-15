import disnake
from disnake.ext import commands
import asyncio
from sqlite3 import connect

class Listen(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.db = connect("database.db")

    #commands
    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        # Check if message is a normal text command
        if message.interaction is None:
            try:
                if message.author.bot:
                    return
                if (len(message.embeds) > 0):
                    _embed = message.embeds[0]
                    description = _embed.description
                    footer = _embed.footer.text
                    image = _embed.image.url
                    author = _embed.author
                    author_name = _embed.author.name
                    colour = _embed.colour
                    message_link = str(message.jump_url)
                    fields = _embed.fields
                    title = _embed.title

            except asyncio.TimeoutError:
                return
        else:
            # If not normal text command, then it's a slash command.  This is all picked up here
            try:
                interaction = message.interaction
                users_id = interaction.user.id
                users_name = interaction.user.name
                user_display_name = interaction.user.display_name
                user_mention = interaction.user.mention
                user = interaction.user
                com_name = interaction.name

                if (len(message.embeds) > 0):
                    _embed = message.embeds[0]
                    footer = _embed.footer.text
                    title = _embed.title
                    description = _embed.description
                    image = _embed.image.url
                    author = _embed.author
                    author_name = _embed.author.name
                    colour = _embed.colour
                    message_link = str(message.jump_url)
                    fields = _embed.fields

            except BaseException as err:
                return


def setup(client):
    client.add_cog(Listen(client))
