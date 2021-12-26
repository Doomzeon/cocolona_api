from handler.routes.cards_router import CardsRouter

from flask import Response

class Router:
    def __init__(self, app):
        self.app = app

        @app.route("/alive", methods=["GET"])
        def alive():
            """Check if the service is running"""
            return Response('I am alive',
                    status=202,
                    mimetype="application/json",
                )

        CardsRouter(app=app)
