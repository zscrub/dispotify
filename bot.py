import tkn
import discord
import dispotify

TOKEN = tkn.tkn

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        embed_ = discord.Embed(title = 'Here\'s some tracks for you {0.author.mention} ... '.format(message), color=0xA750DE)
        embed_.add_field(name='Fleetwood Mac', value='Hypnotized', inline=False)
        await message.channel.send(embed=embed_)

    if message.content.startswith('!theWeeknd'):
        embed_ = discord.Embed(title = 'Albums from The Weeknd', color=EF0622)
        for albumName in dispotify.wkndAlbums:
            embed_.add_field(name=albumName)
        await message.channel.send(embed=embed_)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)