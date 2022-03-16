# Compiling Percona5.7 On Ubuntu

```shell
sudo apt install gcc g++ libaio-dev libncurses5-dev libreadline-dev libcurl4-openssl-dev
```

## openssl
```shell
wget https://www.openssl.org/source/openssl-1.1.1n.tar.gz
tar zxf openssl-1.1.1n.tar.gz
cd openssl-1.1.1n/
./config --prefix=/home/tudou/app/openssl-1.1.1n
make && make install
```

## 编译安装
```shell
wget https://downloads.percona.com/downloads/Percona-Server-5.7/Percona-Server-5.7.36-39/source/tarball/percona-server-5.7.36-39.tar.gz
tar zxf percona-server-5.7.36-39.tar.gz
cd percona-server-5.7.36-39/
wget http://sourceforge.net/projects/boost/files/boost/1.59.0/boost_1_59_0.tar.bz2
tar jxf boost_1_59_0.tar.bz2
cmake . -DCMAKE_INSTALL_PREFIX=/home/tudou/app/percona-server-5.7.36-39 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBUILD_CONFIG=mysql_release -DFEATURE_SET=community -DWITH_EMBEDDED_SERVER=OFF -DDOWNLOAD_BOOST=1 -DWITH_BOOST=boost_1_59_0 -DWITHOUT_ROCKSDB_STORAGE_ENGINE=1 -DWITHOUT_TOKUDB_STORAGE_ENGINE=1 -DWITH_SSL=/home/tudou/app/openssl-1.1.1n -DWITH_ZLIB=bundled
make -j 20
make install
```

## 编译 jemalloc
```shell
wget https://github.com/jemalloc/jemalloc/releases/download/5.2.1/jemalloc-5.2.1.tar.bz2
tar jxf jemalloc-5.2.1.tar.bz2
cd jemalloc-5.2.1/
./configure --prefix=/home/tudou/app/percona-server-5.7.36-39
make -j 20
make install
```

## 将jemalloc 配置到 mysqld_safe 中
```shell
vim /home/tudou/app/percona-server-5.7.36-39/bin/mysqld_safe
# 在文件头部添加 ，这个目录只能是四个目录中的一个 "${MY_BASEDIR_VERSION}/lib/mysql" "/usr/lib64" "/usr/lib/x86_64-linux-gnu" "/usr/lib"
jemalloc_lib="/home/tudou/app/percona-server-5.7.36-39/lib/libjemalloc.so"

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
