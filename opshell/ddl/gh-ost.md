
###
```shell
./gh-ost --host=172.30.4.235 --port=3306 --user=sbtest --password=sbtest --database=sbtest1 --table=sbtest1 --alter="ENGINE=InnoDB" --chunk-size=2000 --max-load=Threads_connected=20
```

###
```shell
./gh-ost --host=172.30.4.235 --port=3306 --user=sbtest --password=sbtest --database=sbtest1 --table=sbtest1 --alter="ENGINE=InnoDB" --chunk-size=2000 --max-load=Threads_connected=20 --test-on-replica --execute
```
