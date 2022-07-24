
```shell
gdb --batch --pid <msyql pid> --ex 'call malloc_trim(0)'
```

```shell
op - 18:51:35 up 1410 days, 20:54,  1 user,  load average: 0.05, 0.05, 0.09
Tasks: 243 total,   1 running, 242 sleeping,   0 stopped,   0 zombie
%Cpu0  :  1.3 us,  0.7 sy,  0.0 ni, 98.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu1  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu2  :  0.3 us,  0.3 sy,  0.0 ni, 99.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu3  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu4  :  2.3 us,  0.3 sy,  0.0 ni, 97.4 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu5  :  0.3 us,  0.3 sy,  0.0 ni, 99.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu6  :  1.3 us,  0.3 sy,  0.0 ni, 98.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu7  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu8  :  0.3 us,  0.3 sy,  0.0 ni, 99.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu9  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu10 :  0.3 us,  0.0 sy,  0.0 ni, 99.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu11 :  0.0 us,  0.3 sy,  0.0 ni, 99.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu12 :  0.7 us,  0.3 sy,  0.0 ni, 99.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu13 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu14 :  0.3 us,  0.3 sy,  0.0 ni, 99.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu15 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 65976480 total,  1737236 free, 55830632 used,  8408612 buff/cache
KiB Swap: 12582908 total, 12582908 free,        0 used.  6481532 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                                                                                                                                                                                     
 1274 work      20   0 68.044g 0.050t   3660 S 521.9 81.5 104576:16 /home/work/mysql/bin/mysqld --defaults-file=/home/work/mysql/etc/my.cnf --basedir=/home/work/mysql --datadir=/home/work/mysql/data --plugin-dir=/home/work/mysql/lib/mysql/plugin --log-error=/home/work/m+ 
23150 work      20   0 1435080 1.153g  12240 S   0.0  1.8  41289:32 /home/work/opbin/containerpilot/bin/consul agent -config-dir /home/work/opbin/containerpilot/conf/consul.d/client/config.json -advertise 10.58.7.154 -disable-host-node-id                                  
 4723 root      20   0 1826512  64052   5156 S   0.3  0.1   3009:26 ./falcon-agent -c ./cfg.json                                                                                                                                                                                
31884 root      20   0 1799220  56856   5320 S   0.0  0.1 446:16.41 ruby /home/xbox/aesir/frigga/bin/frigga.rb                                                                                                                                                                  
 6789 root      20   0 2401716  56560   8880 S   0.0  0.1   1274:33 /opt/hades/.sagent.packages/ad4e76b00e2e4d9b/sagent worker --fg --no-restart --svc-mgnt dpa                                                                                                                 
 1106 root      20   0  690924  35396  34572 S   0.0  0.1  43:35.84 /usr/sbin/rsyslogd -n                                                                                                                                                                                       
31746 root      20   0  894704  21724   4244 S   0.0  0.0 230:28.56 ruby /home/xbox/aesir/ruby/bin/god --no-events --log-level info -c /home/xbox/aesir/frigga/conf/base.god                                                                                                    
 1108 root      20   0  553164  15756   3076 S   0.0  0.0 164:59.70 /usr/bin/python -Es /usr/sbin/tuned -l -P                                                                                                                                                                   
21138 root      20   0 1649696  15472   5140 S   0.0  0.0  41:51.56 /opt/matrix/mtx/mtx daemon -config /opt/matrix/mtx/config.yaml                                                                                                                                              
 1038 root      20   0  112888  12472      0 S   0.0  0.0   0:00.00 /sbin/dhclient -H sgp1-dba-miot-ali-va3-5390-u29of10g1 -1 -q -lf /var/lib/dhclient/dhclient--eth0.lease -pf /var/run/dhclient-eth0.pid eth0                                                                 
 6528 root      20   0 1710700  12380   6572 S   0.0  0.0  32:36.49 /opt/hades/sagent/sagent monitor --fg --no-restart --svc-mgnt dpa                                                                                                                                           
 2959 root      20   0  731024  11348   6588 S   0.0  0.0 291:51.13 /usr/deploy-agent/current/deploy-agent daemon                                                                                                                                                               
  607 root      20   0   46156  10684  10308 S   0.0  0.0  64:59.18 /usr/lib/systemd/systemd-journald                                                                                                                                                                           
 4462 work      20   0  115044  10148   4604 S   0.0  0.0 267:56.54 /home/work/opbin/containerpilot/bin/containerpilot -config-dir=/home/work/opbin/containerpilot/conf -log-file=/home/work/opbin/containerpilot/log/containerpilot.log                                        
  806 polkitd   20   0  529608   9388    988 S   0.0  0.0  73:41.56 /usr/lib/polkit-1/polkitd --no-debug                                                                                                                                                                        
 6774 root      20   0  715976   7000   2616 S   0.0  0.0  39:53.77 /opt/hades/sagent/advs-agent                                                                                                                                                                                
10504 postfix   20   0   93792   6696   5680 S   0.0  0.0   0:00.00 pickup -l -t unix -u                                                                                                                                                                                        
20722 root      20   0  105976   6588   4928 S   0.0  0.0   0:00.06 miauthd: root@pts/0                                                                                                                                                                                         
23124 work      20   0  117412   6432   3452 S   0.0  0.0 104:48.44 /home/work/opbin/containerpilot/bin/containerpilot --daemon                                                                                                                                                 
 2047 work      20   0 1900708   6116   3308 S   0.0  0.0 504:11.19 ./bin/cronnode -conf conf/base.json                                                                                                                                                                         
20724 root      20   0  115348   5588   3204 S   0.0  0.0   0:00.05 -bash                                                                                                                                                                                                       
    1 root      20   0  191752   4856   2536 S   0.0  0.0 116:32.58 /usr/lib/systemd/systemd --switched-root --system --deserialize 21                                                                                                                                          
21877 root      20   0  157892   4680   3776 R   0.3  0.0   0:00.29 top -c                                                                                                                                                                                                      
  816 root      20   0  212780   4200   2408 S   0.0  0.0   3:58.32 /usr/sbin/abrtd -d -s                                                                                                                                                                                       
  819 root      20   0  210292   3736   2376 S   0.0  0.0   6:56.77 /usr/bin/abrt-watch-log -F BUG: WARNING: at WARNING: CPU: INFO: possible recursive locking detected ernel BUG at list_del corruption list_add corruption do_IRQ: stack overflow: ear stack overflow (cur: + 
  622 root      20   0  274560   3608   1096 S   0.0  0.0   0:00.01 /usr/sbin/lvmetad -f                                                                                                                                                                                        
 1109 root      20   0  105488   3596   2616 S   0.0  0.0   0:26.30 /usr/sbin/sshd -D                                                                                                                                                                                           
 1808 root      20   0   91128   3304   2264 S   0.0  0.0   7:26.19 /usr/libexec/postfix/master -w                                                                                                                                                                              
10965 root      20   0  113204   3064   2820 S   0.0  0.0   4:34.75 sh /user/deploy-agent-assistant/deploy-agent-assistant/start.sh                                                                                                                                             
20779 rpc       20   0   65020   3004   2344 S   0.0  0.0   1:19.38 /sbin/rpcbind -w                                                                                                                                                                                            
  827 root      20   0   24572   2796   2100 S   0.0  0.0  76:20.48 /usr/lib/systemd/systemd-logind                                                                                                                                                                             
  837 chrony    20   0  113300   2732   2376 S   0.0  0.0   1:30.48 /usr/sbin/chronyd                                                                                                                                                                                           
  808 dbus      20   0   26808   2720   2092 S   0.0  0.0 142:36.11 /bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation                                                                                                                      
  633 root      20   0   44032   2684   1788 S   0.0  0.0   0:00.06 /usr/lib/systemd/systemd-udevd                                                                                                                                                                              
  831 root      20   0  126264   2668   2008 S   0.0  0.0  15:53.67 /usr/sbin/crond -n                                                                                                                                                                                          
27362 root      20   0   24852   2556   2072 S   0.0  0.0   0:00.68 /opt/miauth/miauthd/miauthd -D -f /opt/miauth/miauthd/sshd_config -h /opt/miauth/ssh_host_rsa_key                                                                                                           
 1831 postfix   20   0   91408   2384   1304 S   0.0  0.0   1:32.24 qmgr -l -t unix -u                                                                                                                                                                                          
32054 work      20   0  113220   2368   1980 S   0.0  0.0   0:00.08 /bin/sh /home/work/mysql/bin/mysqld_safe --defaults-file=/home/work/mysql/etc/my.cnf --user=work                                                                                                            
 6366 root      20   0   76520   2244   1496 S   0.0  0.0   0:17.03 /home/xbox/heimdallrd/bin/heimdallrd -r /home/xbox/heimdallrd/keys/rsa_key                                                                                                                                  
  807 root      20   0   24292   1944   1436 S   0.0  0.0   0:01.33 /usr/sbin/smartd -n -q never                                                                                                                                                                                
  835 root      20   0   25852   1572   1376 S   0.0  0.0   0:00.96 /usr/sbin/atd -f                                                                                                                                                                                            
  812 libstor+  20   0    8532   1484   1340 S   0.0  0.0   3:22.88 /usr/bin/lsmd -d                                                                                                                                                                                            
 1209 root      20   0  110044   1468   1340 S   0.0  0.0   0:00.01 /sbin/agetty --noclear tty1 linux                                                                                                                                                                           
 2040 work      20   0  115260   1292   1028 S   0.0  0.0   0:00.00 -bash -c cd /home/work/opbin/cronsun-v0.3.2/ && nohup ./bin/runit -alive -cmd "./bin/cronnode -conf conf/base.json" >>./log/cronnode.log 2>&1 &                                                             
  822 root      20   0    4376   1180   1084 S   0.0  0.0 937:02.54 /sbin/rngd -f                                                                                                                                                                                               
  853 root      20   0    6564    952    816 S   0.0  0.0   0:00.00 /usr/sbin/mcelog --ignorenodev --daemon --syslog                                                                                                                                                            
22137 root      20   0   76520    748      0 S   0.0  0.0   0:24.54 /home/xbox/heimdallrd/bin/heimdallrd -r /home/xbox/heimdallrd/keys/rsa_key                                                                                                                                  
21713 root      20   0  107904    708    636 S   0.0  0.0   0:00.00 sleep 60                                                                                                                                                                                                    
 2041 work      20   0    4580    404      0 S   0.0  0.0   0:52.26 ./bin/runit -alive -cmd ./bin/cronnode -conf conf/base.json                                                                                                                                                 
    2 root      20   0       0      0      0 S   0.0  0.0  60:59.61 [kthreadd]                                                                                                                                                                                                  
    3 root      20   0       0      0      0 S   0.0  0.0  25:50.47 [ksoftirqd/0]                                                                                                                                                                                               
[root@sgp1-miot-miio-video-db01 ~]# gdb --batch --pid 1274 --ex 'call malloc_trim(0)'
[New LWP 11604]
[New LWP 11598]
[New LWP 11579]
[New LWP 11363]
[New LWP 11342]
[New LWP 11336]
[New LWP 11330]
[New LWP 11315]
[New LWP 11297]
[New LWP 11288]
[New LWP 11227]
[New LWP 11208]
[New LWP 11192]
[New LWP 11179]
[New LWP 11173]
[New LWP 11166]
[New LWP 21149]
[New LWP 7309]
[New LWP 12605]
[New LWP 28921]
[New LWP 4211]
[New LWP 27381]
[New LWP 7141]
[New LWP 26058]
[New LWP 21707]
[New LWP 15103]
[New LWP 4014]
[New LWP 7561]
[New LWP 1852]
[New LWP 14684]
[New LWP 26697]
[New LWP 31799]
[New LWP 1410]
[New LWP 29981]
[New LWP 15520]
[New LWP 13294]
[New LWP 32699]
[New LWP 32698]
[New LWP 1946]
[New LWP 1945]
[New LWP 1942]
[New LWP 1941]
[New LWP 1940]
[New LWP 1939]
[New LWP 1938]
[New LWP 1937]
[New LWP 1936]
[New LWP 1935]
[New LWP 1933]
[New LWP 1932]
[New LWP 1931]
[New LWP 1322]
[New LWP 1321]
[New LWP 1320]
[New LWP 1319]
[New LWP 1318]
[New LWP 1317]
[New LWP 1316]
[New LWP 1315]
[New LWP 1314]
[New LWP 1313]
[New LWP 1312]
[New LWP 1311]
[New LWP 1310]
[New LWP 1309]
[New LWP 1308]
[New LWP 1307]
[New LWP 1306]
[New LWP 1305]
[New LWP 1304]
[New LWP 1303]
[New LWP 1302]
[New LWP 1301]
[New LWP 1300]
[New LWP 1299]
[New LWP 1298]
[New LWP 1297]
[New LWP 1296]
[New LWP 1295]
[New LWP 1294]
[New LWP 1293]
[New LWP 1292]
[New LWP 1291]
[New LWP 1290]
[New LWP 1289]
[New LWP 1288]
[New LWP 1287]
[New LWP 1286]
[New LWP 1285]
[New LWP 1284]
[New LWP 1276]
[New LWP 1275]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".
0x00007f2e8623bdfd in poll () from /lib64/libc.so.6
$1 = 1
[root@sgp1-miot-miio-video-db01 ~]# top -c

top - 18:52:06 up 1410 days, 20:55,  1 user,  load average: 0.17, 0.07, 0.09
Tasks: 247 total,   2 running, 245 sleeping,   0 stopped,   0 zombie
%Cpu0  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu1  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu2  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu3  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu4  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu5  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu6  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu7  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu8  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu9  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu10 :  4.2 us,  0.0 sy,  0.0 ni, 95.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu11 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu12 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu13 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu14 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu15 :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 65976480 total, 19767540 free, 37598064 used,  8610876 buff/cache
KiB Swap: 12582908 total, 12582908 free,        0 used. 24713976 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                                                                                                                                                                                     
 1274 work      20   0 68.028g 0.033t   3684 S   0.0 53.8 104576:16 /home/work/mysql/bin/mysqld --defaults-file=/home/work/mysql/etc/my.cnf --basedir=/home/work/mysql --datadir=/home/work/mysql/data --plugin-dir=/home/work/mysql/lib/mysql/plugin --log-error=/home/work/m+ 
23150 work      20   0 1435080 1.151g  12304 S   0.0  1.8  41289:32 /home/work/opbin/containerpilot/bin/consul agent -config-dir /home/work/opbin/containerpilot/conf/consul.d/client/config.json -advertise 10.58.7.154 -disable-host-node-id                                  
 4723 root      20   0 1826512  64052   5156 S   0.0  0.1   3009:26 ./falcon-agent -c ./cfg.json                                                                                                                                                                                
31884 root      20   0 1799220  56856   5320 S   0.0  0.1 446:16.43 ruby /home/xbox/aesir/frigga/bin/frigga.rb                                                                                                                                                                  
 6789 root      20   0 2401716  56576   8880 S   0.0  0.1   1274:33 /opt/hades/.sagent.packages/ad4e76b00e2e4d9b/sagent worker --fg --no-restart --svc-mgnt dpa                                                                                                                 
 1106 root      20   0  690924  35408  34584 S   0.0  0.1  43:35.84 /usr/sbin/rsyslogd -n                                                                                                                                                                                       
31746 root      20   0  894704  21724   4244 S   0.0  0.0 230:28.56 ruby /home/xbox/aesir/ruby/bin/god --no-events --log-level info -c /home/xbox/aesir/frigga/conf/base.god                                                                                                    
 1108 root      20   0  553164  15756   3076 S   0.0  0.0 164:59.70 /usr/bin/python -Es /usr/sbin/tuned -l -P                                                                                                                                                                   
21138 root      20   0 1649696  15472   5140 S   0.0  0.0  41:51.57 /opt/matrix/mtx/mtx daemon -config /opt/matrix/mtx/config.yaml                                                                                                                                              
 1038 root      20   0  112888  12472      0 S   0.0  0.0   0:00.00 /sbin/dhclient -H sgp1-dba-miot-ali-va3-5390-u29of10g1 -1 -q -lf /var/lib/dhclient/dhclient--eth0.lease -pf /var/run/dhclient-eth0.pid eth0                                                                 
 6528 root      20   0 1710700  12380   6572 S   0.0  0.0  32:36.51 /opt/hades/sagent/sagent monitor --fg --no-restart --svc-mgnt dpa                                                                                                                                           
 2959 root      20   0  731024  11348   6588 S   0.0  0.0 291:51.13 /usr/deploy-agent/current/deploy-agent daemon                                                                                                                                                               
  607 root      20   0   46156  11012  10636 S   0.0  0.0  64:59.18 /usr/lib/systemd/systemd-journald                                                                                                                                                                           
 4462 work      20   0  115044  10148   4604 S   0.0  0.0 267:56.56 /home/work/opbin/containerpilot/bin/containerpilot -config-dir=/home/work/opbin/containerpilot/conf -log-file=/home/work/opbin/containerpilot/log/containerpilot.log                                        
  806 polkitd   20   0  529608   9388    988 S   0.0  0.0  73:41.56 /usr/lib/polkit-1/polkitd --no-debug                                                                                                                                                                        
 6774 root      20   0  715976   7000   2616 S   0.0  0.0  39:53.77 /opt/hades/sagent/advs-agent                                                                                                                                                                                
10504 postfix   20   0   93792   6696   5680 S   0.0  0.0   0:00.00 pickup -l -t unix -u                                                                                                                                                                                        
20722 root      20   0  105976   6588   4928 S   0.0  0.0   0:00.09 miauthd: root@pts/0                                                                                                                                                                                         
23124 work      20   0  117412   6432   3452 S   0.0  0.0 104:48.44 /home/work/opbin/containerpilot/bin/containerpilot --daemon                                                                                                                                                 
 2047 work      20   0 1900708   6116   3308 S   0.0  0.0 504:11.21 ./bin/cronnode -conf conf/base.json                                                                                                                                                                         
20724 root      20   0  115348   5588   3204 S   0.0  0.0   0:00.06 -bash                                                                                                                                                                                                       
22289 root      20   0  112000   5216   4372 S   0.0  0.0   0:00.00 ./dbrtime                                                                                                                                                                                                   
    1 root      20   0  191752   4856   2536 S   0.0  0.0 116:32.58 /usr/lib/systemd/systemd --switched-root --system --deserialize 21                                                                                                                                          
22275 root      20   0  157892   4648   3752 R   4.2  0.0   0:00.50 top -c                                                                                                                                                                                                      
22285 root      20   0  180244   4432   3464 S   0.0  0.0   0:00.00 /usr/sbin/CROND -n                                                                                                                                                                                          
  816 root      20   0  212780   4200   2408 S   0.0  0.0   3:58.32 /usr/sbin/abrtd -d -s                                                                                                                                                                                       
  819 root      20   0  210292   3736   2376 S   0.0  0.0   6:56.77 /usr/bin/abrt-watch-log -F BUG: WARNING: at WARNING: CPU: INFO: possible recursive locking detected ernel BUG at list_del corruption list_add corruption do_IRQ: stack overflow: ear stack overflow (cur: + 
  622 root      20   0  274560   3608   1096 S   0.0  0.0   0:00.01 /usr/sbin/lvmetad -f                                                                                                                                                                                        
 1109 root      20   0  105488   3596   2616 S   0.0  0.0   0:26.30 /usr/sbin/sshd -D                                                                                                                                                                                           
 1808 root      20   0   91128   3304   2264 S   0.0  0.0   7:26.19 /usr/libexec/postfix/master -w                                                                                                                                                                              
22287 root      20   0  113200   3092   2864 S   0.0  0.0   0:00.00 /bin/sh -c cd /home/work/opbin/falcon_monitor/bin && ./dbrtime &>/dev/null                                                                                                                                  
10965 root      20   0  113204   3064   2820 S   0.0  0.0   4:34.75 sh /user/deploy-agent-assistant/deploy-agent-assistant/start.sh                                                                                                                                             
20779 rpc       20   0   65020   3004   2344 S   0.0  0.0   1:19.38 /sbin/rpcbind -w                                                                                                                                                                                            
  827 root      20   0   24572   2796   2100 S   0.0  0.0  76:20.49 /usr/lib/systemd/systemd-logind                                                                                                                                                                             
  837 chrony    20   0  113300   2732   2376 S   0.0  0.0   1:30.48 /usr/sbin/chronyd                                                                                                                                                                                           
  808 dbus      20   0   26808   2720   2092 S   0.0  0.0 142:36.12 /bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation                                                                                                                      
  633 root      20   0   44032   2684   1788 S   0.0  0.0   0:00.06 /usr/lib/systemd/systemd-udevd                                                                                                                                                                              
  831 root      20   0  126264   2668   2008 S   0.0  0.0  15:53.67 /usr/sbin/crond -n                                                                                                                                                                                          
27362 root      20   0   24852   2556   2072 S   0.0  0.0   0:00.68 /opt/miauth/miauthd/miauthd -D -f /opt/miauth/miauthd/sshd_config -h /opt/miauth/ssh_host_rsa_key                                                                                                           
 1831 postfix   20   0   91408   2384   1304 S   0.0  0.0   1:32.24 qmgr -l -t unix -u                                                                                                                                                                                          
32054 work      20   0  113220   2368   1980 S   0.0  0.0   0:00.08 /bin/sh /home/work/mysql/bin/mysqld_safe --defaults-file=/home/work/mysql/etc/my.cnf --user=work                                                                                                            
 6366 root      20   0   76520   2244   1496 S   0.0  0.0   0:17.03 /home/xbox/heimdallrd/bin/heimdallrd -r /home/xbox/heimdallrd/keys/rsa_key                                                                                                                                  
  807 root      20   0   24292   1944   1436 S   0.0  0.0   0:01.33 /usr/sbin/smartd -n -q never                                                                                                                                                                                
  835 root      20   0   25852   1572   1376 S   0.0  0.0   0:00.96 /usr/sbin/atd -f                                                                                                                                                                                            
  812 libstor+  20   0    8532   1484   1340 S   0.0  0.0   3:22.88 /usr/bin/lsmd -d                                                                                                                                                                                            
 1209 root      20   0  110044   1468   1340 S   0.0  0.0   0:00.01 /sbin/agetty --noclear tty1 linux                                                                                                                                                                           
 2040 work      20   0  115260   1292   1028 S   0.0  0.0   0:00.00 -bash -c cd /home/work/opbin/cronsun-v0.3.2/ && nohup ./bin/runit -alive -cmd "./bin/cronnode -conf conf/base.json" >>./log/cronnode.log 2>&1 &                                                             
  822 root      20   0    4376   1180   1084 S   0.0  0.0 937:02.54 /sbin/rngd -f                                                                                                                                                                                               
  853 root      20   0    6564    952    816 S   0.0  0.0   0:00.00 /usr/sbin/mcelog --ignorenodev --daemon --syslog                                                                                                                                                            
22300 root      20   0   95408    948    772 S   0.0  0.0   0:00.01 ./tcprstat -p 3306 -t 10 -n 1                                                                                                                                                                               
22137 root      20   0   76520    748      0 S   0.0  0.0   0:24.54 /home/xbox/heimdallrd/bin/heimdallrd -r /home/xbox/heimdallrd/keys/rsa_key   
```
