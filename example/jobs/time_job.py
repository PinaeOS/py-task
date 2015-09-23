# coding=utf-8

import time

from task.job import job

class TimeJob(job.Job):

    def __init__(self):
        pass
        
    def execute(self):
        time_stamp = time.time()
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))
        
        print 'JobA : Now is ' + time_now

from task.job import job_listener

class TimeJobListener(job_listener.JobListener):
    
    def init(self):
        print 'Time-job init'
    
    def before_execute(self):
        print 'Time-job before-execute'
    
    def after_execute(self):
        print 'Time-job after-execute'
    
    def destory(self):
        print 'Time-job destory'
    
    def status_changed(self, status):
        print 'Time-job status: %s' % str(status)

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