# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 10 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

from taskmongr import PrimeModels

'''
task_id = {

    func_name 
    com_filename
    d_f
    d_a
    d_k
    execution_status: 1: created, 2: done, 3: abandoned

'''


def db_enqueue(req):
    sts, task = PrimeModels.Task.insert_task_from_req(req)
    response = dict()
    response['flag'] = 1 if sts else 0
    response['task_id'] = task.task_id if sts else ''
    return response


def get_task(req):
    try:
        exe_status = req.args.get('exe_status')
    except Exception as e:
        exe_status = None
    print(exe_status)
    tasks = PrimeModels.Task.get_tasks(execution_status=exe_status)
    models = list()
    for task in tasks:
        t = dict()
        t['task_id'] = task.task_id
        t['func_name'] = task.func_name
        t['py_module'] = task.com_filename
        t['listener'] = task.listener
        t['c_date'] = task.c_data
        t['execution_time'] = task.executing_time
        t['u_date'] = task.u_data

        models.append(t)

    response = dict()
    response['flag'] = 1 if len(models) else 0
    response['_count'] = len(models)
    response['models'] = models
    return response
