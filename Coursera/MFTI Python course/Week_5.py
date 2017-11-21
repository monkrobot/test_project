#import time
#import os
#
#pid = os.getpid()
#
#while True:
#    print(pid, time.time())
#    time.sleep(2)

import time
import os

pid = os.fork()

if pid == 0:
    while True:
        print("child:", os.getpid())
        time.sleep(5)
else:
    print("parent:", os.getpid())
    os.wait()