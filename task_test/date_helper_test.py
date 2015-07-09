'''
date helper unit test case  

@author: Huiyugeng
'''

import unittest

import datetime
from task.trigger import date_helper

class DateHelperTest(unittest.TestCase):
    
    def test_date_helper(self):
        '''next_seconds test'''
        _time = date_helper.next_seconds(10)
        _now = datetime.datetime.now()
        delta = (_time - _now).seconds
        self.assertEqual(int(round(delta)), 10)
        
        '''next_minutes test'''
        _time = date_helper.next_minutes(10)
        _now = datetime.datetime.now()
        delta = (_time - _now).seconds
        self.assertEqual(int(round(delta)), 10 * 60)
        
        '''next_hours test'''
        _time = date_helper.next_hours(10)
        _now = datetime.datetime.now()
        delta = (_time - _now).seconds
        self.assertEqual(int(round(delta)), 10 * 60 * 60)
        
        '''today test'''
        _time = date_helper.today()
        _now = datetime.date.today()
        self.assertEqual(_now.year, _time.year)
        self.assertEqual(_now.month, _time.month)
        self.assertEqual(_now.day, _time.day)
        
        '''next_days test'''
        _now = datetime.datetime.now()
        _time = date_helper.next_days(3, _now.hour, _now.minute, _now.second)
        delta = (_time - _now).days
        self.assertEqual(int(round(delta)), 2)
        
        