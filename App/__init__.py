# -*- coding: utf-8 -*-
# @Time    : 2020-07-29 09:39
# @Author  : Kingcando
# @Software: PyCharm
from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_view


def create_app(env):
    app = Flask(__name__)
    init_view(app)
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(envs.get(env))
    init_ext(app)
    return app
