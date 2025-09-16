from datetime import datetime as date
from random import randint
import time

for i in range(5):
    right_this_minute = date.today().minute
    if(right_this_minute % 2 != 0):
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")

    print("Time registered:", date.today().hour, "h", date.today().minute, "m", date.today().second, "s")
    slp = randint(1, 60)
    print("Sleep time:", slp, "seconds.")

    time.sleep(slp)
