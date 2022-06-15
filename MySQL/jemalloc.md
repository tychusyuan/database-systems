# jemalloc for MySQL 5.7

## 编译安装 jemalloc

```shell
wget https://github.com/jemalloc/jemalloc/releases/download/5.2.1/jemalloc-5.2.1.tar.bz2
tar jxf jemalloc-5.2.1.tar.bz2
cd jemalloc-5.2.1/
# 安装目录请依据企业规范
./configure --prefix=/home/work/mysql
make && make install
```

## 修改 msyqld_safe 启动mysqld时使用jemalloc

```shell
vim /home/work/mysql/bin/mysqld_safe
# 在文件头部添加
export LD_PRELOAD="/home/work/app/mysql/lib/libjemalloc.so"
```

## 启动mysql后，检查是否使用jemalloc
```shell
lsof -Pn -p $(pidof mysqld) | grep jemalloc

```
```shell
for id in $(pidof mysqld); do lsof -Pn -p $id | grep jemalloc;done
```
```shell
lsof -Pn -p $(pidof mysqld) | grep jemalloc
mysqld  15815 work  mem       REG             253,33    4395840 41962974 /home/work/mysql/lib/libjemalloc.so.2
```
