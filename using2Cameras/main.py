import time

import scheduler
from task1 import *
from task2 import *
from AItask import *

scheduler = scheduler.Scheduler()
scheduler.SCH_Init()
# task1 = Task1()
# task2 = Task2()
aitask = AItask(0)
aitask2 = AItask(1)


# scheduler.SCH_Add_Task(task1.Task1Run, 1000, 2000)
# scheduler.SCH_Add_Task(task2.Task2Run, 2000, 4000)
scheduler.SCH_Add_Task(aitask.aitaskRun, 3000, 3000)
scheduler.SCH_Add_Task(aitask2.aitaskRun, 4000, 4500)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(1)

