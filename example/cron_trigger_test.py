'''
Cron trigger test case  

@author: Huiyugeng
'''

import datetime

from task import task
from task import task_container

from task.trigger import cron_trigger

from example.jobs import time_job
from example.jobs import hello_job

container = task_container.TaskContainer()

def test_cron_trigger():
    
    #start time_job hour=* minute=10-50 second=every 5 seconds 
    trigger_1 = cron_trigger.CronTrigger('0-59/5 10-50 * * * * *')
    trigger_1.set_date(datetime.datetime(2015, 7, 9, 1, 25), datetime.datetime(2015, 7, 10, 1, 40));
    
    task_1 = task.Task('Task_1', time_job.TimeJob(), trigger_1)
    container.add_task(task_1)
    
    #start hello_job hour=* minute=15-45 second=every 22 seconds 
    trigger_2 = cron_trigger.CronTrigger('0-59/22 15-45 * * * * *')
    trigger_2.set_date(datetime.datetime(2015, 7, 9, 1, 25));
    
    task_2 = task.Task('Task_2', hello_job.HelloJob(), trigger_2)
    container.add_task(task_2)

    print '---------Start---------'
    container.start_all()

if __name__ == '__main__':
    test_cron_trigger()