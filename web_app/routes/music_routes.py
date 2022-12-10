from flask import Blueprint, request, render_template, redirect, flash

from app.music import fetch_search_data

music_routes = Blueprint("interface_routes", __name__)

@music_routes.route("/interface")

@music_routes.route("/stocks/form")
def stocks_form():
    print("STOCKS FORM...")
    return render_template("stocks_form.html")