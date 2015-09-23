'''
job listener test case  

@author: Huiyugeng
'''

import time

from task import task
from task import task_container

from task.trigger import simple_trigger
from example.jobs import time_job

container = task_container.TaskContainer()

def test_job_listener():
    job = time_job.TimeJob()
    job_listener = time_job.TimeJobListener()
    trigger = simple_trigger.SimpleTrigger(0, 2)
    time_task = task.Task('TimeTask', job, trigger, job_listener)
    container.add_task(time_task)

    container.start_all(True)
    
    time.sleep(10) # pause container
    
    container.stop_all()
    
test_job_listener()