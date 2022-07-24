```shell
ps aux|grep mysqld
```
```
work      4440  0.7  5.6 9654260 915724 pts/0  Sl   16:28   0:07 /home/work/app/mysql/bin/mysqld --defaults-file=/home/work/etc/mysql/my.cnf --basedir=/home/work/app/mysql --datadir=/home/work/data/mysql/data3306 --plugin-dir=/home/work/app/mysql/lib/mysql/plugin --log-error=/home/work/log/mysql/log3306/log_error.err --open-files-limit=65535 --pid-file=/dev/shm/mysql3306.pid --socket=/dev/shm/mysql3306.sock --port=3306

```

```shell
strace -p 4440
```
```
strace: Process 4440 attached
restart_syscall(<... resuming interrupted read ...>) = 1
accept(30, {sa_family=AF_UNIX}, [128->2]) = 45
setsockopt(45, SOL_TCP, TCP_NODELAY, [1], 4) = -1 EOPNOTSUPP (Operation not supported)
mmap(NULL, 1056768, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x7f84cb618000
mprotect(0x7f84cb618000, 4096, PROT_NONE) = 0
clone(child_stack=0x7f84cb718f30, flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, parent_tidptr=0x7f84cb7199d0, tls=0x7f84cb719700, child_tidptr=0x7f84cb7199d0) = 4732
poll([{fd=29, events=POLLIN}, {fd=30, events=POLLIN}], 2, -1) = 1 ([{fd=30, revents=POLLIN}])
accept(30, {sa_family=AF_UNIX}, [128->2]) = 45
setsockopt(45, SOL_TCP, TCP_NODELAY, [1], 4) = -1 EOPNOTSUPP (Operation not supported)
mmap(NULL, 1056768, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x7f84cb414000
mprotect(0x7f84cb414000, 4096, PROT_NONE) = 0
clone(child_stack=0x7f84cb514f30, flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, parent_tidptr=0x7f84cb5159d0, tls=0x7f84cb515700, child_tidptr=0x7f84cb5159d0) = 4757
futex(0x2123600, FUTEX_WAKE_PRIVATE, 1) = 1
poll([{fd=29, events=POLLIN}, {fd=30, events=POLLIN}], 2, -1) = 1 ([{fd=30, revents=POLLIN}])
accept(30, {sa_family=AF_UNIX}, [128->2]) = 45
setsockopt(45, SOL_TCP, TCP_NODELAY, [1], 4) = -1 EOPNOTSUPP (Operation not supported)
clone(child_stack=0x7f84cb514f30, flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, parent_tidptr=0x7f84cb5159d0, tls=0x7f84cb515700, child_tidptr=0x7f84cb5159d0) = 4768
poll([{fd=29, events=POLLIN}, {fd=30, events=POLLIN}], 2, -1
```
