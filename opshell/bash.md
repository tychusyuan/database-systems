# Bash

### 生成 rsa key
```shell
ssh-keygen -t rsa
```

### 主机 信任
```shell
 ssh-copy-id remoteuser@remoteserver
```

### ping with datetime
```shell
ping host | while read pong; do echo "$(date): $pong"; done
```
### 按内存排序
```shell
ps aux --sort=+rss
```

### MySQL 内存观察 writeable/private 是否增长
```shell
while true; do pmap -d  24645  | tail -1; sleep 2; done
mapped: 103010548K    writeable/private: 91757448K    shared: 320K
mapped: 103010548K    writeable/private: 91757448K    shared: 320K
mapped: 103010548K    writeable/private: 91757448K    shared: 320K
mapped: 103010548K    writeable/private: 91757448K    shared: 320K
mapped: 103010548K    writeable/private: 91757448K    shared: 320K
mapped: 103010548K    writeable/private: 91757448K    shared: 320K
mapped: 103010548K    writeable/private: 91757448K    shared: 320K
mapped: 103010548K    writeable/private: 91757448K    shared: 320K
mapped: 103010548K    writeable/private: 91757448K    shared: 320K
```

###
```shell
pmap -X -p 24645 > memmysql.log
```

### 内存使用
```shell
ps eo user,pid,vsz,rss $(pgrep -f 'mysqld')
USER       PID    VSZ   RSS
work     22833 113456     4
work     24645 103010544 60765528
```
### 专有网络ip
```shell
ifconfig | grep 'inet addr' | cut -d ':' -f 2 | awk '{ print $1 }' | grep -E '^(192\.168|10\.|172\.1[6789]\.|172\.2[0-9]\.|172\.3[01]\.)'
```

### gzip 压缩解压保留原文件
```shell
gzip -c aa > aa.gz
```
```shell
gzip -dc bb.gz > bb
```
