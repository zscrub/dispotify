import tkn
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials


wkndAlbums = []
theWkndURI = 'spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(tkn.SPOTIPY_CLIENT_ID, tkn.SPOTIPY_CLIENT_SECRET))
token = spotipy.util.prompt_for_user_token(client_id= tkn.SPOTIPY_CLIENT_ID, client_secret= tkn.SPOTIPY_CLIENT_SECRET, redirect_uri= 'http://localhost:8888/callback')


results = spotify.artist_albums(theWkndURI, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    wkndAlbums.append(album['name'])

