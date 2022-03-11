# Long Transaction

##  找到 长时间执行的 事务
```shell
show engine innodb status;

---TRANSACTION 4544174272, ACTIVE 61664 sec
1 lock struct(s), heap size 1136, 0 row lock(s), undo log entries 3155
MySQL thread id 18417379, OS thread handle 139959229220608, query id 29221616777 localhost user
---TRANSACTION 4543851747, ACTIVE 68836 sec
1 lock struct(s), heap size 1136, 0 row lock(s), undo log entries 3685
MySQL thread id 18416880, OS thread handle 139958621873920, query id 29221621216 localhost user
---TRANSACTION 4543330048, ACTIVE 75501 sec
2 lock struct(s), heap size 1136, 1 row lock(s), undo log entries 3805
MySQL thread id 18417381, OS thread handle 139959102899968, query id 29221617901 localhost user
```
## 依据 thread id 可以查看到这个事务所在的 线程状态

```shell
select * from information_schema.processlist where `ID`='18417381';
+----------+------------+--------------------+----------+---------+------+-------+------+---------+-----------+---------------+
| ID       | USER       | HOST               | DB       | COMMAND | TIME | STATE | INFO | TIME_MS | ROWS_SENT | ROWS_EXAMINED |
+----------+------------+--------------------+----------+---------+------+-------+------+---------+-----------+---------------+
| 18417381 | user       | localhost.         | db       | Sleep   |    1 |       | NULL |    1509 |         0 |             0 |
+----------+------------+--------------------+----------+---------+------+-------+------+---------+-----------+---------------+
```
## 通过 slow query log 或者 general log 排查问 sql
```shell
cat slow.log | grep -A11 'user' | grep -A11 '18417381'
# User@Host: user[user] @  [localhost]  Id: 18417381
# Schema: db  Last_errno: 1205  Killed: 0
# Query_time: 11.652896  Lock_time: 10.741576  Rows_sent: 0  Rows_examined: 547495  Rows_affected: 0
# Bytes_sent: 67  Tmp_tables: 0  Tmp_disk_tables: 0  Tmp_table_sizes: 0
# InnoDB_trx_id: 10D94AE8C
# QC_Hit: No  Full_scan: No  Full_join: No  Tmp_table: No  Tmp_table_on_disk: No
# Filesort: No  Filesort_on_disk: No  Merge_passes: 0
#   InnoDB_IO_r_ops: 0  InnoDB_IO_r_bytes: 0  InnoDB_IO_r_wait: 0.000000
#   InnoDB_rec_lock_wait: 10.733627  InnoDB_queue_wait: 0.000000
#   InnoDB_pages_distinct: 5917
use misc_cms;
SET timestamp=1645932479;
--
# User@Host: user[user] @  [localhost]  Id: 18417381
# Schema: db  Last_errno: 1205  Killed: 0
# Query_time: 11.592769  Lock_time: 10.727468  Rows_sent: 0  Rows_examined: 547495  Rows_affected: 0
# Bytes_sent: 67  Tmp_tables: 0  Tmp_disk_tables: 0  Tmp_table_sizes: 0
# InnoDB_trx_id: 10D94AE8C
# QC_Hit: No  Full_scan: No  Full_join: No  Tmp_table: No  Tmp_table_on_disk: No
# Filesort: No  Filesort_on_disk: No  Merge_passes: 0
#   InnoDB_IO_r_ops: 0  InnoDB_IO_r_bytes: 0  InnoDB_IO_r_wait: 0.000000
#   InnoDB_rec_lock_wait: 10.727361  InnoDB_queue_wait: 0.000000
#   InnoDB_pages_distinct: 5920
SET timestamp=1645932491;
DELETE FROM t_stat_upload_file WHERE UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(updatetime)>3600*24*90;
```
