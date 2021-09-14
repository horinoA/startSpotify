import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotifyAPI as api

client_id = api.client_id
client_secret = api.client_secret
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(
    client_id, client_secret)

spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager)

name = "Stevie Wonder"
results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
serch_uri = ''
if len(items) > 0:
    artist = items[0]
    serch_uri = artist['uri']
    print(artist['name'], artist['uri'], artist['images'][0]
          ['url'])

if serch_uri != '':
    results = spotify.artist_albums(serch_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'], album['release_date'],
              album['total_tracks'], album['uri'])
