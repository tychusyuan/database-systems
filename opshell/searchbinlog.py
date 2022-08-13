import pymysql.cursors
import time
from datetime import datetime
import hashlib

#execute = True
execute = False

mysql_source={
"host":"10.0.0.103",
"port":3306,
"user":"root",
"pwd":"password",
}

mysql_dest={
"host":"10.0.0.102",
"port":3306,
"user":"root",
"pwd":"password",
}

replica={
"user":"sync_user",
"pwd":"password",
}

def source_binlog(conn):
    lst=[]
    with conn.cursor() as cursor:
        # 预取 binlog file 和pos，取出这个pos开始到sql_thread结束之后的所有 binlog event
        cursor.execute("show master status;")
        master_status=cursor.fetchone()
        f=master_status["File"]
        p=master_status["Position"]
        print(f,p)
        time.sleep(8)
        if execute:
            print("STOP SLAVE IO_THREAD; execute")
            cursor.execute("STOP SLAVE IO_THREAD;")
        else:
            print("STOP SLAVE IO_THREAD; test")
        time.sleep(2)

        if execute:
            print("STOP SLAVE SQL_THREAD; execute")
            cursor.execute("STOP SLAVE SQL_THREAD;")
        else:
            print("STOP SLAVE SQL_THREAD; test")
        cursor.execute("SHOW BINLOG EVENTS IN %s FROM %s",(f,p))
        binlog_events=cursor.fetchall()
        for row in binlog_events:
            hexadecimal = hashlib.md5(bytes(row['Event_type']+str(row['Server_id'])+row['Info'],'utf-8')).hexdigest()
            p= int(row['End_log_pos'])
            lst.append(hexadecimal)
        #    print(row,hexadecimal)
        print(f,p)
    return lst

def source_change(conn,host,port,user,pwd,fil,pos):
        with conn.cursor() as cursor:
            sql = "CHANGE MASTER TO MASTER_HOST='%s',MASTER_PORT=%s,MASTER_USER='%s',MASTER_PASSWORD='%s',MASTER_LOG_FILE='%s', MASTER_LOG_POS=%s;" % (
                host,port,user,pwd,fil,pos
            )
            if execute:
                print(sql,"execute")
                cursor.execute(sql)
            else:
                print(sql,"test")

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
            # 从预取 file和pos 位置开始向后 逐一检查 binlog event，遇到checksum相同的之后，正组比较checksum
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
                    # 全组都相同，则匹配到file 和 pos
                    break
            else:
                p=int(row['End_log_pos'])
            
        print(f,p)
    return fil, pos

if __name__ == "__main__":
    print("execute =",execute)
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
        # 预取 目标实例 binlog file 和 pos
        dest_result = dest_master_status(conn_dest)
        f = dest_result["File"]
        p = dest_result["Position"]

    lst = None
    with conn_source :
        # 迁移实例 最后一组 binlog event
        lst = source_binlog(conn_source)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    with conn_dest :
        # 目标实例binlog event对比迁移实例最后一组 event，找到对应的file 和 pos
        f,p = dest_binlog(conn_dest,f,p,lst)

    with conn_source :
        # change master
       source_change(conn_source,mysql_dest["host"],mysql_dest["port"],replica["user"],replica["pwd"],f,p) 
