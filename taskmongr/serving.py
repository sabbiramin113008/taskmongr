# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 11 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
from flask_admin import Admin

from taskmongr.Models.AdminViews import *
from taskmongr.Models.PrimeModels import *
from taskmongr.application import app


def run_server():
    import logging

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    admin = Admin(app, name='TaskMongr')

    admin.add_view(TaskAdmin(Task))
    app.run(
        host='localhost',
        port=4000,
        debug=True
    )
