# Tools

## processlist
```sql
select * from information_schema.processlist where `COMMAND`<>'Sleep' order by `TIME` asc;
```

## database info

### 排查 数据库中所有表 大小
```sql
SELECT concat( table_schema, '.', table_name ) table_name,  
concat( round( data_length / ( 1024 *1024*1024 ) , 2 ) , 'G' ) data_length,  
concat( round( index_length / ( 1024 *1024*1024 ) , 2 ) , 'G' ) index_length,  
concat( round( round( data_length + index_length ) / ( 1024 *1024*1024 ) , 2 ) , 'G' ) total_size,  
concat( round( DATA_FREE / ( 1024 *1024*1024 ) , 2 ) , 'G' ) DATA_FREE  
FROM information_schema.TABLES 
ORDER BY information_schema.TABLES.DATA_LENGTH DESC LIMIT 50;
```
### 排查 某个数据库中表大小
```sql
SELECT concat( table_schema, '.', table_name ) table_name,
concat( round( data_length / ( 1024 *1024*1024 ) , 2 ) , 'G' ) data_length,
concat( round( index_length / ( 1024 *1024*1024 ) , 2 ) , 'G' ) index_length,
concat( round( round( data_length + index_length ) / ( 1024 *1024*1024 ) , 2 ) , 'G' ) total_size,
concat( round( DATA_FREE / ( 1024 *1024*1024 ) , 2 ) , 'G' ) DATA_FREE
FROM information_schema.TABLES WHERE TABLE_SCHEMA='db_name'
ORDER BY information_schema.TABLES.DATA_LENGTH DESC LIMIT 20;
```
### tables last_update
```sql
SELECT * FROM mysql.innodb_table_stats order by last_update desc limit 50;
```
## pt-tools
### pt-query-digest
#### slow query
```shell
pt-query-digest --explain localhost -P3306 -uadmin -ppassword --type slowlog --limit 100% --order-by Query_time:sum --since '2022-06-28 00:00:00' --until '2022-06-28 00:30:00' slow.log > slow_query.txt

```

### 锁等待 , 杀掉阻塞的 thread
```sql
select concat('kill ',b.trx_mysql_thread_id,';') from information_schema.innodb_lock_waits as a inner join information_schema.innodb_trx as b on b.trx_id = a.blocking_trx_id inner join information_schema.innodb_trx as c on c.trx_id = a.requesting_trx_id;
```
```shell
watch 'cat select_kill | mysql -h localhost -P3308 -u root -p password -A -N | grep kill > kill ; cat kill ; cat kill | mysql -h localhost -P3308 -u root -p password -A
```

### sql 会话内kill
```sql
set @sql_kill=''; select @sql_kill:=concat('kill ',b.trx_mysql_thread_id,';') from information_schema.innodb_lock_waits as a inner join information_schema.innodb_trx as b on b.trx_id = a.blocking_trx_id inner join information_schema.innodb_trx as c on c.trx_id = a.requesting_trx_id; PREPARE stmt FROM @sql_kill ; EXECUTE stmt; deallocate prepare stmt;
```
