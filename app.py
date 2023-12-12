import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import sys

if len(sys.argv) != 3:
    print("\nERROR: Please provide the name of the seed playlist as the first argument \
            and the target playlist as the second argument")
    exit()
    
seed_playlist = sys.argv[1]
target_playlist = sys.argv[2]

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

user_playlists = sp.current_user_playlists()

seed_playlist_id = ""
target_playlist_id = ""
for playlist in user_playlists["items"]:
    if playlist["name"] == seed_playlist:
        seed_playlist_id = playlist["id"]
    if playlist["name"] == target_playlist:
        target_playlist_id = playlist["id"]
if seed_playlist_id == "":
    print(f"ERROR: Could not find seed playlist '{seed_playlist}' - is it a public playlist?")
    exit()
if target_playlist_id == "":
    print(f"ERROR: Could not find target playlist '{target_playlist}' - is it a public playlist?")
    exit()

artist_uris = []
track_uris = []
playlist = sp.playlist(seed_playlist_id)
for track in playlist["tracks"]["items"]:
    for artist in track["track"]["artists"]:
        artist_uris.append(artist["uri"])
    track_uris.append(track["track"]["uri"])

random.shuffle(artist_uris)
random.shuffle(track_uris)
recommendations = sp.recommendations(#seed_artists=artist_uris[:4],
                                     seed_tracks=track_uris[:5],
                                     limit = 100,
                                     county = 'GB') 

recommendation_uris = []
for track in recommendations["tracks"]:
    recommendation_uris.append(track["uri"])
    # print(track["name"], end=" --- ")
    # for artist in track["artists"]:
    #     print(artist["name"], end=", ")
    # print()


scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
sp.user_playlist_replace_tracks(sp.me(), 
                                target_playlist_id,
                                recommendation_uris)

print(f"\nSUCCESS: Contents of '{target_playlist}' has been replaced with recommendations")
    
