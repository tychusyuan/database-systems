# nc ipv6
## 安装 netcat-openbsd
```shell
apt install netcat-openbsd
```
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
## 传递目录
### recv
```shell
nc -6l 8080 | tar -xf -
```
### send
```shell
tar -cf - test | nc -q 1 -6nv 0:0:0:0:0:0:0:1 8080
```
## 压缩文件后传输
### recv
```shell
nc -6l 8080 | zstd -d > test.log
```
### send , 压缩级别 1 ，压缩线程 8
```shell
cat test.log | zstd -1 -T8 - | nc -q 1 -6nv 0:0:0:0:0:0:0:1 8080
```
## 压缩目录后传输
### recv
```shell
nc -6l 8080 | zstd -d |tar -xf -
```
### send
```shell
tar -cf - test | zstd -1 -T8 - | nc -q 1 -6nv 0:0:0:0:0:0:0:1 8080
```
