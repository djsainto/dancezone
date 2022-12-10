from flask import Blueprint, request, render_template, redirect, flash

from app.music import fetch_search_data, fetch_song_data

music_routes = Blueprint("music_routes", __name__)

@music_routes.route("/music/form", methods=['GET', 'POST'])
def music_home():
    return render_template("interface.html")

@music_routes.route("/music/output", methods=['GET', 'POST'])
def music_form():
    print("MUSIC FORM...")
    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)
    inString = request_data.get("search_song")
    data = fetch_search_data(inString)
    song = fetch_song_data(data)
    return render_template("output.html", song=song)

