# -*- coding: utf-8 -*-
# @Time    : 2020-07-29 09:39
# @Author  : Kingcando
# @Software: PyCharm
from App.views.home import home


def init_view(app):
    app.register_blueprint(home)
