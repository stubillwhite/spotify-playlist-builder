import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from itertools import *
from random import shuffle
import os

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


class Track:

    def __init__(this, url, submitter):

        track = spotify.track(url)

        this.submitter = submitter
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
    print(t.url)
    print(t.track_name)
    print(t.artists)

    print('------')
