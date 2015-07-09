# coding=utf-8
'''
date helper

@author: Huiyugeng
'''
import datetime

def next_seconds(seconds = 1):
    now = datetime.datetime.now()
    time_delta = datetime.timedelta(seconds=seconds)
    
    return now + time_delta

def next_minutes(minutes = 1):
    now = datetime.datetime.now()
    time_delta = datetime.timedelta(minutes=minutes)
    
    return now + time_delta

def next_hours(hours = 1):
    now = datetime.datetime.now()
    time_delta = datetime.timedelta(hours=hours)
    
    return now + time_delta

def today(hours = 0, minutes = 0, seconds = 0):
    _date = datetime.date.today()
    
    return datetime.datetime(_date.year, _date.month, _date.day, 
                             hours, minutes, seconds)

def tomrrow(hours = 0, minutes = 0, seconds = 0):
    return next_days(1, hours, minutes, seconds)

def next_days(days = 1, hours = 0, minutes = 0, seconds = 0):
    now = datetime.datetime.now()
    time_delta = datetime.timedelta(days = days)
    
    _date = now + time_delta
    return datetime.datetime(_date.year, _date.month, _date.day, 
                             hours, minutes, seconds)
