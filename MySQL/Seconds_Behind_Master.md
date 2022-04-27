# innodb_flush_log_at_trx_commit & sync_binlog

##
```shell
SHOW GLOBAL VARIABLES WHERE Variable_Name IN ('innodb_flush_log_at_trx_commit','sync_binlog');
```

##
```shell
 set global innodb_flush_log_at_trx_commit=2;
```

```shell
set global sync_binlog=2000;
```
