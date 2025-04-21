from keep_alive import keep_alive
from flask import Flask
from threading import Thread
import discord
import audioop
from discord.ext import commands
import asyncio
from discord.ext.commands import has_permissions
import os

app = Flask('')

@app.route('/')

keep_alive()


client = commands.Bot(command_prefix=".", intents=discord.Intents.all())
client.remove_command("help")

# help
@client.command()
async def help(ctx):
    await ctx.channel.send("pomoc")

# clear
@client.command()
async def clear(ctx,ilosc = 5):
    await asyncio.sleep(1)
    await ctx.channel.purge(limit=ilosc + 1)
    await ctx.send("Usunięto!!")
    await asyncio.sleep(0.5)
    await ctx.channel.purge(limit=1)
    
# ban
@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason="Zostałeś zbanowany"):
    await member.ban(reason=reason)

# kick
@client.command()
@has_permissions(ban_members=True)
async def kick(ctx, member : discord.Member, reason="Zostałeś wyrzucony!"):
    await member.kick(reason=reason)


# play
@client.command()
async def play(ctx, game):
    await client.change_presence(activity=discord.Game(name=game))

token = os.getenv("MTM1NzA0NDg3Njg1MTU0NDA4NA.GWVVGc.Zl8UZFtK2X0w6RrX0J3scsXZW_m71cnA30LwDI")
client.run(tron)
client.run("MTM1NzA0NDg3Njg1MTU0NDA4NA.GWVVGc.Zl8UZFtK2X0w6RrX0J3scsXZW_m71cnA30LwDI")