# coding=utf-8

import time

from task import task
from task import task_container

import my_job

container = task_container.TaskContainer()

from task.trigger import simple_trigger
def test_simple_trigger():
    _job = my_job.MyJob()
    
    _trigger = simple_trigger.SimpleTrigger(50, 3)
    _trigger.set_delay(5, 0)
    _task = task.Task('Task', _job, _trigger)
    
    container.add_task(_task)
    
    print '---------Start Simple Trigger---------'
    container.start_all()
    time.sleep(10)
    
    print '---------Pause---------'
    container.pasuse_all()
    time.sleep(30)
    
    print '---------Restart---------'
    container.start_all()
    time.sleep(60)
    
    print '---------Stop---------'
    container.stop_all()
    time.sleep(10)
    
    print '---------Remove---------'
    container.remove_task('Task')

from task.trigger import cron_trigger
def test_cron_trigger():
    _job = my_job.MyJob()
    _trigger = cron_trigger.CronTrigger('0-59/5 10,15,20 * * MAY * 2015')
    _task = task.Task('Task2', _job, _trigger)
    
    container.add_task(_task)

    print '---------Start Cron Trigger---------'
    container.start_all()
    
test_simple_trigger()
time.sleep(30)
test_cron_trigger()