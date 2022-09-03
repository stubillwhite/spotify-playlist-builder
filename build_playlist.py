import click
import os
import spotipy
from random import shuffle
from spotipy.oauth2 import SpotifyOAuth

PLAYLIST_DIR = 'playlists'
PLAYLIST_NAME = 'generated-playlist'


class Track:

    def __init__(this, spotify, url, submitter):
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


def read_tracks(spotify, path):
    submitter = os.path.basename(path)
    return [Track(spotify, url, submitter) for url in read_lines(path)]


def flatten(coll):
    return [x for xs in coll for x in xs]


def build_spotify_client():
    scope = 'playlist-modify-public'
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, redirect_uri='http://localhost:8080'))


def compile_track_list(spotify):
    submission_files = [os.path.join(PLAYLIST_DIR, os.fsdecode(f)) for f in os.listdir(PLAYLIST_DIR)]
    tracks = flatten([read_tracks(spotify, path) for path in submission_files])
    shuffle(tracks)
    return tracks


def display_track_list(show_submitter, tracks):
    if show_submitter:
        fmt_track = lambda t: f'{t.url}\t{t.artists}\t{t.track_name}\t{t.submitter}'
    else:
        fmt_track = lambda t: f'{t.url}\t{t.artists}\t{t.track_name}'

    for t in tracks:
        print(fmt_track(t))


def generate_spotify_playlist(spotify, tracks):
    user_id = spotify.current_user()['id']

    playlist = spotify.user_playlist_create(user=user_id, name=PLAYLIST_NAME)
    playlist_id = playlist['id']

    track_ids = [t.id for t in tracks]

    spotify.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=track_ids)


@click.command()
@click.option('--upload', is_flag=True, help='Upload the playlist to Spotify')
@click.option('--show-submitter', is_flag=True, help='Display who submitted the track')
def build_playlist(upload, show_submitter):
    spotify = build_spotify_client()

    tracks = compile_track_list(spotify)
    display_track_list(show_submitter, tracks)

    if upload:
        generate_spotify_playlist(spotify, tracks)


if __name__ == '__main__':
    build_playlist()
