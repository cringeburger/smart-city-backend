from resources.db_queries.connection import db_cursor
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Custom modules
import resources.routes
from resources.modules.config import host_val
