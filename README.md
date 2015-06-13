py_task
=========
py_task is a task scheduling tools for Python.

Installation
------------
The lastest stable is py_task-1.0.tar.gz

    python setup.py install
    
Getting Start
------------

A short demo:
	
	from task import task
	from task import task_container
	from task.job import job
	from task.trigger import cron_trigger
	
	class MyJob(job.Job):

    	def __init__(self):
        	pass
    
    	def execute(self):
        	print 'Hello now is ' + str(time.time())
    
    new_task = task.Task('Task', MyJob(), cron_trigger.CronTrigger('0-59/5 10,15,20 * * * * 2015'))
    container.add_task(new_task)
    container.start_all()

Documentation
------------

Full documentation is hosted on [HERE](). 
Sources are available in the `docs/` directory.

License
-------
py_task is licensed under the Apache License, Version 2.0. See LICENSE for full license text

