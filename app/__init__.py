import os
from flask import Flask
from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    import app.graph.controllers as graph
    import app.general.controllers as general
    import app.autorization.controllers as autorization
    import app.articles.controllers as articles

    app.register_blueprint(graph.module)
    app.register_blueprint(general.module)
    app.register_blueprint(autorization.module)
    app.register_blueprint(articles.module)

    db.init_app(app)
    with app.test_request_context():
        db.create_all() #db.drop_all()
#    with app.app_context():
#        db.init_app(app)
#        db.create_all()

    if app.debug == True:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            toolbar = DebugToolbarExtension(app)
        except:
            pass


    return app
