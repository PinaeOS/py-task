# coding=utf-8

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
        