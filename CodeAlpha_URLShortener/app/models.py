from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ShortURL(db.Model):
    __tablename__ = "short_urls"

    id = db.Column(db.Integer, primary_key=True)
    short_code = db.Column(db.String(16), unique=True, nullable=False, index=True)
    original_url = db.Column(db.Text, nullable=False)
    clicks = db.Column(db.Integer, default=0, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"<ShortURL {self.short_code} -> {self.original_url[:40]}>"