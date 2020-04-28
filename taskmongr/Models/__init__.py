# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 10 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
import datetime
import os
import peewee
from peewee import *

Db_Path = 'D:\\taskmongr_home\\db\\taskmongr'
default_path = os.environ.get('USERPROFILE')
default_base = os.environ.get('taskmongr', default=default_path)
# make a home directory
try:
    os.mkdir(os.path.join(default_base, 'taskmongr_home'))
except:
    pass
final_path = os.path.join(default_base, 'taskmongr_home')
db_name = 'taskmongr.sqlite'
joined_path_name = os.path.join(final_path, db_name)

db = peewee.SqliteDatabase(joined_path_name,
                           check_same_thread=False)


class BaseModel(peewee.Model):
    isActive = IntegerField(default=2)  # 1: inactive, 2: active
    c_data = DateTimeField(default=datetime.datetime.now())
    u_data = DateTimeField(null=True)

    class Meta:
        database = db
