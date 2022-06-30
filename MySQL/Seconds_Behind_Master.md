# innodb_flush_log_at_trx_commit & sync_binlog

## 收到报警 Seconds_Behind_Master>300 ，并且观察从库磁盘 IO_util > 90%

## 观察MySQL从库 参数
```shell
SHOW GLOBAL VARIABLES WHERE Variable_Name IN ('innodb_flush_log_at_trx_commit','sync_binlog');
```
```shell
+--------------------------------+-------+
| Variable_name                  | Value |
+--------------------------------+-------+
| innodb_flush_log_at_trx_commit | 1     |
| sync_binlog                    | 1     |
+--------------------------------+-------+
2 rows in set (0.14 sec)
```
## 牺牲从库的数据安全性，提高主从复制性能
```shell
 set global innodb_flush_log_at_trx_commit=2;
```
```shell
set global sync_binlog=2000;
```

## 观察结果
```shell
SHOW GLOBAL VARIABLES WHERE Variable_Name IN ('innodb_flush_log_at_trx_commit','sync_binlog');
+--------------------------------+-------+
| Variable_name                  | Value |
+--------------------------------+-------+
| innodb_flush_log_at_trx_commit | 2     |
| sync_binlog                    | 2000  |
+--------------------------------+-------+
2 rows in set (0.14 sec)
```
## Multi-Threaded Replication
### 开启
```
stop slave;
set global slave_parallel_type='LOGICAL_CLOCK';
set global slave_parallel_workers=8;
start slave;
```
### 关闭
```
stop slave;
set global slave_parallel_type='DATABASE';
set global slave_parallel_workers=0;
start slave;
```
