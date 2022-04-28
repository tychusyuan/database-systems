import os
from datetime import datetime
from time import sleep

'''
mkdir /home/work/applylog -p
chown work.work /home/work/applylog -R
mkdir /home/applylog -p
chown work.work /home/applylog -R
'''

DFLIST = [
{'df':"/home/work",'log':"/home/work/applylog"},
{'df':"/home",'log':"/home/applylog"},
]
BLOCKSIZE = 1024 * 1024 * 1024
P = True
LEV = 0.5

def plog(s):
    if P:
        # print "%s %s" % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),s)
        print("%s %s" % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),s))

def availRatio(vfs):
    return  vfs.f_bavail/vfs.f_blocks

def availSpace(vfs):
    return int( (vfs.f_bavail - (vfs.f_blocks * LEV) ) * vfs.f_bsize / BLOCKSIZE )

def appendFile(fielpath):
    with open(fielpath,"w") as f:
        fs=0
        plog( "%s %s" % ("append",fielpath))
        while True:
            lst=[]
            for idx in range(0,1000):
                now = datetime.now()
                lst.append("%s %s" % (now.strftime('%Y-%m-%d %H:%M:%S'),"[Note] Aborted connection 3519053 to db: 'unconnected' user: 'unauthenticated' host: 'localhost' (Got an error reading communication packets)"))
            
            f.write('\n'.join(lst))
            f.write('\n')

            fs = os.path.getsize(fielpath)
            if fs < BLOCKSIZE :
                sleep(0.1)
                continue
            else:
                break

def takeUp(space,logpath):
    if space > 0:
        for idx in range(0,space):
            now = datetime.now()
            appendFile("%s/%s.log" % (logpath,now.strftime('%Y%m%d%H%M%S')))
            sleep(1)

def takeDown(space,logpath):
    if space < 0 :
        idx = abs(space)
        lst = os.listdir(logpath)
        if len(lst) > 0:
            for f in lst:
                file_name = "%s/%s" % (logpath,f)
                os.remove(file_name)
                plog("%s %s" % ("remove",file_name))
                idx -= 1
                if idx > 0:
                    sleep(1)
                    continue
                else:
                    break

def Run():
    while True:
        for idx in range(0,60):
            for item in DFLIST:
                df = item['df']
                logpath = item['log']

                if not os.path.exists(logpath):
                    os.mkdir(logpath)

                info = os.statvfs(df)
                plog(info)
                space = availSpace(info)
                plog(space)
                takeDown(space,logpath)
                if idx == 0 :
                    takeUp(space,logpath)

            plog("next loop")
            sleep(60)

if __name__ == "__main__":
    Run()
