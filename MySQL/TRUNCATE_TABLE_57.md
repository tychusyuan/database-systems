# TRUNCATE TABLE at MySQL 5.7

## 8.0 版本之后可以直接 truncate table
首先为了保证修改能尽量的稳定，在满足需求的前提下，需要能够动态开关和尽量减少对原有逻辑的侵入。8.0之前的ddl都不是原子的，但是为了尽可提 高ddl的原子性，在分析了innodb层的几个相关接口后，如果选择直接把delete和create接口修改字典数据放到一个事务里改动比较大, 尤其是对delete接口的 改造，而把rename+create放到一个事务里相对简单，这样我们就可以把truncate修改为 rename + create 一个事务里修改字典数据，它成功后再把rename的 临时表删除。 truncate table t 修改为:rename t to #sqlxxxx; // 重命名到临时表 create table t;这个修改字典表和rename在一个事务里，如果失败字典表就还是老表 delete #sqlxxxx; // 删除之前的临时表减少对原有代码的侵入 选择判断一些前置条件：

## 5.7版本 流程
```sql
START TRANSACTION;
CREATE TABLE dev_tab_new LIKE dev_tab; 
RENAME TABLE dev_tab TO dev_tab_old; 
RENAME TABLE dev_tab_new TO dev_tab; 
DROP TABLE dev_tab_old;
COMMIT;
```
