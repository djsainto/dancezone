from flask import Blueprint, request, render_template, redirect, flash

from app.dance import fetch_search_data, # commands for turning data into 10 tracks

number_routes = Blueprint("number_routes", __name__)


@number_routes.route("/tracklist")
def number_routes():
    try:
        track_list = fetch_search_data()
        return render_template("number.html",
            track_list = track_list
        )
    except Exception as err:
        print('OOPS', err)
        return redirect("/")