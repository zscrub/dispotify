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
        embed_ = discord.Embed(title = 'Albums from The Weeknd', color=0xA750DE)
        for albumName in dispotify.theWeekndAlbums():
            # await message.channel.send(albumName)
            embed_.add_field(name=dispotify.theWeekndAlbums().index(albumName)+1, value=albumName)
        await message.channel.send(embed=embed_)

    if message.content.startswith('!searchf'):
        embed_ = discord.Embed(title = 'Search for Radiohead')
        for r in dispotify.searchTest():
            embed_.add_field(name='Radiohead?', value=r)  
        
        await message.channel.send(embed=embed_)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)