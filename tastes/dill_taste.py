# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 10 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
import dill


def print_me():
    import os
    print ('OS Name:',os.name)


d_f = dill.dumps(print_me())
func_after = dill.loads(d_f)
print (func_after)