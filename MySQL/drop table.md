
### drop 表防止被 hang住 ，有两个层面，内存和磁盘
### buffer pool中会对需要删除表对应的data page 进行清除，无需 flush
### 删除磁盘上的idb 文件

### 应对内存清理 data page 的方案是 先rename，再drop
### 应对删除大文件 则使用 硬链接
```shell
sudo ln test.idb test.idb.hdlk
```
