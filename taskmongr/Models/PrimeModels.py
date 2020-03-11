# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 10 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
import uuid

from taskmongr.Models import *


class Task(BaseModel):

    listener = CharField(null=True)
    task_type = CharField(null=True)
    executing_time = DateTimeField(null=True)

    task_id = CharField(null=True)
    func_name = CharField(null=True)
    com_filename = CharField(null=True)
    d_f = BlobField(null=True)
    d_a = BlobField(null=True)
    d_k = BlobField(null=True)
    execution_status = IntegerField(default=1)

    @classmethod
    def insert_task_from_req(cls, req):
        data = req.get_json()
        try:
            task = Task(
                listener=data.get('listener'),
                task_type=data.get('task_type'),
                executing_time= data.get('executing_time'),
                task_id=str(uuid.uuid4()).replace('-', ''),
                func_name=data.get('func_name'),
                com_filename=data.get('com_filename'),
                d_f=data.get('d_f'),
                d_a=data.get('d_a'),
                d_k=data.get('d_k'),
            )
            task.save()
            return 1, task
        except Exception as e:
            return 0, ""

    @classmethod
    def insert_task_from_data(cls, data):
        print(type(data.get('d_f')))
        try:
            task = Task(
                listener=data.get('listener'),
                task_type=data.get('task_type'),
                executing_time=data.get('executing_time'),
                task_id=str(uuid.uuid4()).replace('-', ''),
                func_name=data.get('func_name'),
                com_filename=data.get('com_filename'),
                d_f=data.get('d_f'),
                d_a=data.get('d_a'),
                d_k=data.get('d_k'),
            )
            task.save()
            return 1, task
        except Exception as e:
            print('Error Saving Task:', e)
            return 0, ""

    @classmethod
    def get_tasks(cls, execution_status=None):
        tasks_collection = list()
        if execution_status:
            for task in Task.select().where(Task.execution_status == execution_status):
                tasks_collection.append(task)
            return tasks_collection
        else:
            for task in Task.select():
                tasks_collection.append(task)

        return tasks_collection

print ()