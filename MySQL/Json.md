```sql
mysql> select * from t1;
+----------------------------------------+------+
| data                                   | id   |
+----------------------------------------+------+
| {"key1": "value1", "key2": "VALUE2"}   |    1 |
| {"key2": "VALUE2"}                     |    2 |
| {"key2": "VALUE2"}                     |    1 |
| {"a": "x", "b": "y", "key2": "VALUE2"} |    1 |
+----------------------------------------+------+
4 rows in set (0.00 sec)

mysql> update t1 set data = JSON_SET(data, "$.key2", "I am ID2") where id = 2;
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from t1;
+----------------------------------------+------+
| data                                   | id   |
+----------------------------------------+------+
| {"key1": "value1", "key2": "VALUE2"}   |    1 |
| {"key2": "I am ID2"}                   |    2 |
| {"key2": "VALUE2"}                     |    1 |
| {"a": "x", "b": "y", "key2": "VALUE2"} |    1 |
+----------------------------------------+------+
4 rows in set (0.00 sec)

mysql> update t1 set data = JSON_SET(data, "$.key3", "I am ID3") where id = 2;
Query OK, 1 row affected (0.07 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from t1;
+------------------------------------------+------+
| data                                     | id   |
+------------------------------------------+------+
| {"key1": "value1", "key2": "VALUE2"}     |    1 |
| {"key2": "I am ID2", "key3": "I am ID3"} |    2 |
| {"key2": "VALUE2"}                       |    1 |
| {"a": "x", "b": "y", "key2": "VALUE2"}   |    1 |
+------------------------------------------+------+
4 rows in set (0.00 sec)
```
