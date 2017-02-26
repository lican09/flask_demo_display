# -*- coding: utf-8 -*-

from flask import Blueprint

from .views import IndexView, AuthView, AuthedView


front = Blueprint('front', __name__)

front.add_url_rule('/signin', view_func=AuthView.as_view('signin'))
front.add_url_rule('/search_into_pieces', view_func=AuthedView.as_view('main'))
front.add_url_rule('/', view_func=IndexView.as_view('index'))
front.add_url_rule('/operator', view_func=IndexView.as_view('operator'))

front.add_url_rule('/authority', view_func=IndexView.as_view('authority'))

front.add_url_rule('/success', view_func=IndexView.as_view('success'))

