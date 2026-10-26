
import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-me")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///shortener.sqlite3"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:5000")
    SHORT_CODE_LENGTH = 7


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"