# spotify-discover-more

Replace the contents of a target playlist with recommendations based on the
contents of a seed playlist

The idea is to have a '\<GENRE\> Discover' target playlist which you can frequently repopulate with new 
recommendations based on a playlist of tracks from that genre that you use as the seed playlist.

## Dependencies

- Python3 w/ venv module
- Seed and target playlists are public
- Seed playlist contains more than 5 tracks

## Usage

1. Go to [https://developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Create a new app
    - name: 'spotify-discover-more'
    - desc: 'recommendations based on a playlist's content'
    - website: leave blank
    - redirect uri: 'http://127.0.0.1:9090'
    - APIs: select Web API
3. Go to the app and click 'Settings'
4. Copy the client-id and client-secret into the `scripts/run_template.sh` file
5. Change the seed playlist and target playlists in `scripts/run_template.sh`
6. Run the script!
