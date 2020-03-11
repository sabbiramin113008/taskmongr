# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 10 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
import datetime
import time

import dill
import schedule

from taskmongr.Models import PrimeModels


def batch_execute():
    tasks = PrimeModels.Task.get_tasks(execution_status=1)
    for task in tasks:
        # checking whether it is a regular task or ScheduledTask
        if task.task_type == 'regular':
            f_after = dill.loads(task.d_f)
            a_after = dill.loads(task.d_a)
            k_after = dill.loads(task.d_k)
            try:
                value = f_after(*a_after, **k_after)
                task.execution_status = 2
                task.executing_time = datetime.datetime.now()
                task.u_data = datetime.datetime.now()
                task.save()
                print('Task ID: {}: Execution Status: {}'
                      .format(task.task_id, task.execution_status))
            except Exception as e:
                task.execution_status = 3
                task.executing_time = datetime.datetime.now()
                task.u_data = datetime.datetime.now()
                task.save()
                print('Task ID: {}: Execution Status: {}, Error: {}'
                      .format(task.task_id, task.execution_status, e))
        elif (task.task_type == 'scheduled') \
                and (task.executing_time < datetime.datetime.now()):
            f_after = dill.loads(task.d_f)
            a_after = dill.loads(task.d_a)
            k_after = dill.loads(task.d_k)
            try:
                value = f_after(*a_after, **k_after)
                task.execution_status = 2
                task.u_data = datetime.datetime.now()
                task.save()
                print('Task ID: {}: Execution Status: {}'
                      .format(task.task_id, task.execution_status))
            except Exception as e:
                task.execution_status = 3
                task.u_data = datetime.datetime.now()
                task.save()
                print('Task ID: {}: Execution Status: {}, Error: {}'
                      .format(task.task_id, task.execution_status, e))


schedule.every(1).minutes.do(batch_execute)

while True:
    time.sleep(1)
    schedule.run_pending()
