'''
simple trigger unit test case  

@author: Huiyugeng
'''

import time

from task import task
from task import task_container

from task.trigger import simple_trigger

from example.jobs import time_job, time_job_listener

container = task_container.TaskContainer()

def get_now():
    time_stamp = time.time()
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))
    return time_now

def test_simple_trigger():
    test_job = time_job.TimeJob()
    test_job_listener = time_job_listener.TimeJobListener()
    
    # repeat 50 times in every 3 seconds
    test_trigger = simple_trigger.SimpleTrigger(50, 3)
    # start delay 5 senconds
    test_trigger.set_delay(5, 0)
    # add task to container
    _task = task.Task('Task', test_job, test_trigger, test_job_listener)
    container.add_task(_task)
    test_job.set_task(_task)
    
    print 'start at %s' % get_now()
    print '---------Start---------'
    container.start_all()
    
    time.sleep(10) # pause container
    print '---------Pause---------'
    container.pasuse_all()
    
    time.sleep(30) # restart container
    print '---------Restart---------'
    container.start_all()
    
    time.sleep(60) # stop container
    print '---------Stop---------'
    container.stop_all()
    
    time.sleep(10) # remove task
    print '---------Remove---------'
    container.remove_task('Task')

test_simple_trigger()
