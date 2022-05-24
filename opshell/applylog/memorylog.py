# -*- coding: utf-8 -*-

import sys
import gc
from time import sleep
from datetime import datetime

TOPLVE = 0.5
LOWLVE = 0.4
BLOCKSIZE = 1024 * 1024

def sysMem():
    with open("/proc/meminfo") as meminfo:
        for item in meminfo:
            if item.startswith("MemTotal"):
                total_mem = int(item.split()[1])
            elif item.startswith("MemAvailable"):
                aval_mem = int(item.split()[1])
                break
            else:
                pass
    return total_mem*1024,aval_mem*1024

def plog(s):
    print("%s %s" % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),s))

def memorySpace(lve):
    total_mem , aval_mem = sysMem()
    plog((total_mem - aval_mem)/float(total_mem))
    return int((aval_mem  - (total_mem * (1-lve) )) / BLOCKSIZE)

def memoryUp(lst):
    while memorySpace(LOWLVE) > 0:
        lst.append(fillBlock())
    
        plog(len(lst))

def memoryDown(lst):
    while len(lst) > 0:
        if memorySpace(TOPLVE) < 0:
            del(lst[0])
            gc.collect()
        else:
            break
        plog(len(lst))

def fillBlock():
    lst=[]
    for idx in range(0,8192):
        lst.append("NcOSK1oobg9cqVKC_dCYV1y6WNhqzNEN")
    lst.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return "".join(lst)

if __name__ == "__main__":
    lst=[]
    while True:
        for idx in range(0,20):
            memoryDown(lst)
            if idx == 1:
                memoryUp(lst)

            sleep(1)
