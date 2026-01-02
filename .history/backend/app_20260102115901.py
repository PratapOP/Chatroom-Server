from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

from database import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "pulsechat-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pulsechat.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)

db.init_app(app)

socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

from socket_events import register_socket_events
register_socket_events(socketio)

@app.route("/")
def index():
    return {"status": "PulseChat backend running"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()   # 🔥 creates tables automatically
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
