
## 从机上设置跳过主机某个事务
```sql
SET GLOBAL sql_slave_skip_counter = n
```
```sql
stop slave;SET GLOBAL sql_slave_skip_counter=1;start slave;select SLEEP(1);show slave status\G
```

## 跳过单个GTID事务
### 查看一下信息并记录下来:
```sql
show slave status \G;
Retrieved_Gtid_Set: 8f9e146f-0a18-11e7-810a-0050568833c8:1-4  --跳过此事务  
Executed_Gtid_Set: 8f9e146f-0a18-11e7-810a-0050568833c8:1-3,f7c86e19-24fe-11e7-a66c-005056884f03:1-9
```
通过上面的信息可以知道已经执行的gtid是8f9e146f-0a18-11e7-810a-0050568833c8:1-3,准备要执行8f9e146f-0a18-11e7-810a-0050568833c8:4的时候出问题了，所以条跳过此步骤

### 确定跳过哪个事务id 
```sql
select * from performance_schema.replication_applier_status_by_worker;
```
### 利用一个空事务，跳过某个gtid事务
```sql
 STOP SLAVE;SET GTID_NEXT='aaa-bbb-ccc-ddd:N';BEGIN;COMMIT;SET GTID_NEXT='AUTOMATIC';START SLAVE;
```
### 重置
```sql
stop slave;reset master ;SET @@GLOBAL.GTID_PURGED = '933bdff2-998b-11e6-a3ce-246e9618f108:34'; start slave;sleep 1; show slave status\G
```
