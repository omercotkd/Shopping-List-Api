from dotenv import load_dotenv

load_dotenv()

from flask import Flask
from flask_cors import CORS
import mongoengine as me
import os

app = Flask(__name__)
CORS(app)

me.connect(db=os.getenv("MONGO_DB"),
           username=os.getenv("MONGO_USERNAME"),
           password=os.getenv("MONGO_PASSWORD"),
           host=os.getenv("MONGO_HOST"))

# Routes
from Routes.login_route import login_routes
from Routes.manage_lists_route import manage_lists_routes

app.register_blueprint(login_routes)
app.register_blueprint(manage_lists_routes)
