# coding=utf-8
'''
task container

@author: Huiyugeng
'''

import logging

import task
import task_runner

class TaskContainer(object):

    def __init__(self, max_task = 100):
        self.max_task = max_task
        
        self.tasks = {}
        self.task_runners = {}
    
    def _check_task(self, _task):
        if _task != None and isinstance(_task, task.Task):
            name = _task.get_name()
            if name != None:
                return True
        return False
    
    def add_task(self, _task):
        logging.info('add task: %s' % _task.get_name())
        if self._check_task(_task):
            if  len(self.tasks) < self.max_task:
                self.tasks[_task.get_name()] = _task
            else:
                logging.error('task constainer is FULL, max size is %d' % self.max_task)
        else:
            logging.error('task is NOT instance of task.Task')
    
    def remove_task(self, _task):
        if self._check_task(_task):
            name = _task.get_name()
            if self.task_runners.has_key(name):
                r = self.task_runners.get(name)
                if r != None:
                    r.stop()
                del(self.task_runners[name])
            del(self.tasks[name])
    
    def start(self, name):
        logging.info('start task: %s' % name)
        if name != None:
            if self.task_runners.has_key(name):
                r = self.task_runners.get(name)
            else:
                r = task_runner.TaskRunner(self.tasks.get(name))
                self.task_runners[name] = r
            if r != None:
                r.start_task()
            else:
                logging.error('Task Runner is None')
        else:
            logging.error('No such task: %s' % name)
            
    def start_all(self):
        for name in self.tasks:
            self.start(name)
    
            
    def pause(self, name):
        logging.info('pause task: %s' % name)
        if name != None:
            r = self.task_runners.get(name)
            r.pause_task()
        else:
            logging.error('No such running task %s' % name)
    
    def pasuse_all(self):
        for name in self.tasks:
            self.pause(name)
                
    def stop(self, name):
        logging.info('stop task: %s' % name)
        if name != None:
            r = self.task_runners.get(name)
            r.stop_task()
        else:
            logging.error('No such running task %s' % name)
    
    def stop_all(self):
        for name in self.tasks:
            self.stop(name)
        
