# CSVファイルを保存するpandasをpdという名前でインポートします
import pandas as pd
# Spotify用のAPIを取り込みます
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# token用のファイルspotifyAPI.pyを別で用意し、apiよいう名前でインポートします
# これでtokenをとりあえずベタガキしないですみます
import spotifyAPI as api

# apiからtokenはよびだします
client_id = api.client_id
client_secret = api.client_secret
# ここからはSpotifyAPIの設定です
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(
    client_id, client_secret)
spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager)

# name変数に検索したいミュージシャン名をいれます
name = "Stevie Wonder"
results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
serch_uri = ''
if len(items) > 0:
    artist = items[0]
    serch_uri = artist['uri']
#    print(artist['name'], artist['uri'], artist['images'][0]
#          ['url'])

if serch_uri != '':
    path = "../albums.csv"
    results = spotify.artist_albums(serch_uri, album_type='album')
    albums = results['items']

    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'], album['release_date'],
              album['total_tracks'], album['uri'])

    # pandasのDataFrameでJsonを変換します
    df = pd.DataFrame(albums)
    #　path変数にフルパス入るとフォルダも指定できます。encodingで文字コードを指定して保存できます
    df.to_csv(path, encoding='shift_jis')
