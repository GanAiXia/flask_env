# -*- coding: utf-8 -*-
# @Time    : 2020-07-29 09:41
# @Author  : Kingcando
# @Software: PyCharm
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

models = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    models.init_app(app)
    migrate.init_app(app, models)
