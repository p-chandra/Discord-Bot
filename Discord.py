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
    temp = 0
    for index, x in enumerate(args):
    	if (x == '+'):
    	    temp = int(args[index-1]) + int(args[index+1])
    	
    	elif (x == '-'):
    	    temp = int(args[index-1]) - int(args[index+1])
    	
    	elif(x == '*'):
    	    temp = int(args[index-1]) * int(args[index+1])
    	
    	elif(x == '/' and args[index+1] != '0'):
    	    temp = int(args[index-1]) / int(args[index+1])
    
    	else:
    	    await ctx.send("Invalid Data Entry")
    	    break
    await ctx.send(temp)

        
client.run("")
