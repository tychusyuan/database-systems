
### 查看权限
```sql
select user,host,authentication_string from mysql.user;
```

### 复制用户
```sql
 select CONCAT("CREATE USER '",user,"'@'",host,"' IDENTIFIED BY PASSWORD '",authentication_string,"';" from mysql.user;
```

### 撤销权限
```sql
REVOKE INSERT ON *.* FROM 'user'@'localhost';
```
```sql
REVOKE ALL PRIVILEGES ON *.* FROM 'user'@'localhost';
```

###  查看权限
```sql
SHOW GRANTS FOR 'user'@'localhost';
```
