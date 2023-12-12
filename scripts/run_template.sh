cd $(dirname "${BASH_SOURCE[0]}")
cd ..

export SPOTIPY_CLIENT_ID='your-client-id' # MODIFY
export SPOTIPY_CLIENT_SECRET='your-client-secret' # MODIFY
export SPOTIPY_REDIRECT_URI='http://127.0.0.1:9090'

if [ -d "env" ]; then
    source ./env/bin/activate
else
    python3 -m venv env
    source ./env/bin/activate
    pip install -r "requirements.txt"
fi

python3 app.py "seed-playlist-name" "target-playlist-name" # MODIFY
