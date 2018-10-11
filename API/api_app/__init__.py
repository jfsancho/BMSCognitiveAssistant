#  api_app/__init__.py
import os
from flask import Flask
from flask import session, Blueprint


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # Load the default configuration
    app.config.from_object('config')
    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py', silent=True)
    app.secret_key= 'dev' # it is necesary to user sessions
    # Now we can access the configuration variables via app.config["VAR_NAME"].

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Blueprints
    from . import auth,request

    #register the different blueprints
    app.register_blueprint(auth.bp)
    app.register_blueprint(request.bp)




    return app
