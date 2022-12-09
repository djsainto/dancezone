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

Run DanceZone:

```sh
python app/sourcecode.py
```

## Testing

Run tests:

```sh
pytest
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```