# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Feb 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""
from setuptools import setup

setup(
    name='taskmongr',
    author='S.M. Sabbir Amin',
    author_email='<sabbiramin.cse11ruet@gmail.com>,<sabbir@rokomari.com>',
    version='0.5.0',
    description='A Simple Task Scheduling and Queueing in Python',
    packages=["taskmongr", "taskmongr.Models", ],
    entry_points={"console_scripts": ["taskmongr = taskmongr.__main__:main"]},
    license='GNU GPL v3 or later',
    install_requires=[
        'Flask == 1.0.2',
        'Flask_Admin == 1.5.4',
        'dill == 0.3.1.1',
        'peewee == 3.5.0',
        'schedule == 0.6.0',
        'setuptools == 39.0.1',

    ],
    package_data={
    },
    data_files=[
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
