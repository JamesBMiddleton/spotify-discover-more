import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

playlist_map = {
        "--- Techno" : "0DAtTiYMvfWEBxOc8fTbJy"
    }

# genre_seeds = sp.recommendation_genre_seeds()
# print(genre_seeds)
genre_seeds = ["deep-house", "edm", "electro", "electronic", "house"]

artist_uris = []
song_uris = []
playlist = sp.playlist(playlist_map["--- Techno"])
for track in playlist["tracks"]["items"]:
    for artist in track["track"]["artists"]:
        artist_uris.append(artist["uri"])
    song_uris.append(track["track"]["uri"])

# print(artist_uris)
# print(song_uris)

recommendations = sp.recommendations(seed_artists=artist_uris[:4],
                                     # seed_tracks=song_uris,
                                     limit = 100,
                                     county = 'GB') 

for track in recommendations["tracks"]:
    print(track["name"], end=" --- ")
    for artist in track["artists"]:
        print(artist["name"], end=", ")
    print()

    
