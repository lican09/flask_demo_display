# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import render_template, redirect
from flask_login import login_required, current_user


class AuthedView(MethodView):

    def get(self, *args, **kwargs):
        if current_user.is_authenticated:
            return render_template('modules/core/frame.tpl.html')
        else:
            return redirect('/signin')


class IndexView(MethodView):

    def get(self, *args, **kwargs):

        if current_user.is_authenticated:
            return redirect('/search_into_pieces')
        else:
            return redirect('/signin')


class AuthView(MethodView):

    def get(self, *args, **kwargs):

        return render_template('modules/core/frame.tpl.html')