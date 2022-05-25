# Bash

### ping with datetime
```shell
ping host | while read pong; do echo "$(date): $pong"; done
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
