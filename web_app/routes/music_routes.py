from flask import Blueprint, request, render_template, redirect, flash

from app.music import fetch_search_data

music_routes = Blueprint("interface_routes", __name__)

@music_routes.route("/music/form")
def stocks_form():
    print("MUSIC FORM...")
    return render_template("interface.html")

@music_routes.route("/music/output")
def music_home():
    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)
    song = request_data.get("search_song")
    return render_template("output.html", song=song)

