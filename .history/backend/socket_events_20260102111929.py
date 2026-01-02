from flask_socketio import emit
from datetime import datetime

# In-memory user store (later replaced with DB / Redis)
connected_users = {}

def register_socket_events(socketio):

    @socketio.on("connect")
    def handle_connect():
        print("New socket connected")

    @socketio.on("join")
    def handle_join(data):
        username = data.get("username", "Anonymous")

        connected_users[username] = True

        emit(
            "status",
            {
                "msg": f"{username} joined the chat",
                "time": current_time()
            },
            broadcast=True
        )

    @socketio.on("message")
    def handle_message(data):
        user = data.get("user", "Anonymous")
        text = data.get("text", "")

        if not text.strip():
            return

        emit(
            "message",
            {
                "user": user,
                "text": text,
                "time": current_time()
            },
            broadcast=True
        )

    @socketio.on("typing")
    def handle_typing():
        emit("typing", broadcast=True, include_self=False)

    @socketio.on("disconnect")
    def handle_disconnect():
        print("Socket disconnected")
        emit(
            "status",
            {
                "msg": "A user left the chat",
                "time": current_time()
            },
            broadcast=True
        )


def current_time():
    return datetime.now().strftime("%H:%M")
