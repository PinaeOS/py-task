# coding=utf-8
'''
task runner

@author: Huiyugeng
'''
import time
import threading

import task
from job import job
from trigger import trigger

class TaskRunner(threading.Thread):

    def __init__(self, _task):
        
        threading.Thread.__init__(self)
        
        if _task != None and isinstance(_task, task.Task):

            self.job = _task.get_job()
            self.trigger = _task.get_trigger()
            
            self.stop_flag = False
            self.pause_flag = False
            
            self.interval = 1
            
            if self.job == None or isinstance(self.job, job.Job) == False:
                raise AttributeError('Job is None')
            if self.trigger == None or isinstance(self.trigger, trigger.Trigger) == False:
                raise AttributeError('Trigger is None')

    
    def run(self):
        while self.stop_flag == False:
            if self.pause_flag == False and self.trigger._is_match():
                self.trigger._inc_execute_count()  # executer counter
                self.job.execute()  # execute job
            
            if self.trigger._is_finish() == False:
                time.sleep(self.interval)
    
    def start_task(self):
        if self.pause_flag == True:
            self.pause_flag = False
        
        elif self.trigger != None and isinstance(self.trigger, trigger.Trigger):
            
            self.start_delay = self.trigger._get_start_delay()
            self.interval = self.trigger._get_repeat_interval()
            
            if self.stop_flag == False:
                self.start()
            
    def stop_task(self):
        self.stop_flag = True
        
    def pause_task(self):
        self.pause_flag = True
        
