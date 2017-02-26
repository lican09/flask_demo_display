# -*- coding: utf-8 -*-


class BaseConfig:

    PROJECT = 'flask_rest_diplay'
    SECRET_KEY = b')\xd7q%\xaf\xa7\x92\x9bx\xc7<d}\xb6\x9b?[\x9a\xbc\x12)\x9c\xd4\x17'

    BLUEPRINTS = (
        'app.auth:auth',
        'app.front:front',
        'app.main:main',
    )

    EXTENSIONS = (
        'app.extensions:bcrypt',
        'app.extensions:login_manager',
        # 'app.extensions:sentry',
    )

    MONGODB_DB = 'flask_rest_diplay'
    MONGODB_HOST = '192.168.1.123'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = ''
    MONGODB_PASSWORD = ''

    CELERY_BROKER_URL = 'redis://192.168.1.123/1'
    CELERYD_MAX_TASKS_PER_CHILD = 40

    SENTRY_DSN = ''


class DefaultConfig(BaseConfig):

    pass


class TestConfig(BaseConfig):

    MONGODB_DB = 'flask_rest_diplay'
    MONGODB_HOST = '10.1.4.251'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = ''
    MONGODB_PASSWORD = ''
