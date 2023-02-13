import discord
import os

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents) 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    print("message-->", message)
    if message.author == client.user:
        return
 
    if message.content == 'Oi bot':
        await message.channel.send('Falatu!')

    if message.content == 'tudo bem bot ?':
       await message.channel.send('to top e tu?')

    if message.content == 'to bem tbm':
        await message.channel.send('que bom!')  
 
    if message.content == '!apresentação':
        await message.channel.send('olá eu sou o AutoBot, fui criado pelo yuri como primeiro projeto de programação, sou amigável!!! É um prazer te conhecer!!!!')
    
    if message.content == 'AutoBot se apresente':
       await message.channel.send('olá eu sou o AutoBot, fui criado pelo yuri como primeiro projeto de programação, sou amigável!!! É um prazer te conhecer!!!!')   

    if message.content == 'bot quem devo contratar ?':
        await message.channel.send('https://www.linkedin.com/in/yuri-silva-96a115218/') 

    if message.content == '!nuvem':
       await message.channel.send('https://github.com/YuriMSdS')

    if message.content == '!developer':
        with open('foto.jpeg','rb')as f:  
         await message.channel.send(file=discord.File('foto.jpeg'))

    if message.content == 'quem é o espuminha?':
        await message.channel.send('Fuja')
    
    if message.content == '!curiosidade':
        await message.author.send('Foi uma mulher que inventou a programação!! O primeiro algoritmo de programação foi criado por Ada Lovelace, em 1833, no processo de construção de uma máquina analítica.')

    if message.content == '!fato':
        await message.author.send('O cérebro humano tem 75% de água na sua composição')

    if message.content == '!conselho':
        await message.author.send('estude! estude muito pq é o futuro!!!!')
from dotenv import load_dotenv
load_dotenv()

token = os.environ.get("TOKEN")
client.run(token)