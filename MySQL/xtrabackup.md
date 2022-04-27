# Xtrabackup

## backup 通过 管道 发送给目标服务器

### 发送端服务器执行
```shell
innobackupex --defaults-file={BACKUP_MY.CNF} --ibbackup=xtrabackup --lock-wait-threshold=40 --lock-wait-query-type=all --lock-wait-timeout=180 --kill-long-queries-timeout=20 --kill-long-query-type=all --parallel=8 --host={LOCALHOST} --port={PORT} --user={ADMIN} --password={PASSWORD} {BACKUP_DIR} --no-timestamp --stream=xbstream | nc {HOST} {PORT}
```
### 接收端服务器执行
```shell
nc -l {PORT} | xbstream -x
```
### 接收完毕后，执行apply-log
```shell
innobackupex --ibbackup=xtrabackup --parallel=8 --apply-log --use-memory=4G --defaults---defaults-file=./backup-my.cnf  ./
```

## 使用本地 unix socket，传输之前使用过lz4 压缩
```shell
# 发送端服务器执行
/home/work/app/xtrabackup/innobackupex --ibbackup=/home/work/app/xtrabackup/xtrabackup --lock-wait-threshold=40 --lock-wait-query-type=all --lock-wait-timeout=180 --kill-long-queries-timeout=20 --kill-long-query-type=all --parallel=8 --defaults-file= ${BACKUP_CNF} --socket=${BACKUP_SOCK} --user={BACKUP_USER} --password=${BACKUP_PWD} ${BAK} --no-timestamp --stream=xbstream | lz4 -B4 | nc {HOST} {PORT}
# 接收端服务器执行
nc -l {PORT} | lz4 -B7 -d | /home/work/app/xtrabackup/xbstream -x
# 接收完毕后，执行apply-log
/home/work/app/xtrabackup/innobackupex --ibbackup=/home/work/app/xtrabackup/xtrabackup --parallel=8 --apply-log --use-memory=4G --defaults---defaults-file=./backup-my.cnf  ./
```
