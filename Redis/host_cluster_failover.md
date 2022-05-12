# Redis host_cluster_failover
## lst
```shell
   bigdata           46640            0.56            1.18            1.00            2.10          master             yes      xxddle-review-cache-ksmos
   xxcloud           47266            0.22            0.21            1.00            0.96          master             yes      xxcloud-elfcontext-store-mos
 internet3           46468            5.01            8.02           11.00            1.60          master             yes                xxpush-mos
 internet5           46440            0.25            0.90            7.00            3.57          master             yes      global-browser-mos-02
  software           49500            0.73            1.04            2.00            1.43          master             yes      passport-account-cache-mos
 internet5           50122            0.79            1.12            3.00            1.42          master             yes      monetization-realtimeFreature-cache-ksmos
  software           49495            0.22            0.30            2.00            1.35          master             yes      passport-accountoauth-cache-mos
 internet5           46445            0.25            0.46            7.00            1.84          master             yes      global-browser-mos-02
 internet2           47197            0.22            0.07            1.00            0.31          master             yes      intermigc-platformaccount-store-mos
 internet5           50128            0.73            1.14            3.00            1.56           slave             yes      monetization-realtimeFreature-cache-ksmos
   bigdata           46642            0.01            0.01            5.00            0.75           slave             yes      xxui-cloudcontrol-mos
 internet2           47156            0.22            0.07            1.00            0.34          master             yes      appstore-ngxshield-cache-mos
 internet2           46999            0.22            0.21            4.00            0.93          master             yes      appstore-synctask-cache-mos
  software           49528            0.40            0.37            1.00            0.92          master             yes      passport-passtokeninvalid-cache-mos
 internet2           47162            0.22            0.07            1.00            0.31          master             yes      appstore-ngxshield-cache-mos
 internet3           50367            5.09            5.19            6.05            1.02           slave             yes      xxpush-dispatcher-cache-ksrumos
   xxcloud           54780            0.23            0.22           10.00            0.95           slave             yes      xxcloud-sms-cache-mos
   xxcloud           55229            0.22            0.03            1.00            0.12          master             yes       xxfe-api-cache-ksru
 internet2           47006            0.22            0.21            4.00            0.93          master             yes      appstore-synctask-cache-mos
 internet1           47530            0.22            0.22            2.00            1.02           slave             yes         beehive-cache-mos

```
## host_cluster_failover.sh
```shell
list_port=$(cat lst | grep ' master '| awk '{print $2}')
for item in ${list_port};
do
    lr_info=$(lr -p ${item})
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
    cat replication_info
    slave_info=$(cat replication_info | grep 'slave' | grep 'online')
    slave_ip=$(echo $slave_info | awk -F'ip=' '{print $2}' | awk -F',port=' '{print $1}')
    slave_port=$(echo $slave_info | awk -F':ip=' '{print $2}' | awk -F',port=' '{print $2}' | awk -F',state=online' '{print $1}')
    redis-cli -h $slave_ip -p $slave_port ${str_pwd} cluster failover
    sleep 30
    redis-cli -h $slave_ip -p $slave_port ${str_pwd} info replication
done
```
