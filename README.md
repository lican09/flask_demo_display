# flask_demo_display
A project display for restful API server,which use Flask and MongoDB.

Flask is a microframework for Python,which has tremendous speed.If you are interested in Flask,there is a display on how to develop a restful API server with Flask and MongoDB.

```
├── app
│   ├── auth
│   │   ├── __init__.py
│   │   ├── parser.py
│   │   └── restful.py
│   ├── config.py
│   ├── constant.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   └── utils.py
│   ├── extensions.py
│   ├── front
│   │   ├── __init__.py
│   │   └── views.py
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   └── piece_into
│   └── models.py
├── celery_app.py
├── conf
│   ├── ansible-playbook.yml
│   ├── master.py
│   ├── nginx.conf
│   ├── release.py
│   ├── supervisord.ini
│   └── uwsgi.ini
├── cover.py
├── manager.py
├── README.md
├── requirements.txt
├── scripts
│   ├── add_user_pass.py
│   ├── add_user.py
│   └── __init__.py
├── task
│   ├── __init__.py
│   └── tasks.py
├── tests
│   └── test_auth.py
└── wsgi.py
```
