import pymysql.cursors
import time

mysql_dsn = {
"host":"localhost",
"port":3306,
"user":"root",
"pwd":"123456",
"db":"db_test",
}

sql_dir = [
{"pk":"id",
"s_sql":"select a.`id` from table_a a left join talbe_b b on a.package_name_hash = b.package_name_hash left join table_c c on b.package_name_hash = c.package_name_hash where a.status in (304, 4) and c.package_name is null;",
"e_sql":"update table_a a left join table_b b on a.package_name_hash = b.package_name_hash left join table_c c on b.package_name_hash = c.package_name_hash set a.status = b.status, a.update_time = 1660123067467 where a.`id` = %s"},
{"pk":"id",
"s_sql":"select a.`id` from table_a a left join table_b b on a.package_name_hash = b.package_name_hash where a.status in (2, 301, 302, 201) and b.package_name is null;",
"e_sql":"update table_a a set a.status = 1,a.update_time = 1660123067467 where a.id = %s"},
]


# Connect to the database
connection = pymysql.connect(host=mysql_dsn["host"],
                             port=mysql_dsn["port"],
                             user=mysql_dsn["user"],
                             password=mysql_dsn["pwd"],
                             database=mysql_dsn["db"],
                             autocommit=False,
                             cursorclass=pymysql.cursors.DictCursor)

# 防止事务过大，或者影响主从延迟
# SELECT CONCAT('delete from `user` where `id`=', `id`, ';') from `user` where `email` like '%s%' ;
for t in sql_dir:
    with connection:
        lst=[]
        with connection.cursor() as cursor:
            cursor.execute(t["s_sql"])
            result = cursor.fetchall()
            result_len=len(result)
            print(result_len)
            time.sleep(10)
            idx=0
            for row in result:
                row_id=row[t["pk"]]
                row_result = cursor.execute(t["e_sql"], (row_id))
                idx = idx + 1
                print(t["e_sql"],row_id,row_result,idx,result_len)
                if row_result == 1:
                    connection.commit()
                else:
                    connection.rollback()
                    exit(0)
