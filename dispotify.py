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




def searchTest(artist):
    if len(sys.argv) > 1:
        search_str = sys.argv[1]
    else:
        search_str = artist

    result = spotify_.search(search_str)
    # pprint.pprint(result)


    topTracksList=[]
    tracks_ = result['tracks']
    # pprint.pprint(tracks_)
    items_ = tracks_['items']
    artists_ = items_[0]['artists'][0]['name']

    artist_id = items_[0]['artists'][0]['id']

    # check if the query for artist matches the artist returned from search results 
    # if artists_.lower() == artist.lower():
        # print(True)
        # print(artist_id)
    # print('{0} -- {1}'.format(artists_.lower(), artist.lower()))
    topTracks_ = spotify_.artist_top_tracks(artist_id)
    for track in topTracks_['tracks']:
        topTracksList.append(track['name'])
    # should loop through items_ to find artist matching query for id

    # items_ returns large dictionary, topTracksList returns list of top tracks via spotipy
    return items_, topTracksList

# fetching artist name example
# print()
# print(searchTest('future')[0][0]['artists'][0]['name'])


# example for track pulling 
# for i in range(len(searchTest('young thug'))):
#     print('\n{0}'.format((searchTest('young thug')[i]['name'])))