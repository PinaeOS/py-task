# coding=utf-8
'''
任务调度

@author: Huiyugeng
'''

class Task():
    
    def __init__(self, name, job, trigger):
        self.name = name
        self.job = job
        self.trigger = trigger
    
    def get_name(self):
        return self.name
    
    def get_serial(self):
        return self.serial
        
    def get_status(self):
        return self.status
    
    def get_job(self):
        return self.job
    
    def get_trigger(self):
        return self.trigger
    
