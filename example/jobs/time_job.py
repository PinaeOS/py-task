# coding=utf-8

import time

from task.job import job

class MyJob(job.Job):

    def __init__(self):
        pass
    
    def execute(self):
        time_stamp = time.time()
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))
        
        print 'Now is ' + time_now
        