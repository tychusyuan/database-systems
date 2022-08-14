# mysqlbinlog

### row mode
```shell
mysqlbinlog -v --base64-output=DECODE-ROWS mysql-bin.xxx
```
### 按位置截取binlog
```shell
mysqlbinlog --start-position=185 --stop-position=338 mysql-bin.xxx > binlog1.txt
```
### 按时间截取binlog
```shell
mysqlbinlog --start-datetime="2010-01-07 11:25:56" --stop-datetime="2010-01-07 13:23:50" mysql-bin.xxx > binlog1.txt
```
```shell
mysqlbinlog mysql-bin.000044 mysql-bin.000045 mysql-bin.000046 mysql-bin.000047 mysql-bin.000048 mysql-bin.000049|grep -v 'Command-goods-updateStockStatus' |grep -B5 -i 'xm_goods' |grep -B5 '1774'
```
### 查看当前binlog文件组
```shell
show master logs;
```
### 查看当前使用的binlog文件
```shell
show binlog events;
```

### 刷新binlog文件组
```shell
flush logs;
```
```shell
reset master;
```

### 清除binlog
```shell
PURGE {MASTER | BINARY} LOGS TO ‘log_name’; //log_name不会被清除
```
```shell
PURGE {MASTER | BINARY} LOGS BEFORE ‘date’; //date不会被清除
```
```shell
purge master logs to ‘binlog.000004′;
```
```shell
purge master logs before ’2009-09-22 00:00:00′;
```

### 清除3天前的数据
```shell
PURGE MASTER LOGS BEFORE DATE_SUB( NOW( ), INTERVAL 3 DAY);
```


### 多文件，使用正则或
```shell
/opt/soft/mysql/bin/mysqlbinlog mysql-bin.000611 mysql-bin.000612 mysql-bin.000613 mysql-bin.000614|grep -B5 xm_unicom_info|grep -B5 -E '70686160|1120914052005070'
```

### 筛选binlog出错 unknown variable 'default-character-set=utf8'
```shell
/opt/soft/mysql/bin/mysqlbinlog mysql-bin.000067|grep 112062805318083801

/opt/soft/mysql/bin/mysqlbinlog: unknown variable 'default-character-set=utf8'

/opt/soft/mysql/bin/mysqlbinlog --no-defaults
```
