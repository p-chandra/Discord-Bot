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

@client.command()
async def cal(ctx,*args):
    data = list(args)
    if (len(data) % 2 != 1):
        await ctx.send("Invalid Number of Arguments")
    else:
        for x in data:
            if (x == '*'):
                index = data.index('*')
                temp = float(data.pop(index-1)) * float(data.pop(index))
                data.remove('*')
                data.insert(index-1,temp)
            elif (x == '+'):
                index = data.index('+')
                temp = float(data.pop(index-1)) + float(data.pop(index))
                data.remove('+')
                data.insert(index-1,temp)
            await ctx.send(data)
       
client.run("")
