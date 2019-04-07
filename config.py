import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Aeon Klebang'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or ("sqlite:///" + os.path.join(basedir, 'anghari.db'))
    # "postgres://username:password@hostname:5432/dbname"
    # ("sqlite:///" + os.path.join(basedir, 'anghari.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- FOR EMAIL ERROR SENDING ---
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['your-email@example.com']
