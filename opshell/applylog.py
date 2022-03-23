import os
from datetime import datetime
from time import sleep

DF = "/home/work"
LOGPATH = "/home/work/applylog/log"
BLOCKSIZE = 1024 * 1024 * 1024
P = True

def plog(s):
    if P:
        print(s)

def availRatio(vfs):
    return  vfs.f_bavail/vfs.f_blocks

def availSpace(vfs):
    return int( (vfs.f_bavail - (vfs.f_blocks / 2) ) * vfs.f_bsize / BLOCKSIZE )

def appendFile(fielpath):
    with open(fielpath,"w") as f:
        fs=0
        while True:
            lst=[]
            for idx in range(0,1000):
                now = datetime.now()
                lst.append("%s %s" % (now.strftime('%Y-%m-%d %H:%M:%S'),"[Note] Aborted connection 3519053 to db: 'unconnected' user: 'unauthenticated' host: 'localhost' (Got an error reading communication packets)"))
            
            f.write('\n'.join(lst))
            f.write('\n')

            fs = os.path.getsize(fielpath)
            if fs < BLOCKSIZE :
                continue
            else:
                break

def takeUp(space):
    if space > 0:
        for idx in range(0,space):
            now = datetime.now()
            appendFile("%s/%s.log" % (LOGPATH,now.strftime('%Y%m%d%H%M%S')))
            sleep(1)

def takeDown(space):
    if space > 0 :
        idx = 0
        lst = os.listdir(LOGPATH)
        for f in lst:
            os.remove("%s/%s" % (LOGPATH,f))
            idx += 1
            if idx < space:
                sleep(1)
                continue
            else:
                break

def Run():
    while True:
        for idx in range(0,60):
            info = os.statvfs(DF)
            plog(info)
            space = availSpace(info)
            plog(space)
            if availRatio(info) > 0.5 :
                takeDown(abs(space))
            if idx == 0 :
                takeUp(space)

            idx -= 1
            sleep(60)

if __name__ == "__main__":
    Run()
