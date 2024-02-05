import spotipy
import json

credentials_file_path = './credentials.json'

with open(credentials_file_path, 'r') as f:
    credentials = json.load(f)

sp = spotipy.Spotify(auth=credentials['token'])

def get_release_date(song):
    result = sp.search(song)
    tracks = result['tracks']['items']
    if len(tracks) > 0:
        return tracks[0]['album']['release_date']
    else:
        return None

def get_popularity(song):
    result = sp.search(song)
    tracks = result['tracks']['items']
    if len(tracks) > 0:
        return tracks[0]['popularity']
    else:
        return None

def get_explicitness(song):
    result = sp.search(song)
    tracks = result['tracks']['items']
    if len(tracks) > 0:
        return tracks[0]['explicit']
    else:
        return None

def get_market_number(song):
    result = sp.search(song)
    tracks = result['tracks']['items']
    if len(tracks) > 0:
        return len(tracks[0]['available_markets'])
    else:
        return None