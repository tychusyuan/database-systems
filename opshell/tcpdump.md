
### 利用组合器
```shell
tcpdump -i eth0 tcp -nn 'port 12345 and host 10.0.0.1' -vvv  -w tcp_retry.pcap
```
### 利用nc
```shell
tcpdump -i eth0 tcp -nn 'port 55125 and host 10.51.24.66' -vvv -w - | nc 10.58.126.1 8555
```

### 接收
```shell
nc -l 8555 > 55125.pcap
```

### 解析 pcap
```shell
tcpdump -r 55125.pcap >> tcp.log
```
