# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 10 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
from datetime import datetime

from taskmongr import Task, ScheduledTask


@Task()
def print_my_name():
    import os
    print(os.name)


@ScheduledTask(at=datetime(2020, 3, 11, 14, 20))
def print_1_to_100():
    for i in range(1, 101):
        print(i)


if __name__ == '__main__':
    print_my_name()
    print_1_to_100()
