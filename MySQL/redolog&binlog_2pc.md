 MySQL事务提交的时候，需要同时完成redo log和binlog的提交，为了保证两个日志的一致性，需要用到两阶段提交（与分布式的两阶段提交不同，这里的两阶段提交是发生在数据库内部）
 

数据库两阶段提交的流程
假设执行一条SQL语句：

update T set c=c+1 where ID=2;
复制
流程如下图所示（图片来自MySQL实战45讲）：
 
![RUNOOB 图标](https://github.com/tychusyuan/database-systems/raw/main/MySQL/img/mysql2pc01.png)

两阶段流程

从图中可以看出，在最后提交事务的时候，需要有3个步骤：

写入redo log，处于prepare状态
写binlog
修改redo log状态为commit
 ps: redo log的提交分为prepare和commit两个阶段，所以称之为两阶段提交 
为什么需要两阶段提交？
假设当前 ID=2 的行，字段 c 的值是 0，再假设执行 update 语句过程中在写完第一个日志后，第二个日志还没有写完期间发生了 crash，会出现什么情况呢？

先写 redo log 后写 binlog。假设在 redo log 写完，binlog 还没有写完的时候，MySQL 进程异常重启。由于我们前面说过的，redo log 写完之后，系统即使崩溃，仍然能够把数据恢复回来，所以恢复后这一行 c 的值是 1。但是由于 binlog 没写完就 crash 了，这时候 binlog 里面就没有记录这个语句。因此，之后备份日志的时候，存起来的 binlog 里面就没有这条语句。然后你会发现，如果需要用这个 binlog 来恢复临时库的话，由于这个语句的 binlog 丢失，这个临时库就会少了这一次更新，恢复出来的这一行 c 的值就是 0，与原库的值不同。
先写 binlog 后写 redo log。如果在 binlog 写完之后 crash，由于 redo log 还没写，崩溃恢复以后这个事务无效，所以这一行 c 的值是 0。但是 binlog 里面已经记录了“把 c 从 0 改成 1”这个日志。所以，在之后用 binlog 来恢复的时候就多了一个事务出来，恢复出来的这一行 c 的值就是 1，与原库的值不同。
可以看到，如果不使用“两阶段提交”，那么数据库的状态就有可能和用它的日志恢复出来的库的状态不一致。

如何完成崩溃恢复
流程中崩溃可能导致问题如下图：

![RUNOOB 图标](https://github.com/tychusyuan/database-systems/raw/main/MySQL/img/mysql2pc02.png)

崩溃恢复

如果在图中时刻 A 的地方，也就是写入 redo log 处于 prepare 阶段之后、写 binlog 之前，发生了崩溃（crash），由于此时 binlog 还没写，redo log 也还没提交，所以崩溃恢复的时候，这个事务会回滚。这时候，binlog 还没写，所以也不会传到备库。

如果 redo log 里面的事务是完整的，也就是已经有了 commit 标识，则直接提交；如果 redo log 里面的事务只有完整的 prepare，则判断对应的事务 binlog 是否存在并完整：

a. 如果是，则提交事务；
b. 否则，回滚事务。
这里，时刻 B 发生 crash 对应的就是 2(a) 的情况，崩溃恢复过程中事务会被提交。

ps: 两阶段提交的最后一个阶段的操作本身是不会失败的，除非是系统或硬件错误，所以也就不再需要回滚（不然就可以无限循环下去了）

## sync_binlog

|Command-Line Format	|--sync-binlog=#|
|--|--|
|System Variable	|sync_binlog|
|Scope	|Global|
|Dynamic	|Yes|
|SET_VAR Hint Applies	|No|
|Type	|Integer|
|Default Value	|1|
|Minimum Value	|0|
|Maximum Value	|4294967295|

Controls how often the MySQL server synchronizes the binary log to disk.

sync_binlog=0: Disables synchronization of the binary log to disk by the MySQL server. Instead, the MySQL server relies on the operating system to flush the binary log to disk from time to time as it does for any other file. This setting provides the best performance, but in the event of a power failure or operating system crash, it is possible that the server has committed transactions that have not been synchronized to the binary log.

sync_binlog=1: Enables synchronization of the binary log to disk before transactions are committed. This is the safest setting but can have a negative impact on performance due to the increased number of disk writes. In the event of a power failure or operating system crash, transactions that are missing from the binary log are only in a prepared state. This permits the automatic recovery routine to roll back the transactions, which guarantees that no transaction is lost from the binary log.

sync_binlog=N, where N is a value other than 0 or 1: The binary log is synchronized to disk after N binary log commit groups have been collected. In the event of a power failure or operating system crash, it is possible that the server has committed transactions that have not been flushed to the binary log. This setting can have a negative impact on performance due to the increased number of disk writes. A higher value improves performance, but with an increased risk of data loss.

For the greatest possible durability and consistency in a replication setup that uses InnoDB with transactions, use these settings:
sync_binlog=1.
innodb_flush_log_at_trx_commit=1.
