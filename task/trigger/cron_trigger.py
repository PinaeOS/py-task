# coding=utf-8
'''
cron trigger

@author: Huiyugeng
'''
import datetime 

import trigger

class CronTrigger(trigger.Trigger):

    def __init__(self, cron):
        trigger.Trigger.__init__(self, 0, 1);
        self.cron = cron
    
    def _is_match(self):
        parser = CronParser(self.cron)
        
        _date = datetime.date.today()
        _time = datetime.datetime.now()
        
        return parser._is_match(_date, _time)
    
class CronParser():

    def __init__(self, cron):
        cron_item = cron.split(' ')
        if len(cron_item) == 6 or len(cron_item) == 7:
            
            self.second_set = self._parse_integer(cron_item[0], 0, 59)
            self.minute_set = self._parse_integer(cron_item[1], 0, 59)
            self.hour_set = self._parse_integer(cron_item[2], 0, 23)
            self.day_of_month_set = self._parse_integer(cron_item[3], 1, 31)
            self.month_set = self._parse_month(cron_item[4])
            self.day_of_week_set = self._parse_day_of_week(cron_item[5])
            if len(cron_item) == 7:
                self.year_set = self._parse_integer(cron_item[6], 1970, 2100)

    def _parse_integer(self, value, min_val, max_val):
        result = []
        
        range_items = []
        if ',' in value:
            range_items = value.split(',')
        else:
            range_items.append(value)

        for range_item in range_items:
            temp_result = []

            interval = 1

            if '/' in range_item:
                temp = range_item.split('/')
                range_item = temp[0]
                interval = int(temp[1])

                if interval < 1:
                    interval = 1
            
            if '*' in range_item:
                temp_result.extend(self._add_to_set(min_val, max_val))
            elif '-' in range_item:
                item = range_item.split('-')
                temp_result.extend(self._add_to_set(int(item[0]), int(item[1])))
            else:
                temp_result.append(int(range_item))
            
            count = 0
            for item in temp_result:
                if count % interval == 0:
                    result.append(item)
                count = count + 1

        return result

    def _add_to_set(self, start, end):
        result = [i for i in range(start, end + 1)]
        return result

    def _parse_month(self, value):
        months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        for i in range(0, 12):
            value = value.replace(months[i], str(i + 1))
        return self._parse_integer(value, 1, 12);
    
    def _parse_day_of_week(self, value):
        day_of_weeks = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
        for i in range(0, 7):
            value = value.replace(day_of_weeks[i], str(i + 1));
        return self._parse_integer(value, 1, 7);
    
    def _is_match(self, _date, _time):
        
        # In Python datetime's weekday Monday is 0 and Sunday is 6
        day_of_week = _date.weekday() + 1  
        
        result = True and \
                    _time.second in self.second_set and \
                    _time.minute in self.minute_set and \
                    _time.hour in self.hour_set and \
                    _date.day in self.day_of_month_set and \
                    _date.month in self.month_set and \
                    _date.year in self.year_set and \
                    day_of_week in self.day_of_week_set
        
        return result
