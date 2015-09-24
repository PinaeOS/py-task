'''
simple trigger test case  

@author: Huiyugeng
'''

import time

from task import task
from task import task_container

from task.trigger import simple_trigger

from example.jobs import time_job

container = task_container.TaskContainer()

def get_now():
    time_stamp = time.time()
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))
    return time_now

def test_simple_trigger():
    job1 = time_job.JobA()
    trigger1 = simple_trigger.SimpleTrigger(0, 2)
    task1 = task.Task('TaskA', job1, trigger1)
    container.add_task(task1)
    
    job2 = time_job.JobB()
    trigger2 = simple_trigger.SimpleTrigger(0, 5)
    trigger2.set_delay(5, 0)
    task2 = task.Task('TaskB', job2, trigger2)
    container.add_task(task2)
    
    print 'start at %s' % get_now()
    print '----Start (With Daemon)----'
    container.start_all(True)
    
    time.sleep(11) # pause container
    print '---------Pause All---------'
    container.pasuse_all()
    
    print container.stat_tasks()
    
    time.sleep(10) # restart container
    print '--------Restart All--------'
    container.start_all()
    
    print container.stat_tasks()
    
    time.sleep(11) # stop task
    print '--------Stop Task A--------'
    container.stop('TaskA')
    
    print container.stat_tasks()
    
    time.sleep(10) # restart task
    print '------Start Task A--------'
    container.start('TaskA')
    
    time.sleep(11) # remove task
    print '---------Remove A---------'
    container.remove_task('TaskA')
    
    time.sleep(10) # stop all
    print '---------Stop All---------'
    container.stop_all()

test_simple_trigger()