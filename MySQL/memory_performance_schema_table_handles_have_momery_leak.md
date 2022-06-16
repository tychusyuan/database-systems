
## 被关闭的bug，看来并不是个案
https://bugs.mysql.com/bug.php?id=93361

## 原来是 默认值问题，导致大量sql打过来，performance_schema 引擎占用大量内存
```sql
select event_name,CURRENT_NUMBER_OF_BYTES_USED/1024/1024 from performance_schema.memory_summary_global_by_event_name order by CURRENT_NUMBER_OF_BYTES_USED desc LIMIT 20;
```
```sql
+-----------------------------------------------------------------------------+----------------------------------------+
| event_name                                                                  | CURRENT_NUMBER_OF_BYTES_USED/1024/1024 |
+-----------------------------------------------------------------------------+----------------------------------------+
| memory/performance_schema/table_handles                                     |                          9280.00000000 |
| memory/performance_schema/events_statements_summary_by_thread_by_event_name |                           246.21679688 |
| memory/performance_schema/memory_summary_by_thread_by_event_name            |                           189.84375000 |
| memory/performance_schema/events_waits_summary_by_thread_by_event_name      |                            99.98437500 |
| memory/performance_schema/events_statements_current                         |                            94.39453125 |
| memory/performance_schema/events_statements_history                         |                            94.39453125 |
| memory/performance_schema/events_statements_history.tokens                  |                            67.50000000 |
| memory/performance_schema/events_statements_current.sqltext                 |                            67.50000000 |
| memory/performance_schema/events_statements_current.tokens                  |                            67.50000000 |
| memory/performance_schema/events_statements_history.sqltext                 |                            67.50000000 |
| memory/performance_schema/events_stages_summary_by_thread_by_event_name     |                            31.64062500 |
| memory/performance_schema/threads                                           |                            27.00000000 |
| memory/performance_schema/events_transactions_history                       |                            22.67578125 |
| memory/performance_schema/events_statements_history_long                    |                            13.65661621 |
| memory/performance_schema/events_waits_history                              |                            11.60156250 |
| memory/sql/String::value                                                    |                             9.86236572 |
| memory/performance_schema/events_statements_summary_by_digest.tokens        |                             9.76562500 |
| memory/performance_schema/events_statements_history_long.sqltext            |                             9.76562500 |
| memory/performance_schema/events_statements_history_long.tokens             |                             9.76562500 |
| memory/performance_schema/mutex_instances                                   |                             7.25000000 |
+-----------------------------------------------------------------------------+----------------------------------------+

```

### MySQL Verification Team
Hi,

Thank you for your bug report. However, I do not believe that this is a bug.

The problem lies in the following settings:
```sql
performance_schema_max_table_instances = 40000
performance_schema_digests_size = 40000
table_open_cache =10000
innodb_open_files=10000
open_files_limit=10000
```
Hence, what you should do, is to reduce the above settings to 10 % of their current settings. After that you should run MySQL server for several hours or one day and collect the same memory data again. I am sure that you will see much less memory usage then 9 Gb. Each of the performance_schema objects takes some memory for itself, frequently not negligible, so when you multiply the above numbers you get a very large memory usage.

Also, you have evidently set InnoDB buffer pool size to be close to the total RAM available on your computer. There are many other parts of MySQL that use the memory. Please, do not set buffer pool size to more then 70 % of the memory that you are dedicated to the server. Also, check out other memory settings , like the values that are allocated for each connection.

This is all explained in our Reference Manual.
```sql
show global variables like 'performance_schema_max_table_instances';
+----------------------------------------+-------+
| Variable_name                          | Value |
+----------------------------------------+-------+
| performance_schema_max_table_instances | -1    |
+----------------------------------------+-------+
1 row in set (0.23 sec)

```
### 最终开启 performance_schema 同时要设置两个参数
```shell
performance_schema                                              = 1
performance_schema_max_table_instances 				= 10000
performance_schema_digests_size 				= 10000
```
###
```shell
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
45305 mysql     20   0   28.4g    25g   8400 S  48.5 81.4  64:46.82 mysqld

gdb --batch --pid `pidof mysqld` --ex 'call malloc_trim(0)'

  PID USER      PR  NI    VIRT    RES    SHR  S  %CPU %MEM     TIME+ COMMAND
45305 mysql     20   0   28.4g    5.2g   8288 S  2.7  17.0  64:56.82 mysqld
```
