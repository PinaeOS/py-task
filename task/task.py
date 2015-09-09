# coding=utf-8
'''
task

@author: Huiyugeng
'''

import time

from job import job_listener

class Task():
    
    def __init__(self, name, job, trigger, job_listener = None):
        self.serial = str(time.time()) + name
        self.name = name
        self.job = job
        self.job_listener = job_listener
        self.trigger = trigger
        
        self.status = 0 # -1:exception, 0:stop, 1:running, 2:pause
    
    def get_name(self):
        return self.name
    
    def get_serial(self):
        return self.serial
    
    def set_status(self, status):
        self.status = status
        if self.job_listener != None and isinstance(self.job_listener, job_listener.JobListener):
            self.job_listener.status_changed(status)
        
    def get_status(self):
        return self.status
    
    def get_job(self):
        return self.job
    
    def get_job_listener(self):
        return self.job_listener
    
    def get_trigger(self):
        return self.trigger
    
