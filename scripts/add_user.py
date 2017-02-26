import hashlib
import flask_bcrypt
from app.models import UserProfile


def insert(username, password):
    obj = UserProfile.objects(username=username).first()
    print("账号：{}".format(username))
    pass_hashed = get_password(password)
    # pass_save = flask_bcrypt.generate_password_hash(pass_hashed)

    if obj:
        obj.set_password(password=pass_hashed)
    else:
        obj = UserProfile(username=username).save()
        obj.set_password(password=pass_hashed)
    print("密码:{}".format(password))
    return 0


def get_password(password):
    # 密码加密盐值
    salt = 'asdfasdf'
    v = (password + salt).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(v)
    pass_hash = md5.hexdigest()
    print(pass_hash)
    return pass_hash
