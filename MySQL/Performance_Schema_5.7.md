# Performance Schema 

## 1. Quick Start
###  The Performance Schema is enabled by default
###  my.cnf 
```
[mysqld]
performance_schema=ON
```
```sql
SHOW VARIABLES LIKE 'performance_schema';
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| performance_schema | ON    |
+--------------------+-------+
```
### The Performance Schema is implemented as a storage engine
```sql
SHOW ENGINES;
```
```
+--------------------+---------+----------------------------------------------------------------------------+--------------+------+------------+
| Engine             | Support | Comment                                                                    | Transactions | XA   | Savepoints |
+--------------------+---------+----------------------------------------------------------------------------+--------------+------+------------+
| PERFORMANCE_SCHEMA | YES     | Performance Schema                                                         | NO           | NO   | NO         |
| CSV                | YES     | CSV storage engine                                                         | NO           | NO   | NO         |
| MyISAM             | YES     | MyISAM storage engine                                                      | NO           | NO   | NO         |
| BLACKHOLE          | YES     | /dev/null storage engine (anything you write to it disappears)             | NO           | NO   | NO         |
| MRG_MYISAM         | YES     | Collection of identical MyISAM tables                                      | NO           | NO   | NO         |
| MEMORY             | YES     | Hash based, stored in memory, useful for temporary tables                  | NO           | NO   | NO         |
| ARCHIVE            | YES     | Archive storage engine                                                     | NO           | NO   | NO         |
| InnoDB             | DEFAULT | Percona-XtraDB, Supports transactions, row-level locking, and foreign keys | YES          | YES  | YES        |
| FEDERATED          | NO      | Federated MySQL storage engine                                             | NULL         | NULL | NULL       |
+--------------------+---------+----------------------------------------------------------------------------+--------------+------+------------+
```
```sql
SELECT * FROM INFORMATION_SCHEMA.ENGINES WHERE ENGINE='PERFORMANCE_SCHEMA';
```
```
+--------------------+---------+--------------------+--------------+------+------------+
| ENGINE             | SUPPORT | COMMENT            | TRANSACTIONS | XA   | SAVEPOINTS |
+--------------------+---------+--------------------+--------------+------+------------+
| PERFORMANCE_SCHEMA | YES     | Performance Schema | NO           | NO   | NO         |
+--------------------+---------+--------------------+--------------+------+------------+
```
### Performance Schema tables
```sql
SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'performance_schema';
```
```sql
SHOW TABLES FROM performance_schema;
```
### not all instruments and consumers are enabled
```sql
select * from performance_schema.setup_instruments;
```
```sql
UPDATE performance_schema.setup_instruments SET ENABLED = 'YES', TIMED = 'YES';
```
```sql
UPDATE performance_schema.setup_instruments SET ENABLED = 'NO' WHERE NAME = 'wait/synch/mutex/sql/LOCK_mysql_create_db';
```
```sql
select * from performance_schema.setup_consumers;
```
```sql
UPDATE performance_schema.setup_consumers SET ENABLED = 'YES';
```
## 2. Performance Schema Build Configuration
### The Performance Schema is mandatory and always compiled in. It is possible to exclude certain parts of the Performance Schema instrumentation. For example, to exclude stage and statement instrumentation, do this:
```shell
cmake . \
        -DDISABLE_PSI_STAGE=1 \
        -DDISABLE_PSI_STATEMENT=1
```
### the descriptions of the DISABLE_PSI_XXX CMake options 
|Formats|	Description	|Default	|
|:----------------------|:---------------------------------------------------------------------|:---------:|
|DISABLE_PSI_COND	|Exclude Performance Schema condition instrumentation	|OFF|		
|DISABLE_PSI_FILE	|Exclude Performance Schema file instrumentation	|OFF|		
|DISABLE_PSI_IDLE	|Exclude Performance Schema idle instrumentation	|OFF|		
|DISABLE_PSI_MEMORY	|Exclude Performance Schema memory instrumentation	|OFF|		
|DISABLE_PSI_METADATA	|Exclude Performance Schema metadata instrumentation	|OFF|		
|DISABLE_PSI_MUTEX	|Exclude Performance Schema mutex instrumentation	|OFF|		
|DISABLE_PSI_PS	|Exclude the performance schema prepared statements	|OFF|		
|DISABLE_PSI_RWLOCK	|Exclude Performance Schema rwlock instrumentation	|OFF|		
|DISABLE_PSI_SOCKET	|Exclude Performance Schema socket instrumentation	|OFF|		
|DISABLE_PSI_SP	|Exclude Performance Schema stored program instrumentation	|OFF|		
|DISABLE_PSI_STAGE	|Exclude Performance Schema stage instrumentation	|OFF|		
|DISABLE_PSI_STATEMENT	|Exclude Performance Schema statement instrumentation	|OFF|		
|DISABLE_PSI_STATEMENT_DIGEST	|Exclude Performance Schema statements_digest instrumentation	|OFF|		
|DISABLE_PSI_TABLE	|Exclude Performance Schema table instrumentation	|OFF|		
|DISABLE_PSI_THREAD	|Exclude the performance schema thread instrumentation	|OFF|		
|DISABLE_PSI_TRANSACTION	|Exclude the performance schema transaction instrumentation	|OFF|		

### To verify whether a server was built with Performance Schema support, check its help output. If the Performance Schema is available, the output mentions several variables with names that begin with performance_schema:
```shell
bin/mysqld --verbose --help | grep performance-schema
```
## 3. Performance Schema Startup Configuration
### To control an instrument at server startup, use an option of this form:
```
--performance-schema-instrument='instrument_name=value'
```
Here, instrument_name is an instrument name such as wait/synch/mutex/sql/LOCK_open, and value is one of these values:

OFF, FALSE, or 0: Disable the instrument

ON, TRUE, or 1: Enable and time the instrument

COUNTED: Enable and count (rather than time) the instrument

Each --performance-schema-instrument option can specify only one instrument name, but multiple instances of the option can be given to configure multiple instruments. In addition, patterns are permitted in instrument names to configure instruments that match the pattern. To configure all condition synchronization instruments as enabled and counted, use this option:
```
--performance-schema-instrument='wait/synch/cond/%=COUNTED'
```
To disable all instruments, use this option:
```
--performance-schema-instrument='%=OFF'
```
Exception: The memory/performance_schema/% instruments are built in and cannot be disabled at startup.

Longer instrument name strings take precedence over shorter pattern names, regardless of order. For information about specifying patterns to select instruments, see Section 25.4.9, “Naming Instruments or Consumers for Filtering Operations”.

An unrecognized instrument name is ignored. It is possible that a plugin installed later may create the instrument, at which time the name is recognized and configured.

To control a consumer at server startup, use an option of this form:
```
--performance-schema-consumer-consumer_name=value
```
Here, consumer_name is a consumer name such as events_waits_history, and value is one of these values:

OFF, FALSE, or 0: Do not collect events for the consumer

ON, TRUE, or 1: Collect events for the consumer

For example, to enable the events_waits_history consumer, use this option:
```
--performance-schema-consumer-events-waits-history=ON
```
To change the value of Performance Schema system variables, set them at server startup. For example, put the following lines in a my.cnf file to change the sizes of the history tables for wait events:
```
[mysqld]
performance_schema
performance_schema_events_waits_history_size=20
performance_schema_events_waits_history_long_size=15000
```
The Performance Schema automatically sizes the values of several of its parameters at server startup if they are not set explicitly. For example, it sizes the parameters that control the sizes of the events waits tables this way. the Performance Schema allocates memory incrementally, scaling its memory use to actual server load, instead of allocating all the memory it needs during server startup. Consequently, many sizing parameters need not be set at all. To see which parameters are autosized or autoscaled, use mysqld --verbose --help and examine the option descriptions, or see Section 25.15, “Performance Schema System Variables”.

|Name	                                                        |Cmd-Line	|Option File	|System Var	|Var Scope	|Dynamic|
|:--------------------------------------------------------------|------|------|------|----------|------|
|performance_schema	|Yes	|Yes	|Yes	|Global	|No|
|performance_schema_accounts_size	|Yes	|Yes	|Yes	|Global	|No|
|performance_schema_digests_size	|Yes	|Yes	|Yes	|Global	|No|
|performance_schema_events_stages_history_long_size	|Yes	|Yes	|Yes	|Global	|No|
|performance_schema_events_stages_history_size	|Yes	|Yes	|Yes	|Global	No|
|performance_schema_events_statements_history_long_size	|Yes	|Yes	|Yes	|Global	|No|
|performance_schema_events_statements_history_size	|Yes	|Yes	|Yes	|Global	|No|
|performance_schema_events_transactions_history_long_size	|Yes	|Yes	|Yes	|Global	|No|

|performance_schema_events_transactions_history_size	|Yes	|Yes	|Yes	Global	No
|performance_schema_events_waits_history_long_size	Yes	Yes	|Yes	Global	No
|performance_schema_events_waits_history_size	Yes	Yes	Yes	Global	No
|performance_schema_hosts_size	Yes	Yes	Yes	Global	No
|performance_schema_max_cond_classes	Yes	Yes	Yes	Global	No
performance_schema_max_cond_instances	Yes	Yes	Yes	Global	No
performance_schema_max_digest_length	Yes	Yes	Yes	Global	No
performance_schema_max_file_classes	Yes	Yes	Yes	Global	No
performance_schema_max_file_handles	Yes	Yes	Yes	Global	No
performance_schema_max_file_instances	Yes	Yes	Yes	Global	No
performance_schema_max_index_stat	Yes	Yes	Yes	Global	No
performance_schema_max_memory_classes	Yes	Yes	Yes	Global	No
performance_schema_max_metadata_locks	Yes	Yes	Yes	Global	No
performance_schema_max_mutex_classes	Yes	Yes	Yes	Global	No
performance_schema_max_mutex_instances	Yes	Yes	Yes	Global	No
performance_schema_max_prepared_statements_instances	Yes	Yes	Yes	Global	No
performance_schema_max_program_instances	Yes	Yes	Yes	Global	No
performance_schema_max_rwlock_classes	Yes	Yes	Yes	Global	No
performance_schema_max_rwlock_instances	Yes	Yes	Yes	Global	No
performance_schema_max_socket_classes	Yes	Yes	Yes	Global	No
performance_schema_max_socket_instances	Yes	Yes	Yes	Global	No
performance_schema_max_sql_text_length	Yes	Yes	Yes	Global	No
performance_schema_max_stage_classes	Yes	Yes	Yes	Global	No
performance_schema_max_statement_classes	Yes	Yes	Yes	Global	No
performance_schema_max_statement_stack	Yes	Yes	Yes	Global	No
performance_schema_max_table_handles	Yes	Yes	Yes	Global	No
performance_schema_max_table_instances	Yes	Yes	Yes	Global	No
performance_schema_max_table_lock_stat	Yes	Yes	Yes	Global	No
performance_schema_max_thread_classes	Yes	Yes	Yes	Global	No
performance_schema_max_thread_instances	Yes	Yes	Yes	Global	No
performance_schema_session_connect_attrs_size	Yes	Yes	Yes	Global	No
performance_schema_setup_actors_size	Yes	Yes	Yes	Global	No
performance_schema_setup_objects_size	Yes	Yes	Yes	Global	No
performance_schema_show_processlist	Yes	Yes	Yes	Global	Yes
performance_schema_users_size	Yes	Yes	Yes	Global	No
For each autosized parameter that is not set at server startup, the Performance Schema determines how to set its value based on the value of the following system values, which are considered as “hints” about how you have configured your MySQL server:
```
max_connections
open_files_limit
table_definition_cache
table_open_cache
```
