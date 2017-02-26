import hashlib
import flask_bcrypt
import pymongo
from pymongo.errors import DuplicateKeyError

# 数据库配置
ip = '192.168.1.123'
database = 'flask_rest_display'
collection = 'user'

# 账号
username = 'test1'
# 密码
password = 'test@'
# 密码加密盐值
salt = 'asdf'

db = pymongo.MongoClient(ip)[database]


def get_password(password):
    v = (password + salt).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(v)
    pass_hash = md5.hexdigest()
    print(pass_hash)
    return pass_hash


def add_user(username, pass_hash, **kwargs):
    try:
        db[collection].insert({
            'username': username,
            'password': flask_bcrypt.generate_password_hash(pass_hash),
            # 'is_active': True,
        })
        print('inserted {}:{}  username:{}: pass:{}'
              .format(ip, collection, username, password))
    except DuplicateKeyError:
        print('already exist!')
        db[collection].update(
            {
                'username': username,
            },
            {
                '$set':
                {
                    'password': flask_bcrypt.generate_password_hash(pass_hash),
                    # 'is_active': True,
                }
            }
        )
        print('updated {}:{}  username:{}: pass:{}'
              .format(ip, collection, username, password))
    print('completed OK!')


if __name__ == "__main__":
    pass_hashed = get_password(password)
    add_user(username=username, pass_hash=pass_hashed)
