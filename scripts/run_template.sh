export SPOTIPY_CLIENT_ID='your-client-id' # MODIFY
export SPOTIPY_CLIENT_SECRET='your-client-secret' #MODIFY
export SPOTIPY_REDIRECT_URI='http://127.0.0.1:9090'

source ./env/bin/activate
python3 app.py
