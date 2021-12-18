from handler.routes.cards_router import CardsRouter


class Router:
    def __init__(self, app):
        self.app = app

        @app.route("/api_v1/alive", methods=["GET"])
        def alive():
            """Check if the service is running"""
            return "I'm alive!"

        CardsRouter(app=app)
