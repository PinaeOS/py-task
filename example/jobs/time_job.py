# coding=utf-8

import time

from task.job import job

class TimeJob(job.Job):

    def __init__(self):
        pass
    
    def set_task(self, _task):
        self._task = _task
        
    def execute(self):
        time_stamp = time.time()
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))
        
        print 'Now is ' + time_now + ' and Status is ' + str(self._task.get_status())
        