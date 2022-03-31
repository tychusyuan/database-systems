import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             database='db',
                             cursorclass=pymysql.cursors.DictCursor)

# 防止事务过大，或者影响主从延迟
# SELECT CONCAT('delete from `user` where `id`=', `id`, ';') from `user` where `email` like '%s%' ;
with connection:
    lst=[]
    with connection.cursor() as cursor:
        sql = "select `id` FROM `users` WHERE `email` like %s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        lst.append(result["id"])

    with connection.cursor() as cursor:
        for item in lst:
            sql = "delete from  `users` where id = %s"
            cursor.execute(sql, (item))
            connection.commit()

