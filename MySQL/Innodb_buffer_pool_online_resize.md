# Innodb buffer pool online resize

## 通过查询 global variables innodb_buffer_pool_size，得知原配置为 40GB
```shell
show global variables like 'innodb_buffer_pool_size';
+-------------------------------------+----------------+
| Variable_name                       | Value          |
+-------------------------------------+----------------+
| innodb_buffer_pool_size             | 42949672960    |
+-------------------------------------+----------------+
1 rows in set (0.14 sec)
```
##  计划将innodb buffer poll size 改为 30GB， union 原配置 是为了防止 算错数量级，出现低级错误
```shell
select 30 * 1024 * 1024 * 1024 union all select 42949672960 ;
+-------------------------+
| 30 * 1024 * 1024 * 1024 |
+-------------------------+
|             32212254720 |
|             42949672960 |
+-------------------------+
2 rows in set (0.15 sec)
```
## 执行操作
```shell
set global innodb_buffer_pool_size = 32212254720;
Query OK, 0 rows affected (0.15 sec)
```
## 通过 InnoDB_buffer_pool_resize_status 来观察resize 过程
```shell
 SHOW STATUS WHERE Variable_name='InnoDB_buffer_pool_resize_status';
+----------------------------------+------------------------------------------------+
| Variable_name                    | Value                                          |
+----------------------------------+------------------------------------------------+
| Innodb_buffer_pool_resize_status | buffer pool 7 : resizing with chunks 40 to 30. |
+----------------------------------+------------------------------------------------+
1 row in set (0.14 sec)

Thu Mar 10 21:52:06 2022
SHOW STATUS WHERE Variable_name='InnoDB_buffer_pool_resize_status';
+----------------------------------+----------------------------------------------------+
| Variable_name                    | Value                                              |
+----------------------------------+----------------------------------------------------+
| Innodb_buffer_pool_resize_status | Completed resizing buffer pool at 220310 21:52:06. |
+----------------------------------+----------------------------------------------------+
1 row in set (0.15 sec)
```

## 最后记得修改 my.cnf ，否则mysql 实例重启后，会按照 my.cnf 的配置malloc内存
```shell
innodb_buffer_pool_size = 30G
```
