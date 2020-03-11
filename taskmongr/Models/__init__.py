# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 10 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
import datetime

import peewee
from peewee import *

Db_Path = 'D:\\taskmongr_home\\db\\taskmongr'
db = peewee.SqliteDatabase(f'{Db_Path}.sqlite',
                           check_same_thread=False)


class BaseModel(peewee.Model):
    isActive = IntegerField(default=2)  # 1: inactive, 2: active
    c_data = DateTimeField(default=datetime.datetime.now())
    u_data = DateTimeField(null=True)

    class Meta:
        database = db
