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

## my.cnf
```shell
[client]
port                            	= 3306
socket                          	= /dev/shm/mysql3306.sock
default-character-set               	= utf8mb4

[mysqld]
lower_case_table_names          	= 1
character-set-server            	= utf8mb4
tmpdir                          	= /home/tudou/tmp
port                            	= 3306
socket                          	= /dev/shm/mysql3306.sock
pid_file                        	= /dev/shm/mysql3306.pid
read_only                       	= OFF
max_connect_errors              	= 99
max_connections                 	= 1024
max_user_connections            	= 1024
back_log                        	= 128
thread_cache_size               	= 10

skip-external-locking
skip-name-resolve
safe-user-create
interactive_timeout             	= 28800
wait_timeout                    	= 28800

open_files_limit                	= 65535
key_buffer_size                 	= 1M
max_allowed_packet              	= 1M
table_definition_cache          	= 65535
table_open_cache                	= 65535
max_length_for_sort_data        	= 8M
max_tmp_tables                  	= 1024
max_heap_table_size             	= 8M
tmp_table_size                  	= 8M

thread_handling                 	= pool-of-threads
thread_pool_size                	= 20
thread_pool_stall_limit         	= 10
thread_pool_idle_timeout        	= 60
thread_pool_max_threads         	= 8
thread_pool_oversubscribe       	= 16

query_cache_type                	= OFF
query_cache_size                	= 0
query_cache_limit               	= 0

#session
join_buffer_size                	= 8M
max_length_for_sort_data        	= 8M
sort_buffer_size                	= 8M
read_buffer_size                	= 8M
read_rnd_buffer_size            	= 8M
net_buffer_length               	= 1M
thread_stack                    	= 1M

datadir                         	= /home/tudou/data/mysql/data3306
memlock
default-storage-engine          	= innodb
innodb_doublewrite      		= 1

innodb_file_per_table       		= 1
innodb_buffer_pool_size         	= 30G
innodb_buffer_pool_instances    	= 1
#innodb_adaptive_hash_index_partitions  = 64
innodb_change_buffering         	= all
innodb_data_file_path           	= ibdata1:1G:autoextend
innodb_concurrency_tickets      	= 1024

innodb_log_group_home_dir       	= /home/tudou/log/mysql/log3306
innodb_max_dirty_pages_pct      	= 75
innodb_flush_method             	= O_DIRECT
innodb_log_file_size            	= 1G
innodb_log_files_in_group       	= 3
#innodb_log_block_size      	= 4096

innodb_page_size                	= 16K
innodb_file_format              	= Barracuda
innodb_file_format_check        	= 1
innodb_file_format_max          	= Barracuda
innodb_strict_mode              	= 1
innodb_checksum_algorithm   	= crc32

innodb_support_xa               	= 0
innodb_stats_on_metadata        	= 0
innodb_use_native_aio           	= 1
innodb_purge_threads            	= 2
innodb_adaptive_flushing        	= 1
innodb_io_capacity              	= 800
innodb_io_capacity_max      		= 1000
innodb_thread_concurrency       	= 0
innodb_read_io_threads          	= 2
innodb_write_io_threads         	= 2
#innodb_sched_priority_cleaner  	= 32

innodb_open_files               	= 65535
innodb_lock_wait_timeout        	= 60
sync_binlog                     	= 0
innodb_sync_spin_loops          	= 0
innodb_flush_log_at_trx_commit  	= 2

general-log                     	= 0
general_log_file                	= /home/tudou/log/mysql/log3306/general.log

slow-query-log                  	= 0
slow_query_log_file             	= /home/tudou/log/mysql/log3306/slow_query.log
long_query_time                 	= 0.001
log-queries-not-using-indexes   	= 1

log_warnings
log_error                       	= /home/tudou/log/mysql/log3306/log_error.err


[mysqldump]
quick
max_allowed_packet              	= 1M

[mysql]
default-character-set               	= utf8mb4
prompt                          	= "(\\u@\\h:\\d \\r:\\m:\\s>"
no-auto-rehash

[myisamchk]
key_buffer_size                 	= 8M
sort_buffer_size                	= 8M

[mysqlhotcopy]
interactive-timeout
```
## 初始化数据库文件
```shell
/home/tudou/app/mysql/bin/mysqld --defaults-file=/home/tudou/app/mysql/etc/my.cnf --initialize-insecure --user=tudou
```

## 启动
```shell
numactl --interleave=all /home/tudou/app/mysql/bin/mysqld_safe --defaults-file=/home/tudou/app/mysql/etc/my.cnf --user=tudou &
```
