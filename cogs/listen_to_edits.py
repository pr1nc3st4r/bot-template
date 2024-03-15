import disnake
from disnake.ext import commands
import asyncio
from sqlite3 import connect

class ListenEdits(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.db = connect("database.db")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.interaction is None:
            if (len(after.embeds) > 0):
                _embed = after.embeds[0]
                description = _embed.description
                footer = _embed.footer.text
                image = _embed.image.url
                author = _embed.author
                author_name = _embed.author.name
                colour = _embed.colour
                message_link = str(after.jump_url)
                fields = _embed.fields
                title = _embed.title
        else:
            try:
                interaction = before.interaction
                users_id = interaction.user.id
                users_name = interaction.user.name
                user_mention = interaction.user.mention
                user = before.guild.get_member_named(users_name)
                if (len(after.embeds) > 0):
                    _embed = after.embeds[0]
                    description = _embed.description
                    footer = _embed.footer.text
                    image = _embed.image.url
                    author = _embed.author
                    author_name = _embed.author.name
                    colour = _embed.colour
                    message_link = str(after.jump_url)
                    fields = _embed.fields
                    title = _embed.title
            except BaseException as err:
                return

def setup(client):
    client.add_cog(ListenEdits(client))
