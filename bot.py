import discord
from discord.ext import commands
import json
import time
import datetime
import sys
import psutil
import time
import platform


def seconds_elapsed():
    return time.time() - psutil.boot_time()
OS = platform.platform()
OS2 = platform.system()

with open("cconf.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")
DEV = ""

@bot.command()
async def create(ctx, infos):
    await ctx.send(f"Deine Infos {infos}")
    await ctx.send("Okay Jut die bot infos wurden an die API Geteilt das kann jetzt bis zu 2Wochen dauern!")

@bot.command()
async def status(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    m = discord.Embed(title="INFO")
    m.add_field(name="OS-V", value=f"{OS}")
    m.add_field(name="OS", value=f"{OS2}")
    m.add_field(name="UPTIME", value=uptime)
    await ctx.send(embed=m)

@bot.command()
async def delete(ctx):
    await ctx.send("Sorry Du hast keine Bots!")

@bot.command()
async def liste(ctx):
    await ctx.send("Sorry Du hast keine Bots!")

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    helpem = discord.Embed(title="HELP PAGE  USER",timestamp=datetime.datetime.utcnow())
    helpem.add_field(name='create',value='damit erstellst du dir dein bot',inline=True)
    helpem.add_field(name='delete',value='Löscht ein bot von dir',inline=True)
    helpem.add_field(name='liste',value='zeigt deine erstellten bots',inline=True)
    helpem.add_field(name='status',value='Uptime und so',inline=True)
    helpem.set_footer(text=f'Geöffnet von {ctx.author.name}')
    helpem.set_thumbnail(url='https://i.pinimg.com/originals/f7/b1/91/f7b1914abbb5aa8d5270bcc35cc3771d.png')
    await ctx.send(embed=helpem)

@bot.event
async def on_ready():
    global startTime
    startTime = time.time()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"BOOTING Bot Ver - {discord.__version__}"))
    print("""
    ________________________
    CYOB OS LOADED SUCCSFULLY
    _________________________""")
    print(f"OS VERSION : {discord.__version__}")
    time.sleep(1)
    print(f"""
    ___OS - LOGING__
    __I {bot.user} I__
    """)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"BOOT SUCCSFULLY STARTING P-KDJH2 ..."))
    time.sleep(5)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"C!help I auf {len(bot.guilds)} Server Aktiv"))


bot.run(token)