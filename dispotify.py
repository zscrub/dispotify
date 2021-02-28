import sys
import tkn
import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

spotify_ = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(tkn.SPOTIPY_CLIENT_ID, tkn.SPOTIPY_CLIENT_SECRET))
token = spotipy.util.prompt_for_user_token(client_id= tkn.SPOTIPY_CLIENT_ID, client_secret= tkn.SPOTIPY_CLIENT_SECRET, redirect_uri= 'http://localhost:8888/callback')


def theWeekndAlbums():
    wkndAlbums = []
    theWkndURI = 'spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ'
    results = spotify_.artist_albums(theWkndURI, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify_.next(results)
        albums.extend(results['items'])

    for album in albums:
        wkndAlbums.append(album['name'])
    return wkndAlbums


# Takes name of artist, returns artist ID
def searchArtist(artist):
    matchBool = False
    if len(sys.argv) > 1:
        search_str = sys.argv[1]
    else:
        search_str = artist
    result = spotify_.search(search_str)

    tracks_ = result['tracks']
    items_ = tracks_['items']

    artists_ = items_[0]['artists'][0]['name']
    artist_id = items_[0]['artists'][0]['id']

    for a in items_:
        if artists_.lower() != artist.lower():
            artists_ = items_[items_.index(a)]['artists'][0]['name']
        else:
            print('Match!')
            matchBool = True
            break

    if artists_.lower() != artist.lower():
        matchBool = False
        artists_ = 'Couldn\'t find anyone!'
        artist_id = None
    else:
        matchBool = True

    return artists_, artist_id, matchBool

def getArtistTopTracks(artist_id):
    tracksList = []
    topTracks = spotify_.artist_top_tracks(artist_id)
    for track in topTracks['tracks']:
        tracksList.append(track['name'])
    return tracksList


