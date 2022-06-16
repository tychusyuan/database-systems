# Performance Schema 

## Quick Start
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
