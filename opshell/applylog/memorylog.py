import gc
from time import sleep
from datetime import datetime
import psutil

LVE = 0.5
BLOCKSIZE = 1024 * 1024

def plog(s):
    print("%s %s" % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),s))

def memorySpace():
    mem = psutil.virtual_memory()
    plog(int((mem.available - (mem.total*LVE)) / BLOCKSIZE))
    return int((mem.available - (mem.total*LVE)) / BLOCKSIZE)

def memoryUp(lst):
    while memorySpace() > 0:
        lst.append(1 << 7864320)

def memoryDown(lst):
    while len(lst) > 0:
        if memorySpace() < 0:
            del(lst[0])
            gc.collect()
        else:
            break

if __name__ == "__main__":
    lst=[]
    while True:
        for idx in range(0,20):
            memoryDown(lst)
            if idx == 0:
                memoryUp(lst)

            sleep(3)
