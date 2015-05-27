# coding=utf-8
'''
简单触发器

@author: Huiyugeng
'''
import trigger

class SimpleTrigger(trigger.Trigger):

    def __init__(self, repeat_count=0, repeat_interval=1):
        trigger.Trigger.__init__(self, repeat_count, repeat_interval);
        
    def _is_match(self):
        return True
        
