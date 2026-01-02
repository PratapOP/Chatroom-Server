from database import db
from werkzeug.security import generate_password_hash, check_password_hash

# =========================
# USER MODEL
# =========================

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # -------------------------
    # PASSWORD HANDLING
    # -------------------------

    def set_password(self, password: str):
        """
        Hash and store the password securely.
        """
        self.password_hash = generate_password_hash(
            password,
            method="pbkdf2:sha256",
            salt_length=16
        )

    def check_password(self, password: str) -> bool:
        """
        Verify password against stored hash.
        """
        return check_password_hash(self.password_hash, password)

    # -------------------------
    # SERIALIZATION
    # -------------------------

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }

    def __repr__(self):
        return f"<User {self.username}>"
