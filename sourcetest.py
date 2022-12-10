import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
from IPython.display import Image, display
from pprint import pprint
from getpass import getpass

Client_ID = getpass("Please input your client_id:") 
Client_Secret = getpass("Please input your client_secret")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=Client_ID, client_secret=Client_Secret))

print("This program will return the danceability of a track given a user input")

def dancezone(search_song, track_number):
        search_song = input("Enter the song name: ")
        print("  ")
        results = sp.search(search_song, 10)
        if len(results['tracks']['items'])> 1:
          print("There are many tracks with that name attributed to different albums and artists. Here is a list of the top 10.")
          print("  ")
          items = results['tracks']['items']
          counter = 1
          for x in items:
              print(str(counter)+".   " +x['album']['artists'][0]['name']+"  ---  "+x['album']['name'])
              counter = counter + 1
          print("  ")
          track_number = input("Which of these projects contains the track you're looking for (enter their number in the list): ")
          track_info = items[int(track_number)-1]
          song = track_info['external_urls']['spotify']
          cover_url = track_info['album']['images'][1]['url']
          analysis = sp.audio_features(song)
          danceability = analysis[0]['danceability'] * 100
          valence = analysis[0]['valence'] * 100
          print(' ')
          display(Image(url=cover_url, height=100))
          print(' ')
          print("The danceability of this song is:", danceability, "%")
          print("The valence of this song is:", valence, "%")
          print("Here is the analyzed song url:")
          print(song)
          print(' ')
        elif len(results['tracks']['items']) < 2:
          results = sp.search(search_song, 1, 0, "track")
          songs_dict = results['tracks']
          song_items = songs_dict['items']
          song = song_items[0]['external_urls']['spotify']
          cover_url = song_items[0]['album']['images'][1]['url']
          analysis = sp.audio_features(song)
          danceability = analysis[0]['danceability'] * 100
          valence = analysis[0]['valence'] * 100
          print(' ')
          display(Image(url=cover_url, height=100))
          print("The danceability of this song is:", danceability, "%")
          print("The valence of this song is:", valence, "%")
          print("Here is the analyzed song url:")
          print(song)
        if danceability + valence >= 120 and danceability >=60:
          output = "This song is would be good to play for a party!"
        if 120 > danceability + valence >= 90 and danceability >=60:
          output = "This song is would be ok to play at a party, but other options might be better."
        if 90> danceability + valence >= 60 and danceability >=60:
          output = "This song is not a great choice for a party. A happier song would be better."
        if 60 > danceability:
          output = "This song is not a great choice for a party. A more upbeat, danceable song would be better."
      return output