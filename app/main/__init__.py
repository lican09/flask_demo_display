# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api


main = Blueprint('main', __name__)
main_wrap = Api(main)
