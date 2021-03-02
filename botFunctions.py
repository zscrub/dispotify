import discord
import dispotify

def topTracksMessage(message):
    # command is !searchTop
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
     

def artistAlbumsMessage(message):
    # command is !albums
    artist = str(message.content)[8:]
    if len(artist) != 0 and artist != ' ':
        embed_ = None
        artistName = dispotify.searchArtist(artist)[0]
        artist_id = dispotify.searchArtist(artist)[1]
        artist_albums = dispotify.artistAlbums(artist)
        if (dispotify.searchArtist(artist)[2]):
            print('Artist found!')
            if len(artist_albums)!=0:
                embed_ = discord.Embed(title = 'Albums for {0}'.format(artistName))
                for album in artist_albums:
                    embed_.add_field(name='Album {0}'.format((artist_albums.index(album))+1), value=album)
                return message.channel.send(embed=embed_)
            else:
                return message.channel.send('Could\'nt find any albums for {0} :( don\'t blame me, make sure you spelt the artist correctly, or maybe they just dont have any...'.format(artist))
        else:
            return message.channel.send('Couldn\'t find accurate results for {0}  :( don\'t blame me, make sure you spelt the artist correctly....'.format(artist))
