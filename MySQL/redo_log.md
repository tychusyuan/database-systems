# redo log

## WAL (Write Ahead Log)

「预写式日志」（Write-ahead logging，缩写 WAL）是关系数据库系统中用于提供原子性和持久性（ACID 属性中的A和D）的一系列技术。在使用 WAL 的系统中，所有的修改在提交之前都要先写入redo/undo log 文件中。
事务commit时，数据变更动作放在redo log写入完成的动作之后，这样内存中的data page 就不需要同步写入disk，减少了disk写入次数。而redo log是顺序写，这样用顺序IO替代了data pege刷新的随机IO，减少了数据写入开销。
当事务需要rollback时，则使用undo log，来确保事物的原子性。
当服务意外终止后，可以依据disk中的data page 和 redo log将数据恢复到crash的前一刻。

## checkpoint

