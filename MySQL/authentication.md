
### 查看用户
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

###  查看某用户的权限
```sql
SHOW GRANTS FOR 'user'@'localhost';
```

### 创建用户并授权
```sql
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY '123456' WITH  GRANT OPTION;

GRANT REPLICATION SLAVE,REPLICATION CLIENT ON *.* TO 'rep'@'10.1.1.1' IDENTIFIED BY '123456';

GRANT SELECT,LOCK TABLES,RELOAD ON *.* TO 'backup'@'10.1.1.1' IDENTIFIED BY '123456';

GRANT USAGE ON *.* TO 'user'@'192.168.%' IDENTIFIED BY '123456';/*只授予登陆权限*/
```
