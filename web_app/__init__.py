# this is the "web_app/__init__.py" file...

import os
from dotenv import load_dotenv
from flask import Flask
from web_app.routes.music_routes import music_routes

#load_dotenv()

load_dotenv()

Client_ID = os.getenv("Client_ID")
Client_Secret = os.getenv("Client_Secret")

def create_app():
    app = Flask(__name__)
    app.config["Client_ID"] = Client_ID
    app.config["Client_Secret"] = Client_Secret


    app.register_blueprint(music_routes)
   
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)