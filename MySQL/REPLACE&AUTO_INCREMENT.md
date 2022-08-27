
### 主从切换发现 AUTO_INCREMENT 有回退现象
```sql
#220825 14:25:49 server id 172327364  end_log_pos 1033382027 	Table_map: `userScene`.`userSceneIdGenerator` mapped to number 28790
# at 1033382027
#220825 14:25:49 server id 172327364  end_log_pos 1033382085 	Update_rows: table id 28790 flags: STMT_END_F
### UPDATE `userScene`.`userSceneIdGenerator`
### WHERE
###   @1=2714486723
###   @2=0
### SET
###   @1=2714371687
###   @2=0
# at 1033382085
#220825 14:25:49 server id 172327364  end_log_pos 1033382112 	Xid = 22244756938
COMMIT/*!*/;
# at 1033382112
```

### 发现从库 AUTO_INCREMENT和 表中数据不一致
```sql
select * from userSceneIdGenerator ; show create table userSceneIdGenerator;
+------------+------+
| us_id      | stub |
+------------+------+
| 2714886180 |    0 |
+------------+------+
1 row in set (0.20 sec)

+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table                | Create Table                                                                                                                                                                                                                                          |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| userSceneIdGenerator | CREATE TABLE `userSceneIdGenerator` (
  `us_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `stub` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`us_id`),
  UNIQUE KEY `unique_key` (`stub`)
) ENGINE=InnoDB AUTO_INCREMENT=2714884845 DEFAULT CHARSET=utf8 |
+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.19 sec)
```
### dev 给出的sql 是 ，replace
```sql
REPLACE INTO userScene.userSceneIdGenerator (stub) values(0)
```

### 原来问题在于 replace 语句在binlog中被改写为 update 语句，无法像 insert 语句一样触发 AUTO_INCREMENT 自增
### 解决方案 1 开启事务，确保 业务逻辑 先delete 再 insert
```sql
begin;delete from userSceneIdGenerator where stub=0;insert userSceneIdGenerator (stub) values (0);commit;
```
### 解决方案 2 使用LAST_INSERT_ID来实现AUTO_INCREMENT 自增
```sql
CREATE TABLE sequence(tablename VARCHAR(64) NOT NULL,id BIGINT UNSIGNED NOT NULL DEFAULT 1,PRIMARY KEY (tablename)) ENGINE=INNODB;
```
```sql
BEGIN
INSERT INTO sequence (tablename) VALUES (tname) ON DUPLICATE KEY UPDATE id=LAST_INSERT_ID(id+1);
SELECT LAST_INSERT_ID();
END
```
### 解决方案 3 update 是 set 变量，再select 变量，来模拟自增
```sql
CREATE TABLE `testupdate` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `val` bigint(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8
```
#### 开启事务是非必须的，只要保证update 和 select 是在同一个会话中完成即可
```sql
update testupdate
set val = val+1
where id = 1 and @value := val+1;

select @value;
```
### 解决方案 4 全局唯一id生成器，snowflake 或者 美团 leaf 
https://github.com/Meituan-Dianping/Leaf
