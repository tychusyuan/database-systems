import pymysql.cursors
import time
from datetime import datetime
import hashlib

mysql_source={
"host":"db03",
"port":3306,
"user":"root",
"pwd":"password",
}

mysql_dest={
"host":"db02",
"port":3306,
"user":"root",
"pwd":"password",
}

def source_binlog(conn):
    lst=[]
    with conn.cursor() as cursor:
        cursor.execute("show master status;")
        master_status=cursor.fetchone()
        f=master_status["File"]
        p=master_status["Position"]
        print(f,p)
        time.sleep(10)
        cursor.execute("SHOW BINLOG EVENTS IN %s FROM %s",(f,p))
        binlog_events=cursor.fetchall()
        for row in binlog_events:
            hexadecimal = hashlib.md5(bytes(row['Event_type']+str(row['Server_id'])+row['Info'],'utf-8')).hexdigest()
            p= int(row['End_log_pos'])
            lst.append(hexadecimal)
        #    print(row,hexadecimal)
        print(f,p)
    return lst

def dest_master_status(conn):
    result=None
    with conn.cursor() as cursor:
        cursor.execute("show master status;")
        result=cursor.fetchone()
        #f=master_status["File"]
        #p=master_status["Position"]
    return result

def dest_binlog(conn,fil,pos,lst):
    f = fil
    p = pos
    l = len(lst)
    if l < 1 :
        return
    with conn.cursor() as cursor:
        while True:
            cursor.execute("SHOW BINLOG EVENTS IN %s FROM %s LIMIT 1",(f,p))
            row=cursor.fetchone()
            hexadecimal = hashlib.md5(bytes(row['Event_type']+str(row['Server_id'])+row['Info'],'utf-8')).hexdigest()
            if hexadecimal == lst[0]:
                fix = 0
                cursor.execute("SHOW BINLOG EVENTS IN %s FROM %s LIMIT %s",(f,p,l))
                binlog_events=cursor.fetchall()
                for i in range(l):
                    event_h = hashlib.md5(bytes(binlog_events[i]['Event_type']+str(binlog_events[i]['Server_id'])+binlog_events[i]['Info'],'utf-8')).hexdigest()
                    p=int(binlog_events[i]['End_log_pos'])
                    #print(binlog_events[i],event_h)
                    if event_h == lst[i]:
                        fix = fix+1
                if fix == l:
                    break
            else:
                p=int(row['End_log_pos'])
            
        print(f,p)

if __name__ == "__main__":
    conn_source = pymysql.connect(host=mysql_source["host"],
                             port=mysql_source["port"],
                             user=mysql_source["user"],
                             password=mysql_source["pwd"],
                             autocommit=False,
                             cursorclass=pymysql.cursors.DictCursor)

    conn_dest = pymysql.connect(host=mysql_dest["host"],
                             port=mysql_dest["port"],
                             user=mysql_dest["user"],
                             password=mysql_dest["pwd"],
                             autocommit=False,
                             cursorclass=pymysql.cursors.DictCursor)
    f = None
    p = None
    with conn_dest :
        dest_result = dest_master_status(conn_dest)
        f = dest_result["File"]
        p = dest_result["Position"]

    lst = None
    with conn_source :
        lst = source_binlog(conn_source)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    with conn_dest :
        dest_binlog(conn_dest,f,p,lst)
