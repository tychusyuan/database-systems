```shell
ps aux | grep mysqld
```
```
work      4440  1.6  5.5 9650132 902928 pts/0  Sl   16:28   0:02 /home/work/app/mysql/bin/mysqld --defaults-file=/home/work/etc/mysql/my.cnf --basedir=/home/work/app/mysql --datadir=/home/work/data/mysql/data3306 --plugin-dir=/home/work/app/mysql/lib/mysql/plugin --log-error=/home/work/log/mysql/log3306/log_error.err --open-files-limit=65535 --pid-file=/dev/shm/mysql3306.pid --socket=/dev/shm/mysql3306.sock --port=3306
```
```shell
pstack 4440
```
```
Thread 23 (Thread 0x7f84c07ff700 (LWP 4441)):
#0  0x00007f84ccd5bde2 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000000d70dcd in native_cond_timedwait (abstime=0x7f84c07fede0, mutex=0x2122f20 <pool_timer>, cond=0x2122f50 <pool_timer+48>) at /home/work/src/percona-server-5.7.38-41/include/thr_cond.h:136
#2  my_cond_timedwait (abstime=0x7f84c07fede0, mp=0x2122f20 <pool_timer>, cond=0x2122f50 <pool_timer+48>) at /home/work/src/percona-server-5.7.38-41/include/thr_cond.h:189
#3  inline_mysql_cond_timedwait (src_file=0x15e65b8 "/home/work/src/percona-server-5.7.38-41/sql/threadpool_unix.cc", src_line=572, abstime=0x7f84c07fede0, mutex=0x2122f20 <pool_timer>, that=<optimized out>) at /home/work/src/percona-server-5.7.38-41/include/mysql/psi/mysql_thread.h:1236
#4  timer_thread (param=param@entry=0x2122f20 <pool_timer>) at /home/work/src/percona-server-5.7.38-41/sql/threadpool_unix.cc:572
#5  0x000000000116caf4 in pfs_spawn_thread (arg=0x7f84cac67220) at /home/work/src/percona-server-5.7.38-41/storage/perfschema/pfs.cc:2198
#6  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#7  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 22 (Thread 0x7f84bfffe700 (LWP 4442)):
#0  0x00007f84cb95458a in sigwaitinfo () from /lib64/libc.so.6
#1  0x0000000000f5c01b in timer_notify_thread_func (arg=arg@entry=0x7ffe115d9b10) at /home/work/src/percona-server-5.7.38-41/mysys/posix_timers.c:89
#2  0x000000000116caf4 in pfs_spawn_thread (arg=0x7f84cac67320) at /home/work/src/percona-server-5.7.38-41/storage/perfschema/pfs.cc:2198
#3  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#4  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 21 (Thread 0x7f828e3ff700 (LWP 4444)):
#0  0x00007f84cc94a644 in __io_getevents_0_4 () from /lib64/libaio.so.1
#1  0x000000000128bb41 in LinuxAIOHandler::collect (this=this@entry=0x7f828e3feba0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:2820
#2  0x000000000128c575 in LinuxAIOHandler::poll (this=this@entry=0x7f828e3feba0, m1=m1@entry=0x7f828e3fec40, m2=m2@entry=0x7f828e3fec50, request=request@entry=0x7f828e3fec60) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:2980
#3  0x000000000129095b in os_aio_linux_handler (request=0x7f828e3fec60, m2=0x7f828e3fec50, m1=0x7f828e3fec40, global_segment=0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:3036
#4  os_aio_handler (segment=segment@entry=0, m1=m1@entry=0x7f828e3fec40, m2=m2@entry=0x7f828e3fec50, request=request@entry=0x7f828e3fec60) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:6878
#5  0x0000000001466de6 in fil_aio_wait (segment=segment@entry=0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/fil/fil0fil.cc:6446
#6  0x000000000134b1a0 in io_handler_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/srv/srv0start.cc:345
#7  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#8  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 20 (Thread 0x7f828dbfe700 (LWP 4445)):
#0  0x00007f84cc94a644 in __io_getevents_0_4 () from /lib64/libaio.so.1
#1  0x000000000128bb41 in LinuxAIOHandler::collect (this=this@entry=0x7f828dbfdba0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:2820
#2  0x000000000128c575 in LinuxAIOHandler::poll (this=this@entry=0x7f828dbfdba0, m1=m1@entry=0x7f828dbfdc40, m2=m2@entry=0x7f828dbfdc50, request=request@entry=0x7f828dbfdc60) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:2980
#3  0x000000000129095b in os_aio_linux_handler (request=0x7f828dbfdc60, m2=0x7f828dbfdc50, m1=0x7f828dbfdc40, global_segment=1) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:3036
#4  os_aio_handler (segment=segment@entry=1, m1=m1@entry=0x7f828dbfdc40, m2=m2@entry=0x7f828dbfdc50, request=request@entry=0x7f828dbfdc60) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:6878
#5  0x0000000001466de6 in fil_aio_wait (segment=segment@entry=1) at /home/work/src/percona-server-5.7.38-41/storage/innobase/fil/fil0fil.cc:6446
#6  0x000000000134b1a0 in io_handler_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/srv/srv0start.cc:345
#7  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#8  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 19 (Thread 0x7f828d3fd700 (LWP 4446)):
#0  0x00007f84cc94a644 in __io_getevents_0_4 () from /lib64/libaio.so.1
#1  0x000000000128bb41 in LinuxAIOHandler::collect (this=this@entry=0x7f828d3fcba0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:2820
#2  0x000000000128c575 in LinuxAIOHandler::poll (this=this@entry=0x7f828d3fcba0, m1=m1@entry=0x7f828d3fcc40, m2=m2@entry=0x7f828d3fcc50, request=request@entry=0x7f828d3fcc60) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:2980
#3  0x000000000129095b in os_aio_linux_handler (request=0x7f828d3fcc60, m2=0x7f828d3fcc50, m1=0x7f828d3fcc40, global_segment=2) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:3036
#4  os_aio_handler (segment=segment@entry=2, m1=m1@entry=0x7f828d3fcc40, m2=m2@entry=0x7f828d3fcc50, request=request@entry=0x7f828d3fcc60) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:6878
#5  0x0000000001466de6 in fil_aio_wait (segment=segment@entry=2) at /home/work/src/percona-server-5.7.38-41/storage/innobase/fil/fil0fil.cc:6446
#6  0x000000000134b1a0 in io_handler_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/srv/srv0start.cc:345
#7  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#8  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 18 (Thread 0x7f828cbfc700 (LWP 4447)):
#0  0x00007f84cc94a644 in __io_getevents_0_4 () from /lib64/libaio.so.1
#1  0x000000000128bb41 in LinuxAIOHandler::collect (this=this@entry=0x7f828cbfbba0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:2820
#2  0x000000000128c575 in LinuxAIOHandler::poll (this=this@entry=0x7f828cbfbba0, m1=m1@entry=0x7f828cbfbc40, m2=m2@entry=0x7f828cbfbc50, request=request@entry=0x7f828cbfbc60) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:2980
#3  0x000000000129095b in os_aio_linux_handler (request=0x7f828cbfbc60, m2=0x7f828cbfbc50, m1=0x7f828cbfbc40, global_segment=3) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:3036
#4  os_aio_handler (segment=segment@entry=3, m1=m1@entry=0x7f828cbfbc40, m2=m2@entry=0x7f828cbfbc50, request=request@entry=0x7f828cbfbc60) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:6878
#5  0x0000000001466de6 in fil_aio_wait (segment=segment@entry=3) at /home/work/src/percona-server-5.7.38-41/storage/innobase/fil/fil0fil.cc:6446
#6  0x000000000134b1a0 in io_handler_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/srv/srv0start.cc:345
#7  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#8  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 17 (Thread 0x7f828c3fb700 (LWP 4448)):
#0  0x00007f84cc94a644 in __io_getevents_0_4 () from /lib64/libaio.so.1
#1  0x000000000128bb41 in LinuxAIOHandler::collect (this=this@entry=0x7f828c3faba0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:2820
#2  0x000000000128c575 in LinuxAIOHandler::poll (this=this@entry=0x7f828c3faba0, m1=m1@entry=0x7f828c3fac40, m2=m2@entry=0x7f828c3fac50, request=request@entry=0x7f828c3fac60) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:2980
#3  0x000000000129095b in os_aio_linux_handler (request=0x7f828c3fac60, m2=0x7f828c3fac50, m1=0x7f828c3fac40, global_segment=4) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:3036
#4  os_aio_handler (segment=segment@entry=4, m1=m1@entry=0x7f828c3fac40, m2=m2@entry=0x7f828c3fac50, request=request@entry=0x7f828c3fac60) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:6878
#5  0x0000000001466de6 in fil_aio_wait (segment=segment@entry=4) at /home/work/src/percona-server-5.7.38-41/storage/innobase/fil/fil0fil.cc:6446
#6  0x000000000134b1a0 in io_handler_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/srv/srv0start.cc:345
#7  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#8  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 16 (Thread 0x7f828bbfa700 (LWP 4449)):
#0  0x00007f84cc94a644 in __io_getevents_0_4 () from /lib64/libaio.so.1
#1  0x000000000128bb41 in LinuxAIOHandler::collect (this=this@entry=0x7f828bbf9ba0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:2820
#2  0x000000000128c575 in LinuxAIOHandler::poll (this=this@entry=0x7f828bbf9ba0, m1=m1@entry=0x7f828bbf9c40, m2=m2@entry=0x7f828bbf9c50, request=request@entry=0x7f828bbf9c60) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:2980
#3  0x000000000129095b in os_aio_linux_handler (request=0x7f828bbf9c60, m2=0x7f828bbf9c50, m1=0x7f828bbf9c40, global_segment=5) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:3036
#4  os_aio_handler (segment=segment@entry=5, m1=m1@entry=0x7f828bbf9c40, m2=m2@entry=0x7f828bbf9c50, request=request@entry=0x7f828bbf9c60) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0file.cc:6878
#5  0x0000000001466de6 in fil_aio_wait (segment=segment@entry=5) at /home/work/src/percona-server-5.7.38-41/storage/innobase/fil/fil0fil.cc:6446
#6  0x000000000134b1a0 in io_handler_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/srv/srv0start.cc:345
#7  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#8  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 15 (Thread 0x7f828b3f9700 (LWP 4450)):
#0  0x00007f84ccd5bde2 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000001291887 in os_event::timed_wait (this=this@entry=0x7f84cac6f518, abstime=abstime@entry=0x7f828b3f8b80) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:92
#2  0x0000000001292210 in os_event::wait_time_low (this=0x7f84cac6f518, time_in_usec=<optimized out>, reset_sig_count=<optimized out>, reset_sig_count@entry=2) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:264
#3  0x00000000012923ca in os_event_wait_time_low (event=<optimized out>, time_in_usec=<optimized out>, reset_sig_count=reset_sig_count@entry=2) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:368
#4  0x000000000140cf7e in pc_sleep_if_needed (sig_count=2, next_loop_time=7628430) at /home/work/src/percona-server-5.7.38-41/storage/innobase/buf/buf0flu.cc:2801
#5  buf_flush_page_cleaner_coordinator (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/buf/buf0flu.cc:3264
#6  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#7  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 14 (Thread 0x7f828abf8700 (LWP 4451)):
#0  0x00007f84ccd5ee9d in nanosleep () from /lib64/libpthread.so.0
#1  0x0000000001292b60 in os_thread_sleep (tm=tm@entry=1000000) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0thread.cc:311
#2  0x000000000140bc09 in buf_lru_manager_sleep_if_needed (next_loop_time=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/buf/buf0flu.cc:3606
#3  buf_lru_manager (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/buf/buf0flu.cc:3698
#4  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#5  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 13 (Thread 0x7f82897ff700 (LWP 4452)):
#0  0x00007f84ccd5bde2 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000001291887 in os_event::timed_wait (this=this@entry=0x7f84cac6f418, abstime=abstime@entry=0x7f82897fedb0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:92
#2  0x0000000001292210 in os_event::wait_time_low (this=0x7f84cac6f418, time_in_usec=time_in_usec@entry=5000000, reset_sig_count=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:264
#3  0x00000000012923ca in os_event_wait_time_low (event=<optimized out>, time_in_usec=time_in_usec@entry=5000000, reset_sig_count=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:368
#4  0x0000000001342ba1 in srv_monitor_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/srv/srv0srv.cc:1952
#5  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#6  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 12 (Thread 0x7f8285fff700 (LWP 4454)):
#0  0x00007f84ccd5bde2 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000001291887 in os_event::timed_wait (this=this@entry=0x7f84cac70298, abstime=abstime@entry=0x7f8285ffecd0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:92
#2  0x0000000001292210 in os_event::wait_time_low (this=this@entry=0x7f84cac70298, time_in_usec=time_in_usec@entry=1000000, reset_sig_count=<optimized out>, reset_sig_count@entry=1) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:264
#3  0x00000000012923ca in os_event_wait_time_low (event=event@entry=0x7f84cac70298, time_in_usec=time_in_usec@entry=1000000, reset_sig_count=reset_sig_count@entry=1) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:368
#4  0x00000000012534d7 in lock_wait_timeout_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/lock/lock0wait.cc:570
#5  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#6  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 11 (Thread 0x7f82857fe700 (LWP 4455)):
#0  0x00007f84ccd5bde2 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000001291887 in os_event::timed_wait (this=this@entry=0x7f84cac6f398, abstime=abstime@entry=0x7f82857fdc50) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:92
#2  0x0000000001292210 in os_event::wait_time_low (this=0x7f84cac6f398, time_in_usec=time_in_usec@entry=1000000, reset_sig_count=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:264
#3  0x00000000012923ca in os_event_wait_time_low (event=<optimized out>, time_in_usec=time_in_usec@entry=1000000, reset_sig_count=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:368
#4  0x0000000001343032 in srv_error_monitor_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/srv/srv0srv.cc:2112
#5  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#6  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 10 (Thread 0x7f8284ffd700 (LWP 4456)):
#0  0x00007f84ccd5ee9d in nanosleep () from /lib64/libpthread.so.0
#1  0x0000000001292b60 in os_thread_sleep (tm=tm@entry=1000000) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0thread.cc:311
#2  0x000000000134a80a in srv_master_sleep () at /home/work/src/percona-server-5.7.38-41/storage/innobase/srv/srv0srv.cc:2816
#3  srv_master_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/srv/srv0srv.cc:2869
#4  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#5  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 9 (Thread 0x7f82847fc700 (LWP 4457)):
#0  0x00007f84ccd5ba35 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000001291b5b in wait (this=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/include/os0event.h:167
#2  os_event::wait_low (this=0x7f84cac6f298, reset_sig_count=<optimized out>, reset_sig_count@entry=1) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:142
#3  0x00000000012923da in os_event_wait_low (event=<optimized out>, reset_sig_count=reset_sig_count@entry=1) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:385
#4  0x00000000013461ad in srv_purge_coordinator_suspend (rseg_history_len=<optimized out>, slot=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/srv/srv0srv.cc:3191
#5  srv_purge_coordinator_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/srv/srv0srv.cc:3310
#6  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#7  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 8 (Thread 0x7f8283ffb700 (LWP 4458)):
#0  0x00007f84ccd5ba35 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000001291b5b in wait (this=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/include/os0event.h:167
#2  os_event::wait_low (this=0x7f84cac6f318, reset_sig_count=<optimized out>, reset_sig_count@entry=0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:142
#3  0x00000000012923da in os_event_wait_low (event=<optimized out>, reset_sig_count=reset_sig_count@entry=0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:385
#4  0x0000000001344968 in srv_worker_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/srv/srv0srv.cc:3030
#5  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#6  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 7 (Thread 0x7f82837fa700 (LWP 4459)):
#0  0x00007f84ccd5ba35 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000001291b5b in wait (this=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/include/os0event.h:167
#2  os_event::wait_low (this=0x7f84cac6f498, reset_sig_count=<optimized out>, reset_sig_count@entry=0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:142
#3  0x00000000012923da in os_event_wait_low (event=<optimized out>, reset_sig_count=reset_sig_count@entry=0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:385
#4  0x0000000001402ccc in buf_dump_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/buf/buf0dump.cc:792
#5  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#6  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 6 (Thread 0x7f8282ff9700 (LWP 4460)):
#0  0x00007f84ccd5bde2 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000001291887 in os_event::timed_wait (this=this@entry=0x7f84cac70698, abstime=abstime@entry=0x7f8282ff8d00) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:92
#2  0x0000000001292210 in os_event::wait_time_low (this=0x7f84cac70698, time_in_usec=time_in_usec@entry=10000000, reset_sig_count=<optimized out>, reset_sig_count@entry=0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:264
#3  0x00000000012923ca in os_event_wait_time_low (event=<optimized out>, time_in_usec=time_in_usec@entry=10000000, reset_sig_count=reset_sig_count@entry=0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:368
#4  0x000000000145ff5d in dict_stats_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/dict/dict0stats_bg.cc:435
#5  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#6  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 5 (Thread 0x7f82827f8700 (LWP 4461)):
#0  0x00007f84ccd5bde2 in pthread_cond_timedwait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000001291887 in os_event::timed_wait (this=this@entry=0x7f84c47e2418, abstime=abstime@entry=0x7f82827f7bb0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:92
#2  0x0000000001292210 in os_event::wait_time_low (this=0x7f84c47e2418, time_in_usec=time_in_usec@entry=5000000, reset_sig_count=<optimized out>, reset_sig_count@entry=1) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:264
#3  0x00000000012923ca in os_event_wait_time_low (event=<optimized out>, time_in_usec=time_in_usec@entry=5000000, reset_sig_count=reset_sig_count@entry=1) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:368
#4  0x00000000013aa88f in ib_wqueue_timedwait (wq=wq@entry=0x7f84c3bf6d98, wait_in_usecs=wait_in_usecs@entry=5000000) at /home/work/src/percona-server-5.7.38-41/storage/innobase/ut/ut0wqueue.cc:185
#5  0x00000000014c75fc in fts_optimize_thread (arg=0x7f84c3bf6d98) at /home/work/src/percona-server-5.7.38-41/storage/innobase/fts/fts0opt.cc:2913
#6  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#7  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 4 (Thread 0x7f8281ff7700 (LWP 4462)):
#0  0x00007f84ccd5ba35 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000001291b5b in wait (this=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/include/os0event.h:167
#2  os_event::wait_low (this=0x7f84cac6f698, reset_sig_count=<optimized out>, reset_sig_count@entry=0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:142
#3  0x00000000012923da in os_event_wait_low (event=<optimized out>, reset_sig_count=reset_sig_count@entry=0) at /home/work/src/percona-server-5.7.38-41/storage/innobase/os/os0event.cc:385
#4  0x00000000013f4be0 in buf_resize_thread (arg=<optimized out>) at /home/work/src/percona-server-5.7.38-41/storage/innobase/buf/buf0buf.cc:3253
#5  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#6  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 3 (Thread 0x7f84cd3ae700 (LWP 4463)):
#0  0x00007f84ccd5f3c1 in sigwait () from /lib64/libpthread.so.0
#1  0x0000000000d85133 in signal_hand (arg=arg@entry=0x0) at /home/work/src/percona-server-5.7.38-41/sql/mysqld.cc:2380
#2  0x000000000116caf4 in pfs_spawn_thread (arg=0x7f8289b4d620) at /home/work/src/percona-server-5.7.38-41/storage/perfschema/pfs.cc:2198
#3  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#4  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 2 (Thread 0x7f82817f6700 (LWP 4464)):
#0  0x00007f84ccd5ba35 in pthread_cond_wait@@GLIBC_2.3.2 () from /lib64/libpthread.so.0
#1  0x0000000000eb7243 in native_cond_wait (mutex=<optimized out>, cond=<optimized out>) at /home/work/src/percona-server-5.7.38-41/include/thr_cond.h:147
#2  my_cond_wait (mp=<optimized out>, cond=<optimized out>) at /home/work/src/percona-server-5.7.38-41/include/thr_cond.h:202
#3  inline_mysql_cond_wait (that=<optimized out>, mutex=<optimized out>, src_file=0x17ba4d0 "/home/work/src/percona-server-5.7.38-41/sql/rpl_gtid_persist.cc", src_line=885) at /home/work/src/percona-server-5.7.38-41/include/mysql/psi/mysql_thread.h:1191
#4  compress_gtid_table (p_thd=p_thd@entry=0x7f82863e4000) at /home/work/src/percona-server-5.7.38-41/sql/rpl_gtid_persist.cc:885
#5  0x000000000116caf4 in pfs_spawn_thread (arg=0x7f8289b4d920) at /home/work/src/percona-server-5.7.38-41/storage/perfschema/pfs.cc:2198
#6  0x00007f84ccd57ea5 in start_thread () from /lib64/libpthread.so.0
#7  0x00007f84cba1bb0d in clone () from /lib64/libc.so.6
Thread 1 (Thread 0x7f84cd3b07c0 (LWP 4440)):
#0  0x00007f84cba10ddd in poll () from /lib64/libc.so.6
#1  0x0000000000d7c5c2 in poll (__timeout=-1, __nfds=<optimized out>, __fds=0x7f84c3bf7ce8) at /usr/include/bits/poll2.h:41
#2  Mysqld_socket_listener::listen_for_connection_event (this=0x7f84c3bf7c80) at /home/work/src/percona-server-5.7.38-41/sql/conn_handler/socket_connection.cc:883
#3  0x0000000000d8ffe1 in connection_event_loop (this=0x7f84cac6c298) at /home/work/src/percona-server-5.7.38-41/sql/conn_handler/connection_acceptor.h:73
#4  mysqld_main (argc=96, argv=0x7f84cac378d0) at /home/work/src/percona-server-5.7.38-41/sql/mysqld.cc:5570
#5  0x00007f84cb93f555 in __libc_start_main () from /lib64/libc.so.6
#6  0x00000000007edc24 in _start ()
```
