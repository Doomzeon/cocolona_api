from flask import Flask
import logging
from handler.router import Router
from dotenv import load_dotenv

from flask_cors import CORS

load_dotenv()

application = Flask(__name__)
cors = CORS(app)

logging.basicConfig(level=logging.INFO)


Router(app)

if __name__ == "__main__":
    application.run(debug=True)
