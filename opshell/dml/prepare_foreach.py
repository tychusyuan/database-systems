import pymysql.cursors
import time

mysql_dsn = {
"host":"127.0.0.1",
"port":3306,
"user":"root",
"pwd":"password",
"db":"db_test",
}

chunk_size = 100

sql_dir = [
{"pk":"id",
"s_sql":"select a.`id` from table_a a left join table_b b on a.package_name_hash = b.package_name_hash left join table_c c on b.package_name_hash = c.package_name_hash where a.status in (304, 4) and c.package_name is null;",
"e_sql":"update table_a a left join table_b b on a.package_name_hash = b.package_name_hash left join table_c c on b.package_name_hash = c.package_name_hash set a.status = b.status, a.update_time = 1660123067467 where a.`id` = %s"},
{"pk":"id",
"s_sql":"select a.`id` from table_a a left join table_b b on a.package_name_hash = b.package_name_hash where a.status in (2, 301, 302, 201) and b.package_name is null;",
"e_sql":"update table_a a set a.status = 1,a.update_time = 1660123067467 where a.id = %s"},
]

def split(lst, chunk_size):
  for i in range(0, len(lst), chunk_size):
    yield lst[i:i + chunk_size]

# 防止事务过大，或者影响主从延迟
# SELECT CONCAT('delete from `user` where `id`=', `id`, ';') from `user` where `email` like '%s%' ;
def sql_foreach(t,conn):
    result=None
    with conn.cursor() as cursor:
        cursor.execute(t["s_sql"])
        result = cursor.fetchall()

    result_len=len(result)

    with conn.cursor() as cursor:
        idx=0
        for chunk in split(result,chunk_size):
            lst=[]
            for row in chunk:
                lst.append(row[t["pk"]])
                idx=idx+1

            row_result = cursor.executemany(t["e_sql"], lst)
            if row_result > chunk_size :
                conn.rollback()
                exit(0)
            else:
                print(t["e_sql"],row_result,idx,result_len)
                conn.commit()

if __name__ == "__main__":
    conn = pymysql.connect(host=mysql_dsn["host"],
                             port=mysql_dsn["port"],
                             user=mysql_dsn["user"],
                             password=mysql_dsn["pwd"],
                             database=mysql_dsn["db"],
                             autocommit=False,
                             cursorclass=pymysql.cursors.DictCursor)
    with conn :
        for t in sql_dir:
           sql_foreach(t,conn) 
