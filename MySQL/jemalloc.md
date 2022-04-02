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
jemalloc_lib="/home/work/mysql/lib/libjemalloc.so"
```

## 在文件中找到 Add jemalloc to ld_preload 部分，因为默认只在4个目录中查找，所以自己append 一段

```shell
#
# Add jemalloc to ld_preload if no other malloc forced - needed for TokuDB
#
if test $load_jemalloc -eq 1
then
  for libjemall in "${MY_BASEDIR_VERSION}/lib/mysql" "/usr/lib64" "/usr/lib/x86_64-linux-gnu" "/usr/lib"; do
    if [ -r "$libjemall/libjemalloc.so.1" ]; then
      add_mysqld_ld_preload "$libjemall/libjemalloc.so.1"
      break
    fi
  done
fi
# 以下三行就是让mysqld启动时调用上面编译的jemalloc
if [ -r "$jemalloc_lib" ]; then
  add_mysqld_ld_preload "$jemalloc_lib"
fi
```

## 启动mysql后，检查是否使用jemalloc

```shell
sudo lsof -Pn -p $(pidof mysqld) | grep jemalloc
mysqld  15815 work  mem       REG             253,33    4395840 41962974 /home/work/mysql/lib/libjemalloc.so.2
```
