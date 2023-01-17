
```sql
select d.*,b.*,e.*,c.* from information_schema.innodb_lock_waits as a  
inner join information_schema.innodb_locks as b on b.lock_trx_id = a.blocking_trx_id  
inner join information_schema.innodb_locks as c on c.lock_trx_id = a.requesting_trx_id 
inner join information_schema.innodb_trx as d on d.trx_id = a.blocking_trx_id 
inner join information_schema.innodb_trx as e on e.trx_id = a.requesting_trx_id\G
```
### 锁等待
```sql
 SELECT p2.`HOST` AS 被阻塞方host, p2.`USER` AS 被阻塞方用户, r.trx_id AS 被阻塞方事务id, r.trx_mysql_thread_id AS 被阻塞方线程号
    , TIMESTAMPDIFF(SECOND, r.trx_wait_started, CURRENT_TIMESTAMP) AS 等待时间
    , r.trx_query AS 被阻塞的查询, l.lock_table AS 阻塞方锁住的表, m.`lock_mode` AS 被阻塞方的锁模式, m.`lock_type` AS "被阻塞方的锁类型(表锁还是行锁)", m.`lock_index` AS 被阻塞方锁住的索引
    , m.`lock_space` AS 被阻塞方锁对象的space_id, m.lock_page AS 被阻塞方事务锁定页的数量, m.lock_rec AS 被阻塞方事务锁定行的数量, m.lock_data AS 被阻塞方事务锁定记录的主键值, p.`HOST` AS 阻塞方主机
    , p.`USER` AS 阻塞方用户, b.trx_id AS 阻塞方事务id, b.trx_mysql_thread_id AS 阻塞方线程号, b.trx_query AS 阻塞方查询, l.`lock_mode` AS 阻塞方的锁模式
    , l.`lock_type` AS "阻塞方的锁类型(表锁还是行锁)", l.`lock_index` AS 阻塞方锁住的索引, l.`lock_space` AS 阻塞方锁对象的space_id, l.lock_page AS 阻塞方事务锁定页的数量, l.lock_rec AS 阻塞方事务锁定行的数量
    , l.lock_data AS 阻塞方事务锁定记录的主键值
    , IF(p.COMMAND = 'Sleep', CONCAT(p.TIME, ' 秒'), 0) AS 阻塞方事务空闲的时间
FROM information_schema.INNODB_LOCK_WAITS w
    INNER JOIN information_schema.INNODB_TRX b ON b.trx_id = w.blocking_trx_id
    INNER JOIN information_schema.INNODB_TRX r ON r.trx_id = w.requesting_trx_id
    INNER JOIN information_schema.INNODB_LOCKS l
    ON w.blocking_lock_id = l.lock_id
        AND l.`lock_trx_id` = b.`trx_id`
    INNER JOIN information_schema.INNODB_LOCKS m
    ON m.`lock_id` = w.`requested_lock_id`
        AND m.`lock_trx_id` = r.`trx_id`
    INNER JOIN information_schema.PROCESSLIST p ON p.ID = b.trx_mysql_thread_id
    INNER JOIN information_schema.PROCESSLIST p2 ON p2.ID = r.trx_mysql_thread_id
ORDER BY 等待时间 DESC\G
```
