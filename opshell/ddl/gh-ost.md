### 
```shell
./gh-ost \
-allow-on-master \
-assume-rbr \
-chunk-size 500 \
-exact-rowcount \
-max-load Threads_running=20 \
-critical-load Threads_connected=64,Connections=10240 \
-critical-load-interval-millis 600 \
-cut-over atomic \
-cut-over-lock-timeout-seconds 3 \
-nice-ratio 1 \
-default-retries 60 \
-heartbeat-interval-millis 500 \
-serve-socket-file ./gh-ost.sock \
-throttle-flag-file ./throttle.flag \
-postpone-cut-over-flag-file ./cut.over.flag \
-panic-flag-file ./ghost.panic.flag \
-throttle-additional-flag-file ./throttle.additional.flag \
-max-lag-millis 1500 \
-throttle-control-replica=192.16.12.22:3306,192.16.12.23:3307,192.16.13.12:3308 \
-host \
-port \
-user \
-password \
-database \
-table \
-alter "" \
-verbose \
-execute 2>&1 | tee gh-ost.log
```

###
```shell
./gh-ost --host=127.0.0.1 --port=3306 --user=sbtest --password=sbtest --database=sbtest1 --table=sbtest1 --alter="ENGINE=InnoDB" --chunk-size=2000 --max-load=Threads_connected=20
```

###
```shell
./gh-ost -allow-on-master -assume-rbr -exact-rowcount -host 127.0.0.1 -port 3306 -user root -ask-pass --database=sbtest --table=sbtest1 --alter="ENGINE=InnoDB" --chunk-size=2000 --max-load=Threads_connected=2000 --execute
```

###
```shell
gh-ost -allow-on-master -assume-rbr -exact-rowcount 
    -critical-load Threads_running=20 -critical-load-hibernate-seconds 60 
    -chunk-size 500 -max-load Threads_running=20 -nice-ratio 0.1 
    -database ghost -table sbtest1  
    -host 127.0.0.1 -port 3306 -user percona -ask-pass
    -postpone-cut-over-flag-file /home/ubuntu/gh-ost-sentinel 
    -throttle-additional-flag-file /home/ubuntu/gh-ost-throttle_ghost.sbtest1 
    -alter 'ENGINE=InnoDB' 
    -verbose -execute 2>&1 | tee gh-ost.log
```
