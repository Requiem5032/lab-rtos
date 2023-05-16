print("Hello LAB2")
import time
from scheduler import *
from task1 import *
from task2 import *
scheduler = Scheduler()
scheduler.SCH_Init()

task1 = task1()
task2 = task2()

scheduler.SCH_Add_Task(task1.Task1_Run, 1000,2000)
scheduler.SCH_Add_Task(task2.Task2_Run, 2000,4000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(1)