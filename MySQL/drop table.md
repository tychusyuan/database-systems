
## drop 表防止被 hang住 ，有两个层面，内存和磁盘
### buffer pool中会对需要删除表对应的data page 进行清除，无需 flush
### 删除磁盘上的idb 文件

## 应对方案
### 应对内存清理 data page 的方案是 先rename，再drop
### 应对删除大文件 则使用 硬链接
```shell
sudo ln test.idb test.idb.hdlk
```
## 清理磁盘文件
### 使用truncate时，SIZE参数必须是整数和可选单位（例如：10K是10*1024）。使用的单位是K、M、G、T、P、E、Z、Y（1024的幂）或KB、MB、…（1000的幂）。
```shell
touch file.txt
```
```shell
truncate -s 100K file.txt
```
```shell
truncate -s +200K file.txt
```
```shell
truncate -s -250K file.txt
```
