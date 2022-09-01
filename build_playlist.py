import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

from itertools import *
from random import shuffle
import os

scope = 'playlist-modify-public'

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, redirect_uri='http://localhost:8080'))


class Track:

    def __init__(this, url, submitter):

        track = spotify.track(url)

        this.submitter = submitter
        this.id = track['id']
        this.url = track['external_urls']['spotify']
        this.track_name = track['name']
        this.artists = ' / '.join([artist['name'] for artist in track['artists']])


def read_lines(path):
    lines = []
    with open(path, 'r') as f:
        lines = f.readlines()
    return [l.strip() for l in lines]


def read_tracks(path):
    submitter = os.path.basename(path)
    return [Track(url, submitter) for url in read_lines(path)]


def flatten(coll):
    return [x for xs in coll for x in xs]


playlist_dir = 'playlists'

submission_files = [os.path.join(playlist_dir, os.fsdecode(f)) for f in os.listdir(playlist_dir)]

tracks = flatten([read_tracks(path) for path in submission_files])

shuffle(tracks)

for t in tracks:
    
    print(t.submitter)
    print(t.id)
    print(t.url)
    print(t.track_name)
    print(t.artists)

    print('------')

user_id = spotify.current_user()['id']

playlist = spotify.user_playlist_create(user=user_id, name='Test playlist')
playlist_id = playlist['id']

track_ids = [t.id for t in tracks]

spotify.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=track_ids)
