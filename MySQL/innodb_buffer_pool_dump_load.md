#

##

###
```sql
set global innodb_buffer_pool_dump_now=on;
```
```sql
SHOW STATUS LIKE 'Innodb_buffer_pool_dump_status';
```
```shell
nc remote_server 3305 < ib_buffer_pool
```
## 
### 
```shell
nc -l 3305 > ib_buffer_pool 
```
### 
```shell
set global innodb_buffer_pool_load_now=on;
```
```sql
SHOW STATUS LIKE 'Innodb_buffer_pool_dump_status';
```
