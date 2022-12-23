# nc ipv6

## tcp传递文件
### recv
```shell
nc -6l 8080 > test.log
```
### send
```shell
nc -q 1 -6nv 0:0:0:0:0:0:0:1 8080 < test.log
```
## udp传递文件
### recv
```shell
nc -6ul 8080 > test.log
```
### send
```shell
nc -q 1 -6unv 0:0:0:0:0:0:0:1 8080 < test.log
```
### 传递目录
