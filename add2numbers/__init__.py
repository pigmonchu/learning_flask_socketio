from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    from .operations import operations as operations_blueprint

    @app.route('/')
    def hello_world():
        return 'Flask running'

    app.register_blueprint(operations_blueprint)
    CORS(app)
    socketio.init_app(app, cors_allowed_origins="*")
    return app

