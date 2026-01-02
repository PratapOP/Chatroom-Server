from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Basic configuration
app.config["SECRET_KEY"] = "pulsechat-secret-key"

# Enable CORS for frontend communication
CORS(app)

# Initialize Socket.IO
socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="threading"
)

# Import socket events AFTER socketio initialization
from socket_events import register_socket_events

# Register all real-time events
register_socket_events(socketio)

# Health check route
@app.route("/")
def index():
    return {
        "status": "PulseChat backend running",
        "socket": "active"
    }

# Run server
if __name__ == "__main__":
    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=True
    )
