import discord
import random
import os
from discord.ext import commands
import requests

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
async def program(ctx):
    lista_de_mempro = os.listdir('program')
    img_name = random.choice(lista_de_mempro)

    with open(f'program/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def mem(ctx):
    lista_de_membook = os.listdir('books')
    img_book  = random.choice(lista_de_membook)

    with open(f'books/{img_book}', 'rb') as f:
         image =  discord.File(f)
    await ctx.send(file=image)      

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("Token")
