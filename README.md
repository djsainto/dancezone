# dancezone

##README File

## Usage

```sh
python app/sourcecode.py
```

## Configuration


Obtain Spotify Credentials

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file...

client_id="___________________"
client_secret="___________________"
```

Run DanceZone's source code:

```sh
python -m misc.sourcecode
```

## Testing

Run tests:

```sh
pytest
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/music/form):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# If it asks for client ID export it from console
export SPOTIPY_CLIENT_ID='02633e8b7f0e43a2bf16882a47f72f55'
export SPOTIPY_CLIENT_SECRET='e8d29c15040049bc94a0b1c488aa3ae6'
export SPOTIPY_REDIRECT_URI='http://google.com/callback/'

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```
