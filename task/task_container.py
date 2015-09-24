# coding=utf-8
'''
task container

@author: Huiyugeng
'''
import types
import logging

import task
import task_runner

class TaskContainer(object):

    def __init__(self, max_task = 100):
        self.max_task = max_task
        
        self.tasks = {}
        self.task_runners = {}
        
        self.daemon = task_runner.DaemonTask()
    
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
        if type(_task) == types.StringType:
            name = str(_task)
        elif self._check_task(_task):
            name = _task.get_name()
        
        if name != None:
            if self.task_runners.has_key(name):
                r = self.task_runners.get(name)
                if r != None:
                    r.stop_task()
                del(self.task_runners[name])
            del(self.tasks[name])
            
    def get_task(self, name):
        if name != None:
            return self.tasks.get(name)
        return None
    
    def get_tasks(self):
        return self.tasks
    
    def stat_tasks(self):
        
        status = {-1 : 'exception', 0 : 'stop', 1 : 'running', 2 : 'pause'}
        
        status_stat = {'exception' : 0, 'stop' : 0, 'running' : 0, 'pause' : 0}
        
        for name in self.tasks:
            try:
                flag = self.tasks.get(name).get_status()
                status_stat[status[flag]] = status_stat[status[flag]] + 1
            except:
                pass
                
        return status_stat  
    
    def _new_task_runner(self, name):
        r = None
        _task = self.tasks.get(name)
        if _task != None and isinstance(_task, task.Task):
            r = task_runner.TaskRunner(_task)
            self.task_runners[name] = r
        else:
            logging.error('task %s is NOT instance of task.Task' % name)
            
        return r
    
    def start(self, name):
        
        logging.info('start task: %s' % name)
        if name != None:
            if self.task_runners.has_key(name):
                r = self.task_runners.get(name)
            else:
                r = self._new_task_runner(name)
                
            if r != None:
                if r.started is True and r.stop_flag is True:
                    r = self._new_task_runner(name)
                r.start_task()
            else:
                logging.error('Task Runner is NONE')
        else:
            logging.error('task name is NONE')
            
    def start_all(self, daemon = False):
        for name in self.tasks:
            self.start(name)
        if daemon:
            self.daemon.start_task()
    
            
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
        self.daemon.stop_task()
        
