# -*- coding:utf-8 -*-
import requests

from celery_app import celery


@celery.task(name='send_sms')
def send_sms(phone_num, verify_code):

    req_dict = {
        "apikey": "123sdfasdf234wdw3rwrsefasdfaef",
        "mobile": phone_num,
        "content": "【demo】您的验证码是{}，验证码有效时间为5分钟。".format(verify_code)
    }
    r = requests.post(
        'https://api.dingdongcloud.com/v1/sms/sendyzm',
        data=req_dict
    )
    print(r.json())
    print("send vrify code '{}' to mobile {}".format(verify_code, phone_num))
