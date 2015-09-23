# coding=utf-8
'''
task runner

@author: Huiyugeng
'''
import time
import threading
import logging

from job import job, job_listener
from trigger import trigger

class TaskRunner(threading.Thread):

    def __init__(self, _task):
        
        threading.Thread.__init__(self)
        
        self._task = _task

        self.name = _task.get_name()
        self.job = _task.get_job()
        self.job_listener = _task.get_job_listener()
        self.trigger = _task.get_trigger()
        
        self.started = False
        self.stop_flag = True
        self.pause_flag = False
            
        self.interval = 1
            
        if self.job == None or isinstance(self.job, job.Job) is False:
            raise AttributeError('Job is None')
        if self.trigger == None or isinstance(self.trigger, trigger.Trigger) is False:
            raise AttributeError('Trigger is None')
        if self.job_listener != None and isinstance(self.job_listener, job_listener.JobListener):
            self.job_listener.init()

    
    def run(self):
        start_delay = self.trigger._get_start_delay()
        if start_delay > 0:
            time.sleep(start_delay)
            
        while self.stop_flag is False:
            if self.pause_flag is False and self.trigger._is_match():
                self.trigger._inc_execute_count()  # executer counter
                try:
                    if self.job_listener != None and isinstance(self.job_listener, job_listener.JobListener):
                        self.job_listener.before_execute()
                        
                    self.job.execute()  # execute job
                    
                    if self.job_listener != None and isinstance(self.job_listener, job_listener.JobListener):
                        self.job_listener.after_execute()
                        
                except Exception, ex:
                    self._task.set_status(-1)
                    logging.error('Execute task: %s Exception: %s' % (self.name, ex.message))
                    
            if self.trigger._is_finish() is False:
                time.sleep(self.interval)
            else:
                break
        
        end_delay = self.trigger._get_end_delay()
        if end_delay > 0:
            time.sleep(end_delay)
        if self.job_listener != None and isinstance(self.job_listener, job_listener.JobListener):
                self.job_listener.destory()
    
    def start_task(self):
        self.started = True
        if self.pause_flag is True:
            self.pause_flag = False
            self._task.set_status(1)  
        elif self.trigger != None and isinstance(self.trigger, trigger.Trigger):

            self.interval = self.trigger._get_repeat_interval()
            
            if self.stop_flag is True:
                try:
                    self._task.set_status(1)
                    self.stop_flag = False
                    self.start()
                except Exception, ex:
                    self._task.set_status(-1)
                    logging.error('Start task: %s Exception: %s' % (self.name, ex.message))
                    
    def stop_task(self):
        self.stop_flag = True
        self._task.set_status(0)
        
    def pause_task(self):
        self.pause_flag = True
        self._task.set_status(2)

class DaemonTask(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name = 'Daemon-Task')
        self.stop_flag = False
    
    def run(self):
        while self.stop_flag is False:
            time.sleep(1)
    
    def start_task(self):
        self.start()
        
    def stop_task(self):
        self.stop_flag = True
        