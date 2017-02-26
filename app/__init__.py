# -*- coding: utf-8 -*-
from os import path

from werkzeug.utils import import_string
from mongoengine import connect
from flask import Flask

from .config import DefaultConfig


__all__ = ['create_app']


def create_app(app_name=None, config=None):

    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = Flask(
        app_name,
        template_folder='templates',
        static_folder='static',
    )

    config_app(app, config)
    config_extensions(app)
    config_blueprints(app)
    config_mongoengine(app)
    configure_logging(app, config)

    return app


def config_app(app, config=None):

    app.config.from_object(DefaultConfig)

    if config:
        app.config.from_object(config)


def config_extensions(app):

    for extension in app.config.get('EXTENSIONS'):
        ext = import_string(extension)
        ext.init_app(app)


def config_blueprints(app):

    for blueprint in app.config.get('BLUEPRINTS'):
        bp = import_string(blueprint)
        app.register_blueprint(bp)


def config_mongoengine(app):

    connect(
        db=app.config['MONGODB_DB'],
        host=app.config['MONGODB_HOST'],
        port=app.config['MONGODB_PORT'],
        username=app.config['MONGODB_USERNAME'],
        password=app.config['MONGODB_PASSWORD'],
        connect=False,
    )


def configure_logging(app, c_n):
    """Configures logging."""

    basedir = path.realpath('.')
    conf = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': ('[%(asctime)s.%(msecs).03d] [pid|%(process)d] '
                           '[%(filename)s:%(lineno)d] [%(levelname)s] %(message)s'),
                'datefmt': '%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
            },
            # 'file': {
            #     'level': 'DEBUG',
            #     'class': 'logging.handlers.RotatingFileHandler',
            #     'filename': path.join(basedir, 'logs/app.log'),
            #     'maxBytes': 10000,
            #     'backupCount': 7,
            #     'formatter': 'standard',
            # },
            # 'deploy': {
            #     'level': 'INFO',
            #     'class': 'logging.handlers.TimedRotatingFileHandler',
            #     'filename': path.join(basedir, 'logs/web.log'),
            #     'when': 'midnight',
            #     'interval': 1,
            #     'backupCount': 7,
            #     'formatter': 'standard',
            # },
        },
        'loggers': {
            'app': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': True
            },
        }
    }
    import logging.config
    logging.config.dictConfig(conf)

    from logging.handlers import SMTPHandler

    if app.config.get("SEND_LOGS"):
        mail_handler = \
            SMTPHandler(
                app.config['MAIL_SERVER'],
                app.config['MAIL_DEFAULT_SENDER'],
                app.config['ADMINS'],
                'application error, no admins specified',
                (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            )

        mail_handler.setLevel(logging.ERROR)
        # mail_handler.setFormatter(formatter)
        app.logger.addHandler(mail_handler)
