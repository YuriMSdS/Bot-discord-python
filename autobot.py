import discord


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
 
    if message.content.startswith('hi'):
        await message.channel.send('Hello!')
 
    if message.content.startswith('image'):
        await message.channel.send(file=discord.File('download.jpg'))
client.run('MTA2NTc5MjE4MTExOTUwNDM4NA.Gm4Wwr.Pvg_4eWF_cX51F1SJuiu9r4cFTLL30623_s0Wk')