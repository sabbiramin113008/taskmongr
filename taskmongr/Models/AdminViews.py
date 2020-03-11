# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 11 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
from datetime import date

from flask_admin.contrib.peewee import ModelView
from flask_admin.model import typefmt


def format_date(view, value):
    return value.strftime('%a %I:%M %p, %b %d, %Y')


MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
MY_DEFAULT_FORMATTERS.update({
    type(None): typefmt.null_formatter,
    date: format_date
})


def make_execution_status(tok):
    if str(tok) == '1':
        return 'created'
    elif str(tok) == '2':
        return 'done'
    elif str(tok) == '3':
        return 'error'


class TaskAdmin(ModelView):
    column_type_formatters = MY_DEFAULT_FORMATTERS

    can_view_details = True
    can_edit = True
    can_export = True
    can_set_page_size = True
    page_size = 50
    can_create = False
    column_formatters = {
        'execution_status': lambda v, c, m, p: make_execution_status(m.execution_status)

    }
    column_exclude_list = ['id', 'isActive', 'u_data', 'py_filepath',
                           'd_f', 'd_a', 'd_k',
                           ]
    column_filters = ['task_type', 'c_data', 'u_data',
                      'task_id', 'listener', 'executing_time',
                      'func_name', 'com_filename', 'execution_status'
                      ]
    column_export_exclude_list = ['d_f','d_k','d_a']
