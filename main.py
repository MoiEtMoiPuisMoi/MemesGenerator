import discord
import os
from meme.meme import *
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import datetime


cmdcount = {
    "help": 0,
    "about": 0,
    "meme": 0,
    "unknow": 0,
    "cooldown": 0
}
global count
load_dotenv(dotenv_path='config/.env')

TOKEN = os.getenv('TOKEN')
blacklistguilds = []
blacklistusers = []
author = "Moi#5013"
prefix = 'm!'
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

#########################################################
#         Bot devlopped by Moi#5013 on discord          #
#########################################################
#   __  __         _    _  _    ____    ___   _  _____  #
#  |  \/  |  ___  (_) _| || |_ | ___|  / _ \ / ||___ /  #
#  | |\/| | / _ \ | ||_  ..  _||___ \ | | | || |  |_ \  #
#  | |  | || (_) || ||_      _| ___) || |_| || | ___) | #
#  |_|  |_| \___/ |_|  |_||_|  |____/  \___/ |_||____/  #
#                                                       #
#########################################################

@bot.event
async def on_command_error(ctx, error):
    x = datetime.datetime.now()
    if isinstance(error, commands.CommandOnCooldown):
        cmdcount["cooldown"] += 1
        after = "%.2fs" %(error.retry_after)
        await ctx.send(f'Try in {after}')
        print(f"[{ctx.message.author}] at {x.hour}:{x.minute} => Try after {after}")

    if isinstance(error, commands.CommandNotFound):
        cmdcount["unknow"] += 1
        await ctx.send('Command not found\nTry m!help for help')
        print(f"[{ctx.message.author}] at {x.hour}:{x.minute} => Command not found")

    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send('The Bot has not the permission(s) to execute this ('+error.missing_perms+')')
        print(f"[{ctx.message.author}] at {x.hour}:{x.minute} => The Bot has not the permission(s) to execute this ('+error.missing_perms+')")


@bot.event
async def on_guild_join(guild):
    logChannel = bot.get_channel(838444862210179132)
    await logChannel.send("Bot has joined \""+str(guild)+"\"")


@bot.command()
async def requests(ctx):
    if ctx.message.author.id == 421001877287862278:
        embed = discord.Embed(title="‎", color=0xff0000)
        embed.set_author(name="Requests Results")
        embed.add_field(name="m!meme", value=str(cmdcount["meme"]), inline=False)
        embed.add_field(name="m!help", value=str(cmdcount["help"]),inline=False)
        embed.add_field(name="m!about", value=str(cmdcount["about"]), inline=False)
        embed.add_field(name="Cooldown", value=str(cmdcount["cooldown"]), inline=False)
        embed.add_field(name="Unknow", value=str(cmdcount["unknow"]), inline=False)
        await ctx.send(embed=embed)

@bot.command()
async def servers(ctx):
    if ctx.message.author.id == 421001877287862278:
        await ctx.send('Server List:')
        num = 0
        num2 = 0
        tmember = 0
        for i in bot.guilds:
            server = bot.guilds[num]
            await ctx.send(f"=================\nName: {server.name}\nMember: {server.member_count}\nID: {server.id}\nOwner ID: {server.owner_id}\n")

            num = num + 1

        for i in bot.guilds:
            server = bot.guilds[num2]
            tmember = tmember + int(server.member_count)

            num2 = num2 + 1

        await ctx.send(f"=================\nTotal Member: {tmember}\nAnd {len(bot.guilds)}\'s servers'")
    else:
        await ctx.send("Command not found\nTry m!help for help")

def getMembers():
    tmember = 0
    num2 = 0
    for i in bot.guilds:
        server = bot.guilds[num2]
        tmember = tmember + int(server.member_count)

        num2 = num2 + 1

    return str(tmember)

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="%s Guilds" % (len(bot.guilds))))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="m!help"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="%s Users" %(getMembers())))
        await asyncio.sleep(5)

@bot.event
async def on_ready():
    print('I am ready')
    bot.loop.create_task(status_task())

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def meme(ctx):
    cmdcount["meme"] += 1
    if ctx.message.guild.id not in blacklistguilds or ctx.message.author.id not in blacklistusers:
        memer = Meme()
        spoiled = ""
        nsfwed = ""

        embed = discord.Embed(title=memer.title, url=memer.postLink, color=0xff4500)
        embed.set_author(name=memer.subreddit, url="https://www.reddit.com/r/"+memer.subreddit,
                         icon_url="https://data.apksum.com/cb/com.jetfuel.colormeme/10.0/icon.png")
        embed.set_footer(text="👍: "+str(memer.ups))

        if memer.spoiler == True:
            spoiled = "WARNING This meme is tagged (SPOILER)\n"
            embed.set_image(url='https://i.ibb.co/9npPd82/spoil.png')
        else:
            spoiled = ""
            embed.set_image(url=memer.url)

        if memer.nsfw == True:
            nsfwed = "WARNING This meme is tagged (NSFW)\n"
            embed.set_image(url='https://i.ibb.co/9npPd82/spoil.png')
        else:
            nsfwed = ""
            embed.set_image(url=memer.url)

        msg = await ctx.send(spoiled+nsfwed, embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

    else:
        await ctx.send("Your server is blacklisted\nContact "+author)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def about(ctx):
    cmdcount["about"] += 1
    if ctx.message.guild.id not in blacklistguilds and ctx.message.author.id not in blacklistusers:
        embed = discord.Embed(title="\n", color=0xff0000)
        embed.set_author(name="About Us")
        embed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Red_information_icon_with_gradient_background.svg/1024px-Red_information_icon_with_gradient_background.svg.png")
        embed.add_field(name="Moi#5013", value="The Coder", inline=False)
        embed.add_field(name="Cam15#2706", value="The Imaginator", inline=False)
        await ctx.message.author.send("https://www.coolcraft.ovh/memeshub", embed=embed)
        await ctx.send('Message send in DM')
    else:
        await ctx.send("Your server is blacklisted\nContact "+author)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx):
    cmdcount["help"] += 1
    if ctx.message.guild.id not in blacklistguilds and ctx.message.author.id not in blacklistusers:
        embed = discord.Embed(title="\n")
        embed.set_author(name="Help")
        embed.set_thumbnail(url="https://mypass.ace-energy.co.th/asset/img/icon_helpdesk.png")
        embed.add_field(name="m!meme", value="Show a random meme", inline=False)
        embed.add_field(name="m!about", value="Send private message to our Discord Me Page", inline=False)
        embed.add_field(name="m!help", value="Show this message", inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Your server is blacklisted\nContact "+author)

bot.run(TOKEN)
