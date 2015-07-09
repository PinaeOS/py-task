'''
simple trigger unit test case  

@author: Huiyugeng
'''

import time

from task import task
from task import task_container

from task.trigger import simple_trigger

from example.jobs import time_job

container = task_container.TaskContainer()

def test_simple_trigger():
    test_job = time_job.MyJob()
    
    # repeat 50 times in every 3 seconds
    test_trigger = simple_trigger.SimpleTrigger(50, 3)
    # start delay 5 senconds
    test_trigger.set_delay(5, 0)
    # add task to container
    container.add_task(task.Task('Task', test_job, test_trigger))
    
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
