
复制用户
```sql
 select CONCAT("CREATE USER '",user,"'@'",host,"' IDENTIFIED BY PASSWORD '",authentication_string,"';" from mysql.user;
```
