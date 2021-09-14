import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json as json
import spotifyAPI as api

client_id = api.client_id
client_secret = api.client_secret
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(
    client_id, client_secret)

spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager)

name = "Stevie Wonder"
result = spotify.search(q="artist:" + name, type="track")
print(result)
