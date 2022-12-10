# this is the "web_app/__init__.py" file...

import os
from dotenv import load_dotenv
from flask import Flask

from web_app.routes.interface_route import interface
from web_app.routes.numbers_route import number
from web_app.routes.output_route import output

#load_dotenv()

#SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # set this to something else on production!!!

def create_app():
    app = Flask(__name__)
   # app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(interface)
    app.register_blueprint(number)
    app.register_blueprint(output)
   
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)