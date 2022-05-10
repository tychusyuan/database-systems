# numactl 
## SYNOPSIS 
```shell
numactl [ --all ] [ --balancing ] [ --interleave nodes ] [
       --preferred node ] [ --membind nodes ] [ --cpunodebind nodes ] [
       --physcpubind cpus ] [ --localalloc ] [--] command {arguments
       ...}
       numactl --show
       numactl --hardware
       numactl [ --huge ] [ --offset offset ] [ --shmmode shmmode ] [
       --length length ] [ --strict ]
       [ --shmid id ] --shm shmkeyfile | --file tmpfsfile
       [ --touch ] [ --dump ] [ --dump-nodes ] memory policy
```
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
### others
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
## DESCRIPTION
```shell
numactl runs processes with a specific NUMA scheduling or memory
       placement policy.  The policy is set for command and inherited by
       all of its children.  In addition it can set persistent policy
       for shared memory segments or files.

       Use -- before command if using command options that could be
       confused with numactl options.

       nodes may be specified as N,N,N or  N-N or N,N-N or  N-N,N-N and
       so forth.  Relative nodes may be specified as +N,N,N or  +N-N or
       +N,N-N and so forth. The + indicates that the node numbers are
       relative to the process' set of allowed nodes in its current
       cpuset.  A !N-N notation indicates the inverse of N-N, in other
       words all nodes except N-N.  If used with + notation, specify
       !+N-N. When same is specified the previous nodemask specified on
       the command line is used.  all means all nodes in the current
       cpuset.

       Instead of a number a node can also be:

       netdev:DEV                 The node connected to network device DEV.
       file:PATH                  The node the block device of PATH.
       ip:HOST                    The node of the network device of HOST
       block:PATH                 The node of block device PATH
       pci:[seg:]bus:dev[:func]   The node of a PCI device.

       Note that block resolves the kernel block device names only for
       udev names in /dev use file:

       Policy settings are:

       --all, -a
              Unset default cpuset awareness, so user can use all
              possible CPUs/nodes for following policy settings.

       --interleave=nodes, -i nodes
              Set a memory interleave policy. Memory will be allocated
              using round robin on nodes.  When memory cannot be
              allocated on the current interleave target fall back to
              other nodes.  Multiple nodes may be specified on
              --interleave, --membind and --cpunodebind.

       --membind=nodes, -m nodes
              Only allocate memory from nodes.  Allocation will fail
              when there is not enough memory available on these nodes.
              nodes may be specified as noted above.

       --cpunodebind=nodes, -N nodes
              Only execute command on the CPUs of nodes.  Note that
              nodes may consist of multiple CPUs.  nodes may be
              specified as noted above.

       --physcpubind=cpus, -C cpus
              Only execute process on cpus.  This accepts cpu numbers as
              shown in the processor fields of /proc/cpuinfo, or
              relative cpus as in relative to the current cpuset.  You
              may specify "all", which means all cpus in the current
              cpuset.  Physical cpus may be specified as N,N,N or  N-N
              or N,N-N or  N-N,N-N and so forth.  Relative cpus may be
              specified as +N,N,N or  +N-N or +N,N-N and so forth. The +
              indicates that the cpu numbers are relative to the
              process' set of allowed cpus in its current cpuset.  A !N-
              N notation indicates the inverse of N-N, in other words
              all cpus except N-N.  If used with + notation, specify
              !+N-N.

       --localalloc, -l
              Try to allocate on the current node of the process, but if
              memory cannot be allocated there fall back to other nodes.

       --preferred=node
              Preferably allocate memory on node, but if memory cannot
              be allocated there fall back to other nodes.  This option
              takes only a single node number.  Relative notation may be
              used.

       --balancing, -b
              Enable Linux kernel NUMA balancing for the process if it
              is supported by kernel.  This should only be used with
              --membind, -m only, otherwise ignored.

       --show, -s
              Show NUMA policy settings of the current process.

       --hardware, -H
              Show inventory of available nodes on the system.

       Numactl can set up policy for a SYSV shared memory segment or a
       file in shmfs/hugetlbfs.

       This policy is persistent and will be used by all mappings from
       that shared memory. The order of options matters here.  The
       specification must at least include either of --shm, --shmid,
       --file to specify the shared memory segment or file and a memory
       policy like described above ( --interleave, --localalloc,
       --preferred, --membind ).

       --huge
       When creating a SYSV shared memory segment use huge pages.  Only
       valid before --shmid or --shm

       --offset
       Specify offset into the shared memory segment. Default 0.  Valid
       units are m (for MB), g (for GB), k (for KB), otherwise it
       specifies bytes.

       --strict
       Give an error when a page in the policied area in the shared
       memory segment already was faulted in with a conflicting policy.
       Default is to silently ignore this.

       --shmmode shmmode
       Only valid before --shmid or --shm When creating a shared memory
       segment set it to numeric mode shmmode.

       --length length
       Apply policy to length range in the shared memory segment or make
       the segment length long Default is to use the remaining length
       Required when a shared memory segment is created and specifies
       the length of the new segment then. Valid units are m (for MB), g
       (for GB), k (for KB), otherwise it specifies bytes.

       --shmid id
       Create or use a shared memory segment with numeric ID id

       --shm shmkeyfile
       Create or use a shared memory segment, with the ID generated
       using ftok(3) from shmkeyfile

       --file tmpfsfile
       Set policy for a file in tmpfs or hugetlbfs

       --touch
       Touch pages to enforce policy early. Default is to not touch
       them, the policy is applied when an applications maps and
       accesses a page.

       --dump
       Dump policy in the specified range.

       --dump-nodes
       Dump all nodes of the specific range (very verbose!)

       Valid node specifiers

       all                 All nodes
       number              Node number
       number1{,number2}   Node number1 and Node number2
       number1-number2     Nodes from number1 to number2
       ! nodes             Invert selection of the following specification.
```
