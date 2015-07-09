'''
cron parser unit test case  

@author: Huiyugeng
'''

import datetime

import unittest
from task.trigger import cron_trigger

class CronParserTest(unittest.TestCase):
    
    def test_parse_cron(self):
        
        parser = cron_trigger.CronParser('0-59/5 15-35 * * * * *')
        _date = datetime.datetime(2015, 5, 12, 20, 20, 10)
        self.assertEqual(parser._is_match(_date.date(), _date.time()), True)
        
        parser = cron_trigger.CronParser('0-59/5 15-35 20 10-20 MAY * *')
        _date = datetime.datetime(2015, 5, 12, 20, 20, 10)
        self.assertEqual(parser._is_match(_date.date(), _date.time()), True)
        
        parser = cron_trigger.CronParser('0-59/5 15-35 20 * MAY SUN *')
        _date = datetime.datetime(2015, 5, 17, 20, 20, 10)
        self.assertEqual(parser._is_match(_date.date(), _date.time()), True)
        
        parser = cron_trigger.CronParser('0-59/5 15-35 20 * MAY SUN 2013-2015')
        _date = datetime.datetime(2015, 5, 17, 20, 20, 10)
        self.assertEqual(parser._is_match(_date.date(), _date.time()), True)