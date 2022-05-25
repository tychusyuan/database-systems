# innodb_buffer_pool_dump & load

## dump 
使用物理备份并恢复的从库表空间id 和主库一致，可以使用主库 dump 文件预热

### 开始dump
```sql
set global innodb_buffer_pool_dump_now=on;
```
### 观察dump 结果
```sql
SHOW STATUS LIKE 'Innodb_buffer_pool_dump_status';
```
### nc 到从库
```shell
nc remote_server 3305 < ib_buffer_pool
```
## load
### 接收 主库传过来的 文件
```shell
nc -l 3305 > ib_buffer_pool 
```
### 开始load
```shell
set global innodb_buffer_pool_load_now=on;
```
### 观察 load 情况
```sql
SHOW STATUS LIKE 'Innodb_buffer_pool_dump_status';
```
