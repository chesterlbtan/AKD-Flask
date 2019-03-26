import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Aeon Klebang'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgres://chester:hello987@localhost:5432/anghari_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
