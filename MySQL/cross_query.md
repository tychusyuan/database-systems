```sql
CREATE TABLE `studentscore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `subject` varchar(32) NOT NULL,
  `score` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
```
```sql
insert studentscore (`name`,`subject`,`score`) values ('张三','语文','60');
insert studentscore (`name`,`subject`,`score`) values ('张三','数学','65');
insert studentscore (`name`,`subject`,`score`) values ('张三','外语','70');
insert studentscore (`name`,`subject`,`score`) values ('李四','语文','80');
insert studentscore (`name`,`subject`,`score`) values ('李四','数学','90');
insert studentscore (`name`,`subject`,`score`) values ('李四','外语','85');
insert studentscore (`name`,`subject`,`score`) values ('王五','语文','70');
insert studentscore (`name`,`subject`,`score`) values ('王五','数学','71');
insert studentscore (`name`,`subject`,`score`) values ('王五','外语','75');
insert studentscore (`name`,`subject`,`score`) values ('赵六','语文','64');
insert studentscore (`name`,`subject`,`score`) values ('赵六','数学','67');
insert studentscore (`name`,`subject`,`score`) values ('赵六','外语','76');
```
```sql
select * from studentscore;
+----+--------+---------+-------+
| id | name   | subject | score |
+----+--------+---------+-------+
|  1 | 张三   | 语文    |    60 |
|  2 | 张三   | 数学    |    65 |
|  3 | 张三   | 外语    |    70 |
|  4 | 李四   | 语文    |    80 |
|  5 | 李四   | 数学    |    90 |
|  6 | 李四   | 外语    |    85 |
|  7 | 王五   | 语文    |    70 |
|  8 | 王五   | 数学    |    71 |
|  9 | 王五   | 外语    |    75 |
| 10 | 赵六   | 语文    |    64 |
| 11 | 赵六   | 数学    |    67 |
| 12 | 赵六   | 外语    |    76 |
+----+--------+---------+-------+
```
```sql
select `name`,case when `subject`='语文' then `score` else 0 end as '语文' from studentscore group by `name`,`subject`,`score`;
+--------+--------+
| name   | 语文   |
+--------+--------+
| 张三   |      0 |
| 张三   |      0 |
| 张三   |     60 |
| 李四   |      0 |
| 李四   |      0 |
| 李四   |     80 |
| 王五   |      0 |
| 王五   |      0 |
| 王五   |     70 |
| 赵六   |      0 |
| 赵六   |      0 |
| 赵六   |     64 |
+--------+--------+
```
```sql
select `name`, 
sum(case when `subject`='语文' then `score` else 0 end) as '语文', 
sum(case when `subject`='数学' then `score` else 0 end) as '数学', 
sum(case when `subject`='外语' then `score` else 0 end) as '外语' 
from studentscore group by `name`;
+--------+--------+--------+--------+
| name   | 语文   | 数学   | 外语   |
+--------+--------+--------+--------+
| 张三   |     60 |     65 |     70 |
| 李四   |     80 |     90 |     85 |
| 王五   |     70 |     71 |     75 |
| 赵六   |     64 |     67 |     76 |
+--------+--------+--------+--------+
```
