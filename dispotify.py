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

def searchTest():
    if len(sys.argv) > 1:
        search_str = sys.argv[1]
    else:
        search_str = 'Radiohead'

    result = spotify_.search(search_str)
    pprint.pprint(result)
    return result

