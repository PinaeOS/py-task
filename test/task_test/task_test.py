# coding=utf-8

import time

from task.trigger import simple_trigger
from task.trigger import cron_trigger
from task import task
from task import task_container

import my_job

container = task_container.TaskContainer()

_job = my_job.MyJob()

_trigger = simple_trigger.SimpleTrigger(50, 3)
_trigger.set_delay(5, 0)
_task = task.Task('Task', _job, _trigger)

container.add_task(_task)

container.start_all()

time.sleep(10)

container.pasuse_all()

time.sleep(30)

container.start_all()

time.sleep(60)

container.stop_all()

time.sleep(10)

container.remove_task('Task')

_trigger = cron_trigger.CronTrigger('0-59/5 48,50,52 * 28 MAY * 2015')
_task = task.Task('Task2', _job, _trigger)

container.add_task(_task)

container.start_all()