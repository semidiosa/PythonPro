import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesion con {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, me llamo {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


bot.run("Token")