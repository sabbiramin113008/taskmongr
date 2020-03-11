# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 10 Mar 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

import datetime

at = datetime.datetime(2020, 3, 10, 22, 10)
print(at)
print(datetime.datetime.today())
if at < datetime.datetime.now():
    print('Yes')


class TimeStamp():
    def __init__(self, year,
                 month,
                 day,
                 hour=0,
                 minute=0,
                 second=0
                 ):
        self.year = year
        self.month = month
        self.day = day,
        self.hour = hour,
        self.minute = minute,
        self.second = second

        self.date_time_const = datetime.datetime(self.year,
                                                 self.month,
                                                 self.day,
                                                 self.hour,
                                                 self.minute,
                                                 self.second)
