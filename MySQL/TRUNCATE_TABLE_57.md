# TRUNCATE TABLE at MySQL 5.7


truncate table会比drop table在删除buffer pool page慢的本质原因，是因为truncate table 需要复用space id, 这导致必须把buffer pool中的老的表中的页全部删除，而drop table因为新旧表的页可用通过space id区分，只需要把flush list中的脏页删除就可以了，也就是可以用drop+create代替truncate来解决大buffer pool夯的问题，很遗憾这个修改实际上是在8.0上做的，也就是5.7我们需要自己实现
## 8.0 版本之后可以直接 truncate table
```sql
TRUNCATE TABLE tbl_name;
```


## 5.7版本 流程
```sql
START TRANSACTION;
CREATE TABLE dev_tab_new LIKE dev_tab; 
RENAME TABLE dev_tab TO dev_tab_old; 
RENAME TABLE dev_tab_new TO dev_tab; 
DROP TABLE dev_tab_old;
COMMIT;
```
