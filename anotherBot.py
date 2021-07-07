import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix='<')

@client.event
async def on_ready():
    print('Bot connected to {0.user}'.format(client))


#Getting the messagers username.
@client.command()
async def hello(ctx):
    username = ctx.message.author.name
    await ctx.send(f'Hello, {username}')
#username = ctx.message.author.display_name  this will display the nickname and default to username if not found


#Reading from a file.
f = open('rules.txt', 'r')
rules = f.readlines()
with open('rules.txt') as f:
   count = sum(1 for _ in f)

@client.command(aliases=['rules'])
async def rule(ctx,*,number):
    if (number.isnumeric() and int(number) < 6):
        await ctx.send(rules[int(number)-1])
    elif ((number) == "all"):
        for x in range(count):
            await ctx.send(rules[x])
    elif (number.isnumeric() and int(number) > 6):
        await ctx.send(f'There is no rule {number}. So far there are only 5 rules. If you would like to add a rule, let me know.')
    else:
        await ctx.send('I see you are trying to test my code... stop it.')



#Counting the arguments.
@client.command()
async def arg(ctx,*args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


#@client.event
#async def on_message(message):
#    user = client.get_user('MEMBER ID')
#    if message.author == client.user:
#        return
#    if message.author == user:
#        if message.content == 'PASSCODE':
#            await message.channel.send('RESPOND')


client.run("")
