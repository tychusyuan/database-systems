
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
