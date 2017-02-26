# -*- coding: utf-8 -*-
from datetime import datetime

from mongoengine import Document, StringField, ListField, IntField,\
    FileField, DateTimeField, DynamicDocument
from flask_login import UserMixin
from .extensions import bcrypt


class UserProfile(DynamicDocument, UserMixin):

    username = StringField()
    password = StringField()
    last_login = DateTimeField()
    update_time = DateTimeField(default=datetime.now)
    query_times = IntField(default=0)
    av_max_times = IntField(default=10)
    company_id = StringField()

    meta = {
        'collection': 'user',
        'indexes': [
            {
                'fields': ['username'],
                'unique': True,
            },
        ],
    }

    def set_password(self, password):

        pwd_hash = bcrypt.generate_password_hash(password)
        self.update(set__password=pwd_hash.decode('utf-8'))

    def check_password(self, password):

        return bcrypt.check_password_hash(self.password, password)


