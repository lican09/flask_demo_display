# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api
from app.models import UserProfile
from app.extensions import login_manager
from . import restful


auth = Blueprint('auth', __name__)
auth_wrap = Api(auth)


@login_manager.user_loader
def load_user(user_id):
    return UserProfile.objects(id=user_id).first()


@login_manager.unauthorized_handler
def unauthorized():
    from app.core.utils import make_response
    from app.constant import const
    return make_response(status=const.AUTH_ERROR)

auth_wrap.add_resource(restful.SignIn, '/api/sign_in/')
auth_wrap.add_resource(restful.SignOut, '/api/logout/')
# auth_wrap.add_resource(restful.ChangePwd, '/api/change_pwd/')
