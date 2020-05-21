# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 4/28/2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

import os


default_path = os.environ.get('USERPROFILE')
default_base = os.environ.get('taskmongr', default=default_path)
# make a home directory
try:
    os.mkdir(os.path.join(default_base,'taskmongr_home'))
except:
    pass
final_path = os.path.join(default_base,'taskmongr_home')
db_name = 'taskmongr.sqlite'
joined_path_name = os.path.join(final_path, db_name)
print(joined_path_name)
print (os.environ)
