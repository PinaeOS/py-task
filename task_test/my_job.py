# coding=utf-8

import time

from task.job import job

class MyJob(job.Job):

    def __init__(self):
        pass
    
    def execute(self):
        print 'Hello now is ' + str(time.time())
        