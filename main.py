from dotenv import load_dotenv
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import websockets

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='+', description='description', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="info")
async def embed(ctx):
    embed = discord.Embed(title='ASM - Systems', description='Advanced Server Monitoring', color=discord.Color.from_rgb(0, 77, 255))
    embed.add_field(name="👤 Made by", value="00Gaddy", inline=False)
    embed.add_field(name="💾 Number of commands", value=f"{len(bot.commands)}", inline=False)
    embed.add_field(name="🌎 Number of joined servers", value=f"{len(bot.guilds)}", inline=False)

    await ctx.send(embed=embed)

@bot.command("websocket")
async def websocket(ctx):
    embed = discord.Embed(title='ASM - Systems', description='Advanced Server Monitoring', color=discord.Color.from_rgb(0, 77, 255))
    embed.add_field(name="Websocket Connection", value="§Websocket_Activity_Placeholder", inline=False)
    embed.add_field(name="Uptime of the Websocket Connection", value=f"§Websocket_Uptime_Placeholder", inline=False)
    embed.add_field(name="Name of the Websocket Server", value=f"§Websocket_Server_Name", inline=False)
    await ctx.send(embed=embed)



bot.run(os.getenv('TOKEN'))
