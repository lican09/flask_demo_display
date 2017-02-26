
from flask import jsonify

from app.constant import const


def make_response(data=None, status=const.SUCCESS):

    return {
        'data': data,
        'code': status,
        'msg': const.MSG.get(status)
    }