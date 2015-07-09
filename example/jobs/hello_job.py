# coding=utf-8

import time

from task.job import job

class HelloJob(job.Job):

    def __init__(self):
        pass
    
    def execute(self):
        print 'Just say Hello at %s' % str(time.time())
        