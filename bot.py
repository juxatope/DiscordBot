import discord
import os
from cowpy import cow
from discord.ext import commands
import rat

AUTH_ENV_KEY = 'D_BOT_AUTH'
auth = os.getenv(AUTH_ENV_KEY)

onlineList = []
offlineList = []
bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print('bot is ready')

@bot.command()
async def hello(ctx):
    await ctx.send('hello')

@bot.command()
async def cowsay(ctx,inp):
    cheese = cow.Moose()
    msg = cheese.milk(inp)
    await ctx.send(msg)

@bot.command()
async def onlineCheck(ctx):
    for user in ctx.guild.members:
        if user.status != discord.Status.offline:
            #print ("online: "+user.name+"#"+user.discriminator)
            #await ctx.send("online: "+user.name+"#"+user.discriminator)
            onlineList.append(user.name)
        elif user.status == discord.Status.offline:
            #print ("offline: "+user.name+"#"+user.discriminator)
            #await ctx.send("offline: "+user.name+"#"+user.discriminator)
            offlineList.append(user.name)

@bot.command()
async def checkLists(ctx):
    for user in onlineList:
        await ctx.send("on:"+user)
        print("on:"+user)
    for user in offlineList:
        await ctx.send("off:"+user)
        print("off:"+user)

@bot.command()
async def chooseGame(ctx):
    for user in onlineList:
        await ctx.send("on:"+user)
        print("on:"+user)
    for user in offlineList:
        await ctx.send("off:"+user)
        print("off:"+user)
    
bot.run(auth)