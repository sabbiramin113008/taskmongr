# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 10 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

from taskmongr import Task


@Task(execute='later')
def print_my_name():
    import os
    print(os.name)


if __name__ == '__main__':
    print_my_name()
