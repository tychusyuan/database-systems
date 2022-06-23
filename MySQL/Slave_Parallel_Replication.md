
## master
```
binlog_group_commit_sync_delay = 10
binlog_group_commit_sync_no_delay_count = 20
```
## slave
```
slave-parallel-type=LOGICAL_CLOCK
slave-parallel-workers=16
master_info_repository=TABLE
relay_log_info_repository=TABLE
relay_log_recovery=ON
```
