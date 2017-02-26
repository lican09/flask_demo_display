# -*- coding: utf-8 -*-

from flask_restful import reqparse


user_parser = reqparse.RequestParser(bundle_errors=True)
user_parser.add_argument("username", type=str, required=True)
user_parser.add_argument("password", type=str, required=True)

pwd_parser = reqparse.RequestParser(bundle_errors=True)
pwd_parser.add_argument("newPwd", type=str, required=True)
pwd_parser.add_argument("oldPwd", type=str, required=True)
pwd_parser.add_argument("username", type=str, required=True)
