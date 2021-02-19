import spotipy
import util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials


wkndAlbums = []
theWkndURI = 'spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
token = util.prompt_for_user_token(username, scope, redirect_uri = 'https://example.com/callback/')

results = spotify.artist_albums(theWkndURI, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    wkndAlbums.append(album['name'])