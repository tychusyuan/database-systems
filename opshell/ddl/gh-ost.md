### 暂停
```shell
echo throttle | socat - ./gh-ost.sock
```
### 恢复
```shell
echo no-throttle | socat - ./gh-ost.sock
```
### 修改参数
```shell
echo chunk-size=100 | nc -U ./gh-ost.sock
```
```shell
echo max-lag-millis=200 | nc -U ./gh-ost.sock
```
```shell
echo max-load=Thread_running=3 | nc -U ./gh-ost.sock
```

### State: postponing cut-over 状态之后，删除cut.over.flag，则开始cut-over
### 创建throttle.flag 开始 pauses
```shell
./gh-ost \
-allow-on-master \
-assume-rbr \
-chunk-size 500 \
-exact-rowcount \
-max-load Threads_running=20 \
-critical-load Threads_running=64 \
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
-host localhost \
-port 3306 \
-user root \
-password 123456 \
-database db \
-table table \
-alter "" \
-verbose \
-execute 2>&1 | tee gh-ost.log

```
### 监控主从状态
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

### Interactive commands

`gh-ost` is designed to be operations friendly. To that effect, it allows the user to control its behavior even while it is running.

### Interactive interfaces

`gh-ost` listens on:

- Unix socket file: either provided via `--serve-socket-file` or determined by `gh-ost`, this interface is always up.
  When self-determined, `gh-ost` will advertise the identify of socket file upon start up and throughout the migration.
- TCP: if `--serve-tcp-port` is provided

Both interfaces may serve at the same time. Both respond to simple text command, which makes it easy to interact via shell.

### Known commands

- `help`: shows a brief list of available commands
- `status`: returns a detailed status summary of migration progress and configuration
- `sup`: returns a brief status summary of migration progress
- `coordinates`: returns recent (though not exactly up to date) binary log coordinates of the inspected server
- `applier`: returns the hostname of the applier
- `inspector`: returns the hostname of the inspector
- `chunk-size=<newsize>`: modify the `chunk-size`; applies on next running copy-iteration
- `dml-batch-size=<newsize>`: modify the `dml-batch-size`; applies on next applying of binary log events
- `max-lag-millis=<max-lag>`: modify the maximum replication lag threshold (milliseconds, minimum value is `100`, i.e. `0.1` second)
- `max-load=<max-load-thresholds>`: modify the `max-load` config; applies on next running copy-iteration
  - The `max-load` format must be: `some_status=<numeric-threshold>[,some_status=<numeric-threshold>...]`'
  - For example: `Threads_running=50,threads_connected=1000`, and you would then write/echo `max-load=Threads_running=50,threads_connected=1000` to the socket.
- `critical-load=<critical-load-thresholds>`: modify the `critical-load` config (exceeding these thresholds aborts the operation)
  - The `critical-load` format must be: `some_status=<numeric-threshold>[,some_status=<numeric-threshold>...]`'
  - For example: `Threads_running=1000,threads_connected=5000`, and you would then write/echo `critical-load=Threads_running=1000,threads_connected=5000` to the socket.
- `nice-ratio=<ratio>`: change _nice_ ratio: 0 for aggressive (not nice, not sleeping), positive integer `n`:
  - For any `1ms` spent copying rows, spend `n*1ms` units of time sleeping.
  - Examples: assume a single rows chunk copy takes `100ms` to complete.
    - `nice-ratio=0.5` will cause `gh-ost` to sleep for `50ms` immediately following.
    - `nice-ratio=1` will cause `gh-ost` to sleep for `100ms`, effectively doubling runtime
    - value of `2` will effectively triple the runtime; etc.
- `throttle-http`: change throttle HTTP endpoint
- `throttle-query`: change throttle query
- `throttle-control-replicas='replica1,replica2'`: change list of throttle-control replicas, these are replicas `gh-ost` will check. This takes a comma separated list of replica's to check and replaces the previous list.
- `throttle`: force migration suspend
- `no-throttle`: cancel forced suspension (though other throttling reasons may still apply)
- `unpostpone`: at a time where `gh-ost` is postponing the [cut-over](cut-over.md) phase, instruct `gh-ost` to stop postponing and proceed immediately to cut-over.
- `panic`: immediately panic and abort operation

### Querying for data

For commands that accept an argument as value, pass `?` (question mark) to _get_ current value rather than _set_ a new one.

### Examples

While migration is running:

```shell
$ echo status | nc -U /tmp/gh-ost.test.sample_data_0.sock
# Migrating `test`.`sample_data_0`; Ghost table is `test`.`_sample_data_0_gst`
# Migration started at Tue Jun 07 11:45:16 +0200 2016
# chunk-size: 200; max lag: 1500ms; dml-batch-size: 10; max-load: map[Threads_connected:20]
# Throttle additional flag file: /tmp/gh-ost.throttle
# Serving on unix socket: /tmp/gh-ost.test.sample_data_0.sock
# Serving on TCP port: 10001
Copy: 0/2915 0.0%; Applied: 0; Backlog: 0/100; Elapsed: 40s(copy), 41s(total); streamer: mysql-bin.000550:49942; ETA: throttled, flag-file
```

```shell
$ echo "chunk-size=250" | nc -U /tmp/gh-ost.test.sample_data_0.sock
# Migrating `test`.`sample_data_0`; Ghost table is `test`.`_sample_data_0_gst`
# Migration started at Tue Jun 07 11:56:03 +0200 2016
# chunk-size: 250; max lag: 1500ms; dml-batch-size: 10; max-load: map[Threads_connected:20]
# Throttle additional flag file: /tmp/gh-ost.throttle
# Serving on unix socket: /tmp/gh-ost.test.sample_data_0.sock
# Serving on TCP port: 10001
```

```shell
$ echo "chunk-size=?" | nc -U /tmp/gh-ost.test.sample_data_0.sock
250
```

```shell
$ echo throttle | nc -U /tmp/gh-ost.test.sample_data_0.sock

$ echo status | nc -U /tmp/gh-ost.test.sample_data_0.sock
# Migrating `test`.`sample_data_0`; Ghost table is `test`.`_sample_data_0_gst`
# Migration started at Tue Jun 07 11:56:03 +0200 2016
# chunk-size: 250; max lag: 1500ms; max-load: map[Threads_connected:20]
# Throttle additional flag file: /tmp/gh-ost.throttle
# Serving on unix socket: /tmp/gh-ost.test.sample_data_0.sock
# Serving on TCP port: 10001
Copy: 0/2915 0.0%; Applied: 0; Backlog: 0/100; Elapsed: 59s(copy), 59s(total); streamer: mysql-bin.000551:68067; ETA: throttled, commanded by user
```
