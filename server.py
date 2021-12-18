from flask import Flask
import logging
from handler.router import Router

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


Router(app)

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
