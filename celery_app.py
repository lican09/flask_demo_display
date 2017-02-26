# -*- coding: utf-8 -*-
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab
from mongoengine import connect

from app.config import DefaultConfig
from app.constant import const


celery = Celery(
    __name__,
    broker=DefaultConfig.CELERY_BROKER_URL,
    # backend=DefaultConfig.CELERY_RESULT_BACKEND,
    include=['task.tasks'],
)

celery.config_from_object(DefaultConfig)

celery.conf.update(
    CELERYBEAT_SCHEDULE={
        'retry_monitor': {
            'task': 'task.retry',
            'schedule': timedelta(seconds=20),
            'options': {
                'queue': const.RETRY_INPUT_QUEUE,
            },
        },
        'image_monitor': {
            'task': 'task.image_clear',
            # 'schedule': crontab(hour=5, minute=30),
            'schedule': timedelta(hours=1),
            'options': {
                'queue': const.IMAGE_MONITOR_QUEUE,
            }
        },
    },
)

connect(
    db=DefaultConfig.MONGODB_DB,
    alias='default',
    host=DefaultConfig.MONGODB_HOST,
    port=DefaultConfig.MONGODB_PORT,
    username=DefaultConfig.MONGODB_USERNAME,
    password=DefaultConfig.MONGODB_PASSWORD,
    connect=False,
)
