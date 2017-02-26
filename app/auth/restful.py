# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask_login import login_user, logout_user, login_required

from .parser import user_parser, pwd_parser
from app.constant import const
from app.models import UserProfile
from app.core.utils import make_response


class SignIn(Resource):
    """登录"""

    def post(self):
        req = user_parser.parse_args(strict=True)
        user_obj = UserProfile.objects(username=req["username"]).first()
        if user_obj and user_obj.check_password(req["password"]):
            login_user(user_obj, remember=True)
            return make_response()
        else:
            return make_response(status=const.AUTH_ERROR)


class SignOut(Resource):
    """退出"""
    @login_required
    def get(self):
        logout_user()
        return make_response()


class ChangePwd(Resource):
    """修改密码"""
    @login_required
    def put(self):
        req = pwd_parser.parse_args(strict=True)
        user_obj = UserProfile.objects(username=req["userName"]).first()
        if user_obj and user_obj.check_password(req["oldPwd"]):
            user_obj.set_password(req["newPwd"])
            return make_response()
        else:
            return make_response(status=const.AUTH_ERROR)
