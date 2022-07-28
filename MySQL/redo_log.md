# redo log

## WAL (Write Ahead Log)

- 「预写式日志」（Write-ahead logging，缩写 WAL）是关系数据库系统中用于提供原子性和持久性（ACID 属性中的A和D）的一系列技术。在使用 WAL 的系统中，所有的修改在提交之前都要先写入redo/undo log 文件中。
- 事务commit时，数据变更动作放在redo log写入完成的动作之后，这样内存中的data page 就不需要同步写入disk，减少了disk写入次数。而redo log是顺序写，这样用顺序IO替代了data pege刷新的随机IO，减少了数据写入开销。
- 当事务需要rollback时，则使用undo log中的记录信息，将data page 数据恢复到事物开启之前的状态，来确保事物的原子性。
- 当服务意外终止后，可以依据disk中的data page 和 redo log执行 recovery，将数据恢复到crash的前一刻。

## checkpoint

- data page 使用的 buffer pool 不能可能缓存所有的数据，一旦free page 数量不足，则需要将dirty page刷到disk，并放回free list中，等待从disk load data page。
- wal的file size不可能无限增长，即便可以无限增长，一旦发生crash，需要recovery,此时因为庞大的log，则整个过程变得不可控。
- 当wal中的记录累积到一定的data page 需要刷到disk之后，数据库进程会执行checkpoint，data page 数据会被刷入disk，另外wal 的file space会被循环利用
- wal提升数据库进程处理性能，包括：
  - log file的 顺序IO替代随机IO，批量读写替代单条写入
  - data page 的 并发读写替代单线程读写，异步读写替代同步读写
