# -*- coding: utf-8 -*-
# @Time    : 2020-07-29 09:42
# @Author  : Kingcando
# @Software: PyCharm
import random

from flask import Blueprint, render_template
from App.models import models, User

home = Blueprint('home', __name__)


@home.route('/')
@home.route('/index')
def index():

    return render_template("index.html")


@home.route('/createdb')
def create_db():
    models.create_all()

    return 'Create Table Success!'


@home.route('/adduser')
def add_user():
    user = User()
    user.username = "kingcando%d" % (random.randint(1, 1000))
    user.userage = random.randint(1, 100)
    models.session.add(user)
    models.session.commit()

    return 'Insert Success!'


@home.route('/dropdb')
def drop_db():
    models.drop_all()

    return 'Drop Tables Success!'
