from discord.ext import commands
import discord

class EmbedCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.command(name="embed")
    async def embed(self, ctx):
        embed = discord.Embed(title='Title', description='Desc', color=discord.Color.random())
        embed.add_field(name="Name", value="Value", inline=False)
        await ctx.send(embed=embed)