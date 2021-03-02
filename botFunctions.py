import discord
import dispotify

def topTracksMessage(message):
    artist = str(message.content)[11:]
    if len(artist) != 0 and artist != ' ':
        embed_ = None
        artistName = dispotify.searchArtist(artist)[0]
        artist_id = dispotify.searchArtist(artist)[1]
        if (dispotify.searchArtist(artist)[2]):
            embed_ = discord.Embed(title = 'Top track results for {0}'.format(artistName))
            for track in dispotify.getArtistTopTracks(artist_id):
                print(track)
                embed_.add_field(name='Track #{0}'.format((dispotify.getArtistTopTracks(artist_id).index(track))+1),
                                                                            value=track)
            return message.channel.send(embed=embed_)
        else:
            print(dispotify.searchArtist(artist))
            print(artistName)
            print(artist)
            return message.channel.send('Couldn\'t find accurate results for {0}  :('.format(artist))

    else:
        return message.channel.send('Name an artist after the command to retrieve top tracks! For example:\n ```!searchtop Nirvana``` ')
    return 