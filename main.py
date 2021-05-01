import discord
import os
from meme.meme import *
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
prefix = 'm!'
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('Try in %.2fs' %(error.retry_after))

    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found\nTry m!help for help')
    if isinstance(error, commands.MissingRole):
        await ctx.send('You have not the role to execute this ('+error.missing_role+")")
    raise error

@bot.event
async def on_guild_join(guild):
    logChannel = bot.get_channel(838083718802440232)
    await logChannel.send("Bot has joined \""+str(guild)+"\"")


@bot.command()
async def servers(ctx):
    await ctx.send('Server List:')
    num = 0
    for i in bot.guilds:
        server = bot.guilds[num]
        num =num + 1
        await ctx.send(f"=================\nName: {server.name}\nMember: {server.member_count}\nID: {server.id}")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="m!help"))
    print('I am ready')


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def meme(ctx):
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

    await ctx.send(spoiled+nsfwed, embed=embed)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def about(ctx):
    embed = discord.Embed(title="\n", color=0xff0000)
    embed.set_author(name="About Us")
    embed.set_thumbnail(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Red_information_icon_with_gradient_background.svg/1024px-Red_information_icon_with_gradient_background.svg.png")
    embed.add_field(name="Moi#5013", value="The Coder", inline=False)
    embed.add_field(name="Cam15#2706", value="The Imaginator", inline=False)
    await ctx.message.author.send("https://discord.me/memeshub", embed=embed)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx):
    embed = discord.Embed(title="\n")
    embed.set_author(name="Help")
    embed.set_thumbnail(url="https://mypass.ace-energy.co.th/asset/img/icon_helpdesk.png")
    embed.add_field(name="m!meme", value="Show a random meme", inline=False)
    embed.add_field(name="m!about", value="Send private message to our Discord Me Page", inline=False)
    embed.add_field(name="m!help", value="Show this message", inline=False)
    await ctx.send(embed=embed)

bot.run(TOKEN)
