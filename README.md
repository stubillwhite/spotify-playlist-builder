# spotify-playlist-builder #

Tiny script to take our team's submitted tracks and generate a playlist on Spotify for our bi-weekly music quiz.

## Running the script ##

- Set up the Python environment
    - `python3 -m venv .`
    - `source bin/activate`
    - `pip3 install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org --default-timeout=1000 -r requirements.txt`

- Add text files with the URLs to the desired songs
    - Create text files containing Spotify URLs in the `playlists` directory

- Run the script
    - Set the Spotify client keys to the development keys from your account
        - `export SPOTIPY_CLIENT_ID="${SECRET_SPOTIFY_CLIENT_ID}"`
        - `export SPOTIPY_CLIENT_SECRET="${SECRET_SPOTIFY_CLIENT_SECRET}"`
    - `python build_playlist.py --upload`
    - The playlist will be created under the name `generated-playlist` in your Spotify account

## Other useful stuff ##

- `extract_data.py`
    - This script will extract the data from the Excel results file we use (an example file,
      `recs-roadtrip-playlist-quiz-master.xlsx`, is checked in here) and output a denormalised CSV file that you can use
      for quick analysis

- `display-stats.sh`
    - This script takes the CSV file output by the previous script and calculates a few interesting statistics (e.g.,
      most easily guessed, most popular tracks, most correct guesses, etc.).
