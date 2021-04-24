import discord
from meme.meme import *
from discord.ext import commands

TOKEN = 'YOUR TOKEN'
prefix = '!'
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('Essayer dans %.2fs' % error.retry_after)

    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command introuvable')
    raise error

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="!meme"))
    print('I am ready')

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def meme(ctx):
    memer = MemeAPI()
    spoiled = ""
    nsfwed = ""

    embed = discord.Embed(title=memer.title, url=memer.postLink, color=0xff4500)
    embed.set_author(name=memer.subreddit, url="https://www.reddit.com/r/"+memer.subreddit,
                     icon_url="https://data.apksum.com/cb/com.jetfuel.colormeme/10.0/icon.png")

    if memer.spoiler == True:
        spoiled = "WARNING Ce meme est taggé (SPOILER)\n"
        embed.set_image(url='https://i.ibb.co/9npPd82/spoil.png')
    else:
        spoiled = ""
        embed.set_image(url=memer.url)

    if memer.nsfw == True:
        nsfwed = "WARNING Ce meme est taggé (NSFW)\n"
        embed.set_image(url='https://i.ibb.co/9npPd82/spoil.png')
    else:
        nsfwed = ""
        embed.set_image(url=memer.url)

    await ctx.send(spoiled+nsfwed, embed=embed)

bot.run(TOKEN)
