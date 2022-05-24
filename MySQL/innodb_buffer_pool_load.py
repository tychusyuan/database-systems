# -*- coding: utf-8 -*-

import pymysql.cursors

table_lst=[
]

dsn={
'host':'127.0.0.1',
'port':3306,
'db':'test_db',
'user':'root',
'passwd':'password',
}

lve=0.8

chunk_size=50

def freeSpace(conn):
    Innodb_buffer_pool_pages_free = None
    Innodb_buffer_pool_pages_total = None
    with conn.cursor() as cursor:
        sql = "show global status where Variable_name in ('Innodb_buffer_pool_pages_free','Innodb_buffer_pool_pages_total');"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            if row['Variable_name'] == 'Innodb_buffer_pool_pages_free':
                Innodb_buffer_pool_pages_free = float(row['Value'])
            elif row['Variable_name'] == 'Innodb_buffer_pool_pages_total':
                Innodb_buffer_pool_pages_total = float(row['Value'])
    return Innodb_buffer_pool_pages_free,Innodb_buffer_pool_pages_total

def indexLst(conn,table):
    index_lst = []
    with conn.cursor() as cursor:
        sql = "show index from %s;" % (table)
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) > 0 :
            index_name = ""
            for row in result:
                if row['Key_name'] == index_name:
                    continue
                else:
                    index_name = row['Key_name']
                    index_lst.append(row['Column_name'])
        else:
            index_lst.append('_rowid')
        
    return index_lst

def tableLst(conn):
    lst = []
    with conn.cursor() as cursor:
        sql = "SELECT concat( table_schema, '.', table_name ) table_name FROM information_schema.TABLES where TABLE_TYPE = 'BASE TABLE' AND ENGINE = 'InnoDB' ORDER BY information_schema.TABLES.DATA_LENGTH DESC LIMIT 50;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            lst.append(row['table_name'])
    return lst

def loadTable(conn,table,index_lst):
    with conn.cursor() as cursor:
        for index in index_lst:
            index_max = None
            sql = "select * from %s order by %s asc limit %s" % (table,index,chunk_size)
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                index_max = row[index]
            while True:
                sql = "select * from %s where %s > '%s' order by %s limit %s" % (table,index,index_max,index,chunk_size)
                cursor.execute(sql)
                result = cursor.fetchall()
                if len(result) == 0:
                    break
                for row in result:
                    index_max = row[index]
                print(table,index,index_max)

def load(conn,lst):
    with conn:
        if len(lst) == 0:
            lst = tableLst(conn)
        for table in lst:
            Innodb_buffer_pool_pages_free,Innodb_buffer_pool_pages_total = freeSpace(conn)
            print(Innodb_buffer_pool_pages_free,Innodb_buffer_pool_pages_total,(Innodb_buffer_pool_pages_total - Innodb_buffer_pool_pages_free)/Innodb_buffer_pool_pages_total)
            if ((Innodb_buffer_pool_pages_total - Innodb_buffer_pool_pages_free)/Innodb_buffer_pool_pages_total) < lve :
                index_lst = indexLst(conn,table)
                if len(index_lst) == 0:
                    index_lst = ['_rowid']

                loadTable(conn,table,index_lst)


if __name__ == "__main__":
    conn = pymysql.connect(host=dsn['host'],port=dsn['port'],database=dsn['db'],
                             user=dsn['user'],password=dsn['passwd'],
                             cursorclass=pymysql.cursors.DictCursor)
    load(conn,table_lst)
