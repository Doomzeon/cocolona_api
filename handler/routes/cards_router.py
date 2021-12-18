import logging
from flask import request, Response
from controller.cards_controller import CardController


class CardsRouter:
    def __init__(self, app):
        self.app = app

        # Add validator Authentication
        @app.route("/api_v1/card/<type>", methods=["GET"])
        def get_card(type):
            try:
                logging.info(f"Processing request /api_v1/card/{type}")
                card_controller = CardController(type=type)
                return card_controller.get_card_by_type()
            except Exception as e:
                logging.error(f"An error occured {e}")
