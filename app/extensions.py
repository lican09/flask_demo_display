# -*- coding: utf-8 -*-

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from raven.contrib.flask import Sentry

from app.config import DefaultConfig

bcrypt = Bcrypt()
login_manager = LoginManager()
sentry = Sentry(dsn=DefaultConfig.SENTRY_DSN)