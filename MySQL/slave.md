
## 从机上设置跳过主机某个事务
```sql
SET GLOBAL sql_slave_skip_counter = n
```
```sql
stop slave;SET GLOBAL sql_slave_skip_counter=1;start slave;select SLEEP(1);show slave status\G
```

## 跳过单个GTID事务
### 确定跳过哪个事务id 
```sql
select * from performance_schema.replication_applier_status_by_worker;
```
### 跳过
```sql
 STOP SLAVE;SET GTID_NEXT='aaa-bbb-ccc-ddd:N';BEGIN;COMMIT;SET GTID_NEXT='AUTOMATIC';START SLAVE;
```
### 重置
```sql
stop slave;reset master ;SET @@GLOBAL.GTID_PURGED = '933bdff2-998b-11e6-a3ce-246e9618f108:34'; start slave;sleep 1; show slave status\G
```
