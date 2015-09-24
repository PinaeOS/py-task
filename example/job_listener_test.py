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

    trigger1 = simple_trigger.SimpleTrigger(1, 2)
    time_task1 = task.Task('TimeTask1', time_job.TimeJob(), trigger1, time_job.TimeJobListener('time-job'))
    container.add_task(time_task1)
    
    trigger2 = simple_trigger.SimpleTrigger(1, 2)
    time_task2 = task.Task('TimeTask2', time_job.TimeJobWithException(), trigger2, time_job.TimeJobListener('exception-job'))
    container.add_task(time_task2)

    container.start_all(True)
    
    time.sleep(2) # stop container
    
    container.stop_all()
    
test_job_listener()