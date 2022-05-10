# numactl 
## EXAMPLES
### bigdatabase arguments Run big database with its memory interleaved on all CPUs.
```shell
numactl --interleave=all /home/work/app/mysql/bin/mysqld_safe --defaults-file=/home/work/etc/my3306.cnf --basedir=/home/work/app/mysql --user=work &
```
### database run with its memory on local node 
```shell
numactl --cpunodebind=0 --localalloc /home/work/app/mysql/bin/mysqld_safe --defaults-file=/home/work/etc/my3306.cnf --basedir=/home/work/app/mysql --user=work &
```
```shell
numactl --cpunodebind=1 --localalloc /home/work/app/mysql/bin/mysqld_safe --defaults-file=/home/work/etc/my3307.cnf --basedir=/home/work/app/mysql --user=work &
```
### cross mode
```shell
numactl --physcpubind=0,1,2,3 --interleave=all /home/work/app/mysql/bin/mysqld_safe --defaults-file=/home/work/etc/my3306.cnf --basedir=/home/work/app/mysql --user=work &
```
```shell
numactl --physcpubind=2,3,4,5 --interleave=all /home/work/app/mysql/bin/mysqld_safe --defaults-file=/home/work/etc/my3307.cnf --basedir=/home/work/app/mysql --user=work &
```
### process Run process on node 0 with memory allocated on node 0 and 1.
```shell
numactl --cpunodebind=0 --membind=0,1 
```
### myapplic arguments Run myapplic on cpus 0-4 and 8-12 of the current cpuset.
```shell
numactl --physcpubind=+0-4,8-12 
```
```shell
       numactl --cpunodebind=0 --membind=0,1 -- process -l Run process
       as above, but with an option (-l) that would be confused with a
       numactl option.

       numactl --cpunodebind=0 --balancing --membind=0,1 process Run
       process on node 0 with memory allocated on node 0 and 1.
       Optimize the page placement with Linux kernel NUMA balancing
       mechanism if possible.

       numactl --cpunodebind=netdev:eth0 --membind=netdev:eth0 network-
       server Run network-server on the node of network device eth0 with
       its memory also in the same node.

       numactl --preferred=1 numactl --show Set preferred node 1 and
       show the resulting state.

       numactl --interleave=all --shm /tmp/shmkey Interleave all of the
       sysv shared memory region specified by /tmp/shmkey over all
       nodes.

       Place a tmpfs file on 2 nodes:
         numactl --membind=2 dd if=/dev/zero of=/dev/shm/A bs=1M
       count=1024
         numactl --membind=3 dd if=/dev/zero of=/dev/shm/A seek=1024
       bs=1M count=1024

       numactl --localalloc /dev/shm/file Reset the policy for the
       shared memory file file to the default localalloc policy.
```
