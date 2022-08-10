import pymysql.cursors
import time

# Connect to the database
connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='123456',
                             database='db_test',
                             autocommit=False,
                             cursorclass=pymysql.cursors.DictCursor)

# 防止事务过大，或者影响主从延迟
# SELECT CONCAT('delete from `user` where `id`=', `id`, ';') from `user` where `email` like '%s%' ;

table_name = "new_app"
where="change_log = 'null'"

pk="app_id"
up_set="change_log = NULL"

with connection:
    lst=[]
    with connection.cursor() as cursor:
        sql = "select `"+pk+"` FROM `"+table_name+"` WHERE "+where+";"
        cursor.execute(sql)
        result = cursor.fetchall()
        result_len=len(result)
        print(result_len)
        time.sleep(10)
        idx=0
        for row in result:
            row_id=row[pk]
            row_sql = "update "+table_name+" set "+up_set+" where `"+pk+"` = %s"
            row_result = cursor.execute(row_sql, (row_id))
            idx = idx + 1
            print(row_sql,row_id,row_result,idx,result_len)
            if row_result == 1:
                connection.commit()
            else:
                connection.rollback()
                exit(0)
