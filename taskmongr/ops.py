# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 10 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
import os
from functools import wraps

import dill

from taskmongr.Models import PrimeModels


def get_filename(file_path_name):
    if os.name == 'nt':
        file_name = file_path_name.split('/')[-1]
    else:
        file_name = file_path_name.split('\\')[-1]
    print(file_name)
    return file_name


def Task(execute='later', listener='Sentinel'):
    '''
    
    :param execute: 
    :param listener: 'default' the queue to the listener
    :return: 
    '''

    def decorate_task(func):
        @wraps(func)
        def wrapper_task(*args, **kwargs):
            func_name = func.__name__
            file_path_name = func.__code__.co_filename
            com_filename = get_filename(file_path_name=file_path_name)

            # print('Func Name: {}\nFile Path Name: {},'.format(func_name, file_path_name))

            # The Whole execution point, based on the logic
            if execute == 'now':
                print('Execution Now.....')
                try:
                    value = func(*args, **kwargs)

                    for k, v in kwargs.items():
                        print(k, v)
                    return value

                except Exception as e:
                    print('Error: ', e)
                    raise e
            elif execute == 'later':
                # Time to pickle the function

                d_f = dill.dumps(func)
                d_a = dill.dumps(args)
                d_k = dill.dumps(kwargs)

                d_obj = dict()
                d_obj['func_name'] = func_name
                d_obj['com_filename'] = com_filename
                d_obj['d_f'] = d_f
                d_obj['d_a'] = d_a
                d_obj['d_k'] = d_k
                d_obj['listener'] = listener
                d_obj['task_type'] = 'regular'
                d_obj['executing_time'] = None

                print('d_obj:', d_obj)

                sts, task = PrimeModels.Task.insert_task_from_data(d_obj)
                response = dict()
                response['flag'] = 1 if sts else 0
                response['task_id'] = task.task_id if sts else ''
                print('response: ', response)
                return response

        return wrapper_task

    return decorate_task


def ScheduledTask(at, listener='Sentinel'):
    '''
    
    :param at: (datatime) datetime  
    :param retry_on_error: (int) 0
    :return: 
    '''

    def decorated_task(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            file_path_name = func.__code__.co_filename
            com_filename = get_filename(file_path_name=file_path_name)
            d_f = dill.dumps(func)
            d_a = dill.dumps(args)
            d_k = dill.dumps(kwargs)

            d_obj = dict()
            d_obj['func_name'] = func_name
            d_obj['com_filename'] = com_filename
            d_obj['d_f'] = d_f
            d_obj['d_a'] = d_a
            d_obj['d_k'] = d_k
            d_obj['listener'] = listener
            d_obj['task_type'] = 'scheduled'
            d_obj['executing_time'] = at

            print('d_obj:', d_obj)

            sts, task = PrimeModels.Task.insert_task_from_data(d_obj)
            response = dict()
            response['flag'] = 1 if sts else 0
            response['task_id'] = task.task_id if sts else ''
            print('response: ', response)
            return response

        return wrapper

    return decorated_task


def RepeatedTask(every):
    pass
















    # func_after = dill.loads(d_f)
    # args_after = dill.loads(d_a)
    # kwargs_after = dill.loads(d_k)
    # value = func_after(*args_after, **kwargs_after)
