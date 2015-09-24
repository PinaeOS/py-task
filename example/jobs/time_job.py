# coding=utf-8

import time

from task.job import job

class TimeJob(job.Job):

    def __init__(self):
        pass
        
    def execute(self):
        time_stamp = time.time()
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))
        
        print 'Time-Job : Now is ' + time_now
        
        return False
    
class TimeJobWithException(job.Job):

    def __init__(self):
        pass
        
    def execute(self):
        time_stamp = time.time()
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))
        
        print 'Time-Job (With Exception) : Now is ' + time_now
        
        raise RuntimeError('Throws exception from Job')

from task.job import job_listener

class TimeJobListener(job_listener.JobListener):
    
    def __init__(self, name):
        self.name = name
    
    def init(self):
        print '%s init' % self.name
    
    def before_execute(self):
        print '%s before-execute' % self.name
    
    def after_execute(self):
        print '%s after-execute' % self.name
    
    def destory(self):
        print '%s destory' % self.name
    
    def status_changed(self, status):
        print '%s status: %s' % (self.name, str(status))
    
    def execute_fail(self):
        print '%s fail' % self.name
    
    def execute_exception(self, exception):
        print '%s exception: %s' % (self.name, exception.message)

class JobA(job.Job):

    def __init__(self):
        pass
        
    def execute(self):
        time_stamp = time.time()
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))
        
        print 'JobA : Now is ' + time_now

class JobB(job.Job):
    
    def execute(self):
        time_stamp = time.time()
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))
        
        print 'JobB : Now is ' + time_now