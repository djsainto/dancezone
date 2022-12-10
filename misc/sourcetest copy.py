import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
from IPython.display import Image, display
from pprint import pprint
from getpass import getpass


def fetch_search_data(search_song):
        results = sp.search(search_song, 10)
        items = results['tracks']['items']
        return items

#for x in items:
            #print(str(counter)+".   " +x['album']['artists'][0]['name']+"  ---  "+x['album']['name'])
            #counter = counter + 1

def fetch_song_data(track_number, items):
        track_info = items[int(track_number)-1]
        song = track_info['external_urls']['spotify']
        cover_url = track_info['album']['images'][1]['url']
        analysis = sp.audio_features(song)
        danceability = analysis[0]['danceability'] * 100
        valence = analysis[0]['valence'] * 100
        if danceability + valence >= 120 and danceability >=60:
          output = "This song is would be good to play for a party!"
        if 120 > danceability + valence >= 90 and danceability >=60:
          output = "This song is would be ok to play at a party, but other options might be better."
        if 90> danceability + valence >= 60 and danceability >=60:
          output = "This song is not a great choice for a party. A happier song would be better."
        if 60 > danceability:
          output = "This song is not a great choice for a party. A more upbeat, danceable song would be better."
        return output, danceability, valence
