## port_cluster_failover.sh

```shell
# ps aux|grep redis-server|grep -v grep | awk -F':' '{print $3}' | awk '{print $1}'
# ps aux|grep redis-server|grep -v grep | awk -F':' '{print $4}' | awk '{print $1}'

for hp in `cat lsp`
do 
    h=$(echo $hp | awk -F':' '{print $1}')
    p=$(echo $hp | awk -F':' '{print $2}')
    lr -p $p > info_port
    lr_info=$(cat info_port | grep $h)
    host=$(echo $lr_info | awk '{print $4}' | awk -F':' '{print $1}')
    port=$(echo $lr_info | awk '{print $4}' | awk -F':' '{print $2}')
    passwd=$(echo $lr_info | awk '{print $5}')
    str_pwd=''
    if [ -z $passwd ];
    then
	str_pwd=''
    else
	str_pwd="-a ${passwd}"
    fi
    redis-cli -h $host -p $port ${str_pwd} info replication > replication_info
    #cat replication_info
    is_master=$(cat replication_info | grep 'role' | grep 'master')
    is_slave=$(cat replication_info | grep 'role' | grep 'slave')
    if [ -z $is_master ] 
    then
        echo $is_slave
    else
        cat replication_info | grep 'slave'
        slave_info=$(cat replication_info | grep 'slave' | grep 'online')
        slave_ip=$(echo $slave_info | awk -F'ip=' '{print $2}' | awk -F',port=' '{print $1}')
        slave_port=$(echo $slave_info | awk -F':ip=' '{print $2}' | awk -F',port=' '{print $2}' | awk -F',state=online' '{print $1}')
        redis-cli -h $slave_ip -p $slave_port ${str_pwd} cluster failover
        sleep 6
        redis-cli -h $slave_ip -p $slave_port ${str_pwd} info replication
    fi
done

```

## lsp
```sehll
192.168.1.72:42697
192.168.1.72:41843
192.168.1.72:19343
192.168.1.72:47262
192.168.1.72:42910
192.168.1.72:42914
192.168.1.72:46338
192.168.1.72:46343
192.168.1.72:47104
192.168.1.72:47110
192.168.1.72:47149
192.168.1.72:47155
192.168.1.72:42145
```
