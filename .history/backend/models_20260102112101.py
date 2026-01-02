from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# SQLAlchemy instance
db = SQLAlchemy()

# =========================
# MESSAGE MODEL
# =========================

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        index=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "content": self.content,
            "time": self.timestamp.strftime("%H:%M")
        }

    def __repr__(self):
        return f"<Message {self.username}: {self.content[:20]}>"
