import  discord
from discord.ext import commands
import json,os,sqlite3
intents = discord.Intents.default()
intents.presences = True
intents.members = True
from discord_together import DiscordTogether
with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

token = config["token"]
prefix = config["prefix"] 
bot = commands.Bot(command_prefix=prefix, intents=intents,help_command=None)  
db=sqlite3.connect("main.db",detect_types=sqlite3.PARSE_DECLTYPES, isolation_level=None)
bot.db=db
bot.close_=bot.close
async def newclose():
    db.commit()
    db.close()
    await bot.close_()
def savedb():
    db.commit()
bot.close=newclose
bot.savedb=savedb
bot.cursor=db.cursor()
if __name__ == '__main__':
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
bot.load_extension('jishaku')
@bot.event
async def on_ready():
    bot.togetherControl = await DiscordTogether(token)

@bot.command()
async def start(ctx):
    link = await bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"{link}\n を推してね!")

bot.run(token)