# -*- coding: utf-8 -*-

import unittest
import datetime
import json

import flask_testing

from app.config import TestConfig
from app import create_app
from app.models import UserProfile


class BaseTestCase(flask_testing.TestCase):

    def create_app(self):

        return create_app(config=TestConfig)

    def setUp(self):

        now = datetime.datetime.now()
        UserProfile.objects(username='123').update(
            upsert=True,
            set__username='123',
            set__password='$2b$12$YBWO0QXxlYvl1HT9QirnVe9aMdtBylt0QQZRJR.FzNUxdYb3JXVmS',
            last_login=now,
        )
        self.login('123', '15d77445c11f15134e765d6acaea7a68')

    def tearDown(self):

        self.logout()
        UserProfile.objects(username='123').delete()

    def login(self, username, password):

        data = {
            'userName': '123',
            'pwd': '15d77445c11f15134e765d6acaea7a68',
        }
        self._post('/api/sign_in/', data)

    def logout(self):

        self.client.get('/api/logout/')

    def _post(self, url, data={}, query_string={}):

        return self.client.post(
            url, data=json.dumps(data), query_string=query_string, content_type='application/json')


if __name__ == '__main__':
    unittest.main()
