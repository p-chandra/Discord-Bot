#bot.py

import discord
from discord.ext import commands

client = discord.Client() 
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot connected to {0.user}'.format(client))
    
@client.command()
async def hello(ctx,*args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
    
@client.command()
async def add(ctx,*args: int):
    await ctx.send(sum(args))

@client.command()
async def sub(ctx,*args: int):
    temp = 0
    for i in args:
        temp = i - temp
    await ctx.send(temp)

@client.command()
async def mul(ctx,*args: int):
    await ctx.send(sum(args))

@client.command()
async def div(ctx,*args: int):
    await ctx.send(sum(args))


        
client.run("NDMxMjk1MzQxNTMxNDk2NDQ4.WsWZFg.aYv-vk483AWIE7x4KrT8kMg3lzo")
