# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 10 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

import datetime



at = datetime.datetime(2020,3,10,22,10)
print (at)
print (datetime.datetime.today())
if at<datetime.datetime.now():
    print ('Yes')