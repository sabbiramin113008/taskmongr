# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 10 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

from taskmongr.Models import PrimeModels


def create_db():
    try:
        PrimeModels.Task.create_table()
    except Exception as e:
        print('Error Creating Table: ', e)

create_db()