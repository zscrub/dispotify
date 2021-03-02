import tkn
import discord
import dispotify
import botFunctions

TOKEN = tkn.tkn

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Remove case sensitivity in commands
    message.content=message.content.lower()

    # if message.content.startswith('!hello'):
    #     embed_ = discord.Embed(title = 'Here\'s some tracks for you {0.author.mention} ... '.format(message), color=0xA750DE)
    #     embed_.add_field(name='Fleetwood Mac', value='Hypnotized', inline=False)
    #     await message.channel.send(embed=embed_)

    if message.content.startswith('!searchtop'):
        await botFunctions.topTracksMessage(message)

    if message.content.startswith('!albums'):
        await botFunctions.artistAlbumsMessage(message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)