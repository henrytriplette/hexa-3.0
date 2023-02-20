import configparser

from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit

# Read Configuration
config = configparser.ConfigParser()
config.read("config.ini")

# instantiate the app
app = Flask(__name__)
app.config["SECRET_KEY"] = config["system"]["secret_key"]
app.config["DEBUG"] = config["system"]["debug"]

# enable CORS
CORS(app)

# enable SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

# 404
@app.errorhandler(404)
def not_found(e):
    return "Not Found", 404

# On connection
@socketio.event
def connection(message):
    print('Client connected')
    socketio.emit('status_log', {'data': 'Client connected'})

@socketio.event
def connect_error(data):
    print("The connection failed!")
    socketio.emit('error', {'data': 'The connection failed'})

@socketio.event
def disconnect():
    print("I'm disconnected!")
    socketio.emit('error', {'data': 'The connection failed'})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=config["system"]["debug"])
