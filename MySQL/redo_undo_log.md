# redo & undo log

## WAL (Write Ahead Log)

- 「预写式日志」（Write-ahead logging，缩写 WAL）是关系数据库系统中用于提供原子性和持久性（ACID 属性中的A和D）的一系列技术。在使用 WAL 的系统中，所有的修改在提交之前都要先写入redo/undo log 文件中。
- 事务commit时，数据变更动作放在redo log写入完成的动作之后，这样内存中的data page 就不需要同步写入disk，减少了disk写入次数。而redo log是顺序写，这样用顺序IO替代了data pege刷新的随机IO，减少了数据写入开销。
- 当事务需要rollback时，则使用undo log中的记录信息，将data page 数据恢复到事物开启之前的状态，来确保事物的原子性。
- 当服务意外终止后，可以依据disk中的data page 和 redo log执行 recovery，将数据恢复到crash的前一刻。

![RUNOOB 图标](https://github.com/tychusyuan/database-systems/raw/main/MySQL/img/writeaheadlog.png)

## checkpoint

- data page 使用的 buffer pool 不能可能缓存所有的数据，一旦free page 数量不足，则需要将dirty page刷到disk，并放回free list中，等待从disk load data page。
- wal的file size不可能无限增长，即便可以无限增长，一旦发生crash，需要recovery,此时因为庞大的log，则整个过程变得不可控。
- 当wal中的记录累积到一定的data page 需要刷到disk之后，数据库进程会执行checkpoint，data page 数据会被刷入disk，另外wal 的file space会被循环利用
- wal提升数据库进程处理性能，包括：
  - log file的 顺序IO替代随机IO，批量读写替代单条写入
  - data page 的 并发读写替代单线程读写，异步读写替代同步读写

## LSN
```sql
SHOW ENGINE INNODB STATUS\G
```
```sql
---
LOG
---
Log sequence number 16131164089282
Log flushed up to   16131163932862
Pages flushed up to 16130995063258
Last checkpoint at  16130995063258
Max checkpoint age    10433226609
Checkpoint age target 10107188278
Modified age          169026024
Checkpoint age        169026024
0 pending log flushes, 0 pending chkp writes
2413674629 log i/o's done, 818.95 log i/o's/second
```
- Log sequence number: redo lsn
- Log flushed up to : redo log flushed disk lsn
- Pages flushed up to : data pages flushed disk lsn
- Last checkpoint at : last checkpoint lsn

### LSN 存储位置
- data page
- redo log file
- checkpoint lsn
### data page Fil Header
|Name |Size|Remarks|
|:--|--|:--|
|FIL_PAGE_SPACE|4|4 ID of the space the page is in|
|FIL_PAGE_OFFSET|4|ordinal page number from start of space|
|FIL_PAGE_PREV|4|offset of previous page in key order|
|FIL_PAGE_NEXT|4|offset of next page in key order|
|FIL_PAGE_LSN|8|log serial number of page's latest log record|
|FIL_PAGE_TYPE|2|current defined types are: FIL_PAGE_INDEX, FIL_PAGE_UNDO_LOG, FIL_PAGE_INODE, FIL_PAGE_IBUF_FREE_LIST|
|FIL_PAGE_FILE_FLUSH_LSN|8|"the file has been flushed to disk at least up to this lsn" (log serial number), valid only on the first page of the file|
|FIL_PAGE_ARCH_LOG_NO|4|the latest archived log file number at the time that FIL_PAGE_FILE_FLUSH_LSN was written (in the log)|

## redo log

![RUNOOB 图标](https://github.com/tychusyuan/database-systems/raw/main/MySQL/img/redolog.png)

innodb_log_buffer_size

|Command-Line Format|	--innodb-log-buffer-size=#|
|--|--|
|System Variable|	innodb_log_buffer_size|
|Scope|	Global|
|Dynamic|	No|
|Type|	Integer|
|Default Value	|16777216|
|Minimum Value	|1048576|
|Maximum Value	|4294967295|

The size in bytes of the buffer that InnoDB uses to write to the log files on disk. The default value changed from 8MB to 16MB with the introduction of 32KB and 64KB innodb_page_size values. A large log buffer enables large transactions to run without the need to write the log to disk before the transactions commit. Thus, if you have transactions that update, insert, or delete many rows, making the log buffer larger saves disk I/O. For related information, see Memory Configuration, and Section 8.5.4, “Optimizing InnoDB Redo Logging”. For general I/O tuning advice, see Section 8.5.8, “Optimizing InnoDB Disk I/O”.

innodb_log_checkpoint_now

|Command-Line Format	|--innodb-log-checkpoint-now[={OFF|ON}]|
|System Variable	|innodb_log_checkpoint_now|
|Scope	|Global|
|Dynamic	|Yes|
|Type	|Boolean|
|Default Value	|OFF|
Enable this debug option to force InnoDB to write a checkpoint. This option is only available if debugging support is compiled in using the WITH_DEBUG CMake option.

innodb_log_checksums

|Command-Line Format	|--innodb-log-checksums[={OFF|ON}]
|System Variable	|innodb_log_checksums|
|Scope	|Global|
|Dynamic|	Yes|
|Type	|Boolean|
|Default Value|	ON|
Enables or disables checksums for redo log pages.

innodb_log_checksums=ON enables the CRC-32C checksum algorithm for redo log pages. When innodb_log_checksums is disabled, the contents of the redo log page checksum field are ignored.

Checksums on the redo log header page and redo log checkpoint pages are never disabled.

innodb_log_compressed_pages

|Command-Line Format|	--innodb-log-compressed-pages[={OFF|ON}]|
|System Variable	|innodb_log_compressed_pages|
|Scope	|Global|
|Dynamic	|Yes|
|Type	|Boolean|
|Default Value|	ON|
Specifies whether images of re-compressed pages are written to the redo log. Re-compression may occur when changes are made to compressed data.

innodb_log_compressed_pages is enabled by default to prevent corruption that could occur if a different version of the zlib compression algorithm is used during recovery. If you are certain that the zlib version is not subject to change, you can disable innodb_log_compressed_pages to reduce redo log generation for workloads that modify compressed data.

To measure the effect of enabling or disabling innodb_log_compressed_pages, compare redo log generation for both settings under the same workload. Options for measuring redo log generation include observing the Log sequence number (LSN) in the LOG section of SHOW ENGINE INNODB STATUS output, or monitoring Innodb_os_log_written status for the number of bytes written to the redo log files.

For related information, see Section 14.9.1.6, “Compression for OLTP Workloads”.

innodb_log_file_size

|Command-Line Format	|--innodb-log-file-size=#|
|System Variable	|innodb_log_file_size|
|Scope	|Global|
|Dynamic	|No|
|Type	|Integer|
|Default Value	|50331648|
|Minimum Value (≥ 5.7.11)	|4194304|
|Minimum Value (≤ 5.7.10)	|1048576|
|Maximum Value	|512GB / innodb_log_files_in_group|
|Unit	|bytes|
The size in bytes of each log file in a log group. The combined size of log files (innodb_log_file_size * innodb_log_files_in_group) cannot exceed a maximum value that is slightly less than 512GB. A pair of 255 GB log files, for example, approaches the limit but does not exceed it. The default value is 48MB.

Generally, the combined size of the log files should be large enough that the server can smooth out peaks and troughs in workload activity, which often means that there is enough redo log space to handle more than an hour of write activity. The larger the value, the less checkpoint flush activity is required in the buffer pool, saving disk I/O. Larger log files also make crash recovery slower.

The minimum innodb_log_file_size value was increased from 1MB to 4MB in MySQL 5.7.11.

For related information, see Redo Log File Configuration. For general I/O tuning advice, see Section 8.5.8, “Optimizing InnoDB Disk I/O”.

innodb_log_files_in_group

|Command-Line Format	|--innodb-log-files-in-group=#|
|System Variable	|innodb_log_files_in_group|
|Scope	|Global|
|Dynamic	|No|
|Type	|Integer|
|Default Value	|2|
|Minimum Value	|2|
|Maximum Value	|100|

The number of log files in the log group. InnoDB writes to the files in a circular fashion. The default (and recommended) value is 2. The location of the files is specified by innodb_log_group_home_dir. The combined size of log files (innodb_log_file_size * innodb_log_files_in_group) can be up to 512GB.

For related information, see Redo Log File Configuration.

innodb_log_group_home_dir

|Command-Line Format	|--innodb-log-group-home-dir=dir_name|
|System Variable	|innodb_log_group_home_dir|
|Scope	|Global|
||Dynamic	|No|
|Type	|Directory name|
The directory path to the InnoDB redo log files, whose number is specified by innodb_log_files_in_group. If you do not specify any InnoDB log variables, the default is to create two files named ib_logfile0 and ib_logfile1 in the MySQL data directory. Log file size is given by the innodb_log_file_size system variable.

For related information, see Redo Log File Configuration.

innodb_log_write_ahead_size

|Command-Line Format	--innodb-log-write-ahead-size=#|
|System Variable	|innodb_log_write_ahead_size|
|Scope	|Global|
|Dynamic	|Yes|
|Type	|Integer|
|Default Value	|8192|
|Minimum Value	|512 (log file block size)|
|Maximum Value	|Equal to innodb_page_size|
|Unit	|bytes|
Defines the write-ahead block size for the redo log, in bytes. To avoid “read-on-write”, set innodb_log_write_ahead_size to match the operating system or file system cache block size. The default setting is 8192 bytes. Read-on-write occurs when redo log blocks are not entirely cached to the operating system or file system due to a mismatch between write-ahead block size for the redo log and operating system or file system cache block size.

Valid values for innodb_log_write_ahead_size are multiples of the InnoDB log file block size (2n). The minimum value is the InnoDB log file block size (512). Write-ahead does not occur when the minimum value is specified. The maximum value is equal to the innodb_page_size value. If you specify a value for innodb_log_write_ahead_size that is larger than the innodb_page_size value, the innodb_log_write_ahead_size setting is truncated to the innodb_page_size value.

Setting the innodb_log_write_ahead_size value too low in relation to the operating system or file system cache block size results in “read-on-write”. Setting the value too high may have a slight impact on fsync performance for log file writes due to several blocks being written at once.

For related information, see Section 8.5.4, “Optimizing InnoDB Redo Logging”.
