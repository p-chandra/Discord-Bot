
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
async def ascii(ctx,*args):
    for i in args:
        if (len(i) >= 2):
            await ctx.send("Invalid Input: Check Spaces")
        else:
            await ctx.send('\'{}\' = {}'.format(i,ord(i)))


#!cal 1 + 3 * 6 / 7
#make sure to use space after each input
@client.command()
async def cal(ctx,*args):
    data = list(args)
    if (len(data) % 2 != 1):
        await ctx.send("Invalid Number of Arguments")
    else:
        while '*' in data or '/' in data:
          for x in data:
            if (x == '*'):
                index = data.index('*')
                temp = float(data.pop(index-1)) * float(data.pop(index))
                data.remove('*')
                data.insert(index-1,temp)
            if (x == '/'):
                index = data.index('/')
                temp = float(data.pop(index-1)) / float(data.pop(index))
                data.remove('/')
                data.insert(index-1,temp)
        while '+' in data or '-' in data:
          for x in data:
            if (x == '+'):
                index = data.index('+')
                temp = float(data.pop(index-1)) + float(data.pop(index))
                data.remove('+')
                data.insert(index-1,temp)
            if (x == '-'):
                index = data.index('-')
                temp = float(data.pop(index-1)) - float(data.pop(index))
                data.remove('-')
                data.insert(index-1,temp)
        await ctx.send(data[0])

        
client.run("")
