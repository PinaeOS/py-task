# coding=utf-8
'''
task runner

@author: Huiyugeng
'''

import threading

import task
from job import job
from trigger import trigger

class TaskRunner(object):

    def __init__(self, _task):
        if _task != None and isinstance(_task, task.Task):

            self.job = _task.get_job()
            self.trigger = _task.get_trigger()
            
            self.stop_flag = False
            self.pause_flag = False
            
            if self.job == None or isinstance(self.job, job.Job) == False:
                raise AttributeError('Job is None')
            if self.trigger == None or isinstance(self.trigger, trigger.Trigger) == False:
                raise AttributeError('Trigger is None')

        
    def __time(self, interval, fun, arg=()):
        t = threading.Timer(interval, fun, arg)
        t.start()
    
    def __task(self):

        if self.stop_flag == False and self.pause_flag == False and self.trigger._is_match():
            self.trigger._inc_execute_count()  # executer counter
            self.job.execute()  # execute job
            
        if self.stop_flag == False and self.trigger._is_finish() == False:
            self.__time(self.interval, self.__task)
    
    def start(self):
        if self.pause_flag == True:
            self.pause_flag = False
        
        elif self.trigger != None and isinstance(self.trigger, trigger.Trigger):
            
            self.start_delay = self.trigger._get_start_delay()
            self.interval = self.trigger._get_repeat_interval()
            
            if self.stop_flag == False:
                self.__time(self.start_delay, self.__task)
            
    def stop(self):
        self.stop_flag = True
        
    def pause(self):
        self.pause_flag = True
        
