```sql
=====================================
2022-07-28 10:22:42 0x7fe4d0ace700 INNODB MONITOR OUTPUT
=====================================
Per second averages calculated from the last 21 seconds
```
Make sure data is sampled for at least 20-30 seconds. If averages are calculated for last 0 or 1 second they are pretty much unusable.


-----------------
BACKGROUND THREAD
-----------------
srv_master_thread loops: 34087406 srv_active, 0 srv_shutdown, 524364 srv_idle
srv_master_thread log flush and writes: 34611744
----------
SEMAPHORES
----------
OS WAIT ARRAY INFO: reservation count 101405775
OS WAIT ARRAY INFO: signal count 232187422
RW-shared spins 0, rounds 435162192, OS waits 71608446
RW-excl spins 0, rounds 561832245, OS waits 3542731
RW-sx spins 4287926, rounds 34008065, OS waits 181852
Spin rounds per wait: 435162192.00 RW-shared, 561832245.00 RW-excl, 7.93 RW-sx
------------------------
LATEST DETECTED DEADLOCK
------------------------
2022-07-20 06:25:03 0x7fe4c307e700
*** (1) TRANSACTION:
TRANSACTION 79624759936, ACTIVE 0 sec inserting
mysql tables in use 1, locked 1
LOCK WAIT 3 lock struct(s), heap size 1136, 2 row lock(s), undo log entries 1
MySQL thread id 8549214, OS thread handle 140620751025920, query id 39084605259 10.58.35.2 test_x update
insert into test_table (`uid`,`did`,`key`,`value`,`last_modify`) values (251081666,'blt.1.1a6j65qgt4g01','2022-05-26','{\"data\":{\"date\":\"2022-05-26\",\"data\":[{\"balance\":67,\"coverage\":33,\"duration\":64,\"over\":0,\"score\":50,\"date\":\"2022-05-26 21:49:29\",\"diagram1\":[true,true,false,false,true,false],\"diagram2\":[false,false,false,false,false,false],\"dateTimer\":1653572969000}],\"dateTimer\":1653494400000,\"score\":50,\"balance\":67,\"coverage\":33,\"duration\":64,\"over\":0},\"timestamp\":1658269502441}',1658269503) ON DUPLICATE KEY UPDATE `uid`=values(`uid`),`did`=values(`did`),`key`=values(`key`),`value`=values(`value`),`last_modify`=values(`last_modify`)
*** (1) WAITING FOR THIS LOCK TO BE GRANTED:
RECORD LOCKS space id 6918 page no 623 n bits 360 index uk_idx_uid_did_key of table `test`.`test_table` trx id 79624759936 lock_mode X locks gap before rec insert intention waiting
*** (2) TRANSACTION:
TRANSACTION 79624759935, ACTIVE 0 sec inserting, thread declared inside InnoDB 1
mysql tables in use 1, locked 1
4 lock struct(s), heap size 1136, 3 row lock(s), undo log entries 1
MySQL thread id 8549322, OS thread handle 140620501346048, query id 39084605258 10.58.1.34 test_x update
insert into test_table (`uid`,`did`,`key`,`value`,`last_modify`) values (251081666,'blt.1.1a6j65qgt4g01','2022-05-27','{\"data\":{\"date\":\"2022-05-27\",\"data\":[{\"balance\":68,\"coverage\":33,\"duration\":83,\"over\":0,\"score\":61,\"date\":\"2022-05-27 06:34:28\",\"diagram1\":[true,true,false,false,true,false],\"diagram2\":[false,false,false,false,false,false],\"dateTimer\":1653604468000},{\"balance\":69,\"coverage\":50,\"duration\":87,\"over\":0,\"score\":67,\"date\":\"2022-05-27 20:46:28\",\"diagram1\":[true,true,false,false,true,false],\"diagram2\":[false,false,false,false,false,false],\"dateTimer\":1653655588000}],\"dateTimer\":1653580800000,\"score\":64,\"balance\":68,\"coverage\":41,\"duration\":85,\"over\":0},\"timestamp\":1658269502440}',1658269503) ON DUPLICATE KEY UPDATE `uid`=values(`uid`),`did`=values(`did`),`key`=values(`key`),`value`=values(`value`),`last_modify`=values(`last_modify`
*** (2) HOLDS THE LOCK(S):
RECORD LOCKS space id 6918 page no 623 n bits 360 index uk_idx_uid_did_key of table `test`.`test_table` trx id 79624759935 lock_mode X locks gap before rec
*** (2) WAITING FOR THIS LOCK TO BE GRANTED:
RECORD LOCKS space id 6918 page no 623 n bits 360 index uk_idx_uid_did_key of table `test`.`test_table` trx id 79624759935 lock_mode X locks gap before rec insert intention waiting
*** WE ROLL BACK TRANSACTION (1)
------------
TRANSACTIONS
------------
Trx id counter 79866968406
Purge done for trx's n:o < 79866968399 undo n:o < 0 state: running but idle
History list length 31
LIST OF TRANSACTIONS FOR EACH SESSION:
---TRANSACTION 422130403662144, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403640712, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404034384, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404029872, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404012952, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404008440, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404005056, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404002800, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403997160, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403987008, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403983624, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403976856, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403963320, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403952040, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403948656, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403945272, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403941888, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403936248, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403928352, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403921584, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403920456, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403912560, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403911432, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403910304, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403904664, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403895640, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403891128, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403888872, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403884360, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403879848, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403875336, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403874208, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403871952, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403859544, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403853904, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403841496, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403836984, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403835856, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403830216, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403812168, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403808784, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403699368, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403672296, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403659888, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403649736, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403646352, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403633944, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403632816, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403636200, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403623792, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403619280, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403629432, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403937376, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403933992, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403924968, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403695984, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403743360, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403683576, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403953168, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403833600, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403618152, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403650864, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403661016, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403642968, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403657632, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403654248, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403655376, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403653120, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403651992, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403644096, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403641840, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403639584, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403638456, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403635072, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403627176, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403622664, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403617024, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130405048456, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130405040560, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130405031536, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130405012360, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404981904, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404943552, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404941296, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404865720, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404845416, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404833008, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404695392, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404790144, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404783376, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404775480, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404746152, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404741640, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404701032, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404696520, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404693136, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404675088, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404672832, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404651400, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404619816, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404599512, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404573568, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404560032, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404540856, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404512656, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404505888, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404502504, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404493480, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404488968, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404484456, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404478816, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404473176, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404466408, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404463024, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404451744, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404446104, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404439336, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404367144, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404341200, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404317512, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404316384, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130404310744, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403744488, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403756896, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403782840, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403843752, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403840368, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403839240, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403834728, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403829088, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403754640, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403820064, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403807656, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403787352, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403736592, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403806528, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403805400, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403800888, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403788480, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403741104, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403798632, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403797504, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403796376, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403760280, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403735464, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403779456, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403777200, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403776072, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403773816, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403772688, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403771560, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403738848, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403749000, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403747872, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403745616, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403742232, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403739976, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403765920, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403763664, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403762536, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403737720, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403621536, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403630560, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403730952, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403729824, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403728696, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403727568, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403723056, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403721928, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403720800, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403719672, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403718544, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403717416, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403715160, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403711776, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403709520, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403708392, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403707264, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403705008, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403701624, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403700496, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403697112, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403693728, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403690344, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403689216, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403688088, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403686960, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403685832, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403684704, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403682448, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403681320, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403680192, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403679064, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403677936, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403676808, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403675680, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403674552, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403673424, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403671168, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403670040, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403668912, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403667784, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403666656, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403665528, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403664400, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403663272, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403658760, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403656504, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403648608, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403626048, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403624920, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403620408, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403789608, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403804272, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403637328, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403783968, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403631688, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403628304, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403647480, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
---TRANSACTION 422130403645224, not started
0 lock struct(s), heap size 1136, 0 row lock(s)
--------
FILE I/O
--------
I/O thread 0 state: waiting for completed aio requests (insert buffer thread)
I/O thread 1 state: waiting for completed aio requests (log thread)
I/O thread 2 state: waiting for completed aio requests (read thread)
I/O thread 3 state: waiting for completed aio requests (read thread)
I/O thread 4 state: waiting for completed aio requests (read thread)
I/O thread 5 state: waiting for completed aio requests (read thread)
I/O thread 6 state: waiting for completed aio requests (read thread)
I/O thread 7 state: waiting for completed aio requests (read thread)
I/O thread 8 state: waiting for completed aio requests (read thread)
I/O thread 9 state: waiting for completed aio requests (read thread)
I/O thread 10 state: waiting for completed aio requests (read thread)
I/O thread 11 state: waiting for completed aio requests (read thread)
I/O thread 12 state: waiting for completed aio requests (read thread)
I/O thread 13 state: waiting for completed aio requests (read thread)
I/O thread 14 state: waiting for completed aio requests (read thread)
I/O thread 15 state: waiting for completed aio requests (read thread)
I/O thread 16 state: waiting for completed aio requests (read thread)
I/O thread 17 state: waiting for completed aio requests (read thread)
I/O thread 18 state: waiting for completed aio requests (write thread)
I/O thread 19 state: waiting for completed aio requests (write thread)
I/O thread 20 state: waiting for completed aio requests (write thread)
I/O thread 21 state: waiting for completed aio requests (write thread)
I/O thread 22 state: waiting for completed aio requests (write thread)
I/O thread 23 state: waiting for completed aio requests (write thread)
I/O thread 24 state: waiting for completed aio requests (write thread)
I/O thread 25 state: waiting for completed aio requests (write thread)
Pending normal aio reads: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] , aio writes: [0, 0, 0, 0, 0, 0, 0, 0] ,
 ibuf aio reads:, log i/o's:, sync i/o's:
Pending flushes (fsync) log: 0; buffer pool: 0
2348130124 OS file reads, 6603285620 OS file writes, 401533899 OS fsyncs
0.00 reads/s, 0 avg bytes/read, 818.91 writes/s, 0.95 fsyncs/s
-------------------------------------
INSERT BUFFER AND ADAPTIVE HASH INDEX
-------------------------------------
Ibuf: size 1, free list len 18728, seg size 18730, 1112365459 merges
merged operations:
 insert 1500529931, delete mark 50053629, delete 1286226
discarded operations:
 insert 51, delete mark 0, delete 0
Hash table size 7844257, node heap has 104 buffer(s)
Hash table size 7844257, node heap has 54 buffer(s)
Hash table size 7844257, node heap has 32 buffer(s)
Hash table size 7844257, node heap has 95 buffer(s)
Hash table size 7844257, node heap has 96 buffer(s)
Hash table size 7844257, node heap has 2542 buffer(s)
Hash table size 7844257, node heap has 183 buffer(s)
Hash table size 7844257, node heap has 20 buffer(s)
1939.48 hash searches/s, 2559.69 non-hash searches/s
---
LOG
---
Log sequence number 16131164089282
Log flushed up to   16131163932862
Pages flushed up to 16130995063258
Last checkpoint at  16130995063258
Max checkpoint age    10433226609
Checkpoint age target 10107188278
Modified age          169026024
Checkpoint age        169026024
0 pending log flushes, 0 pending chkp writes
2413674629 log i/o's done, 818.95 log i/o's/second
----------------------
BUFFER POOL AND MEMORY
----------------------
Total large memory allocated 48335159296
Dictionary memory allocated 22492088
Internal hash tables (constant factor + variable factor)
    Adaptive hash index 553282496 	(502032448 + 51250048)
    Page hash           3922936 (buffer pool 0 only)
    Dictionary cache    148000200 	(125508112 + 22492088)
    File system         2608624 	(812272 + 1796352)
    Lock system         79937448 	(79687528 + 249920)
    Recovery system     0 	(0 + 0)
Buffer pool size   2774016
Buffer pool size, bytes 45449478144
Free buffers       895505
Database pages     1875385
Old database pages 692119
Modified db pages  14113
Pending reads      0
Pending writes: LRU 0, flush list 0, single page 0
Pages made young 466536285, not young 1961378780
0.00 youngs/s, 0.00 non-youngs/s
Pages read 2348194302, created 28366344, written 4039514323
0.00 reads/s, 0.14 creates/s, 0.00 writes/s
Buffer pool hit rate 1000 / 1000, young-making rate 0 / 1000 not 0 / 1000
Pages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s
LRU len: 1875385, unzip_LRU len: 0
I/O sum[0]:cur[0], unzip sum[0]:cur[0]
----------------------
INDIVIDUAL BUFFER POOL INFO
----------------------
---BUFFER POOL 0
Buffer pool size   346752
Buffer pool size, bytes 5681184768
Free buffers       111936
Database pages     234425
Old database pages 86515
Modified db pages  1959
Pending reads      0
Pending writes: LRU 0, flush list 0, single page 0
Pages made young 58538975, not young 243501850
0.00 youngs/s, 0.00 non-youngs/s
Pages read 294982579, created 3555661, written 506681825
0.00 reads/s, 0.00 creates/s, 0.00 writes/s
Buffer pool hit rate 1000 / 1000, young-making rate 0 / 1000 not 0 / 1000
Pages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s
LRU len: 234425, unzip_LRU len: 0
I/O sum[0]:cur[0], unzip sum[0]:cur[0]
---BUFFER POOL 1
Buffer pool size   346752
Buffer pool size, bytes 5681184768
Free buffers       111939
Database pages     234422
Old database pages 86515
Modified db pages  1626
Pending reads      0
Pending writes: LRU 0, flush list 0, single page 0
Pages made young 58946658, not young 243882993
0.00 youngs/s, 0.00 non-youngs/s
Pages read 297491886, created 3555781, written 499766818
0.00 reads/s, 0.05 creates/s, 0.00 writes/s
Buffer pool hit rate 1000 / 1000, young-making rate 0 / 1000 not 0 / 1000
Pages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s
LRU len: 234422, unzip_LRU len: 0
I/O sum[0]:cur[0], unzip sum[0]:cur[0]
---BUFFER POOL 2
Buffer pool size   346752
Buffer pool size, bytes 5681184768
Free buffers       111941
Database pages     234421
Old database pages 86514
Modified db pages  1726
Pending reads      0
Pending writes: LRU 0, flush list 0, single page 0
Pages made young 57539184, not young 234751969
0.00 youngs/s, 0.00 non-youngs/s
Pages read 281151452, created 3459564, written 507126368
0.00 reads/s, 0.00 creates/s, 0.00 writes/s
Buffer pool hit rate 1000 / 1000, young-making rate 0 / 1000 not 0 / 1000
Pages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s
LRU len: 234421, unzip_LRU len: 0
I/O sum[0]:cur[0], unzip sum[0]:cur[0]
---BUFFER POOL 3
Buffer pool size   346752
Buffer pool size, bytes 5681184768
Free buffers       111943
Database pages     234417
Old database pages 86514
Modified db pages  1972
Pending reads      0
Pending writes: LRU 0, flush list 0, single page 0
Pages made young 58359150, not young 249596435
0.00 youngs/s, 0.00 non-youngs/s
Pages read 296836527, created 3563830, written 505895542
0.00 reads/s, 0.00 creates/s, 0.00 writes/s
Buffer pool hit rate 1000 / 1000, young-making rate 0 / 1000 not 0 / 1000
Pages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s
LRU len: 234417, unzip_LRU len: 0
I/O sum[0]:cur[0], unzip sum[0]:cur[0]
---BUFFER POOL 4
Buffer pool size   346752
Buffer pool size, bytes 5681184768
Free buffers       111988
Database pages     234373
Old database pages 86496
Modified db pages  1622
Pending reads      0
Pending writes: LRU 0, flush list 0, single page 0
Pages made young 58864011, not young 250156318
0.00 youngs/s, 0.00 non-youngs/s
Pages read 295198928, created 3556826, written 506931694
0.00 reads/s, 0.00 creates/s, 0.00 writes/s
Buffer pool hit rate 1000 / 1000, young-making rate 0 / 1000 not 0 / 1000
Pages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s
LRU len: 234373, unzip_LRU len: 0
I/O sum[0]:cur[0], unzip sum[0]:cur[0]
---BUFFER POOL 5
Buffer pool size   346752
Buffer pool size, bytes 5681184768
Free buffers       111896
Database pages     234465
Old database pages 86530
Modified db pages  1718
Pending reads      0
Pending writes: LRU 0, flush list 0, single page 0
Pages made young 57717244, not young 242956396
0.00 youngs/s, 0.00 non-youngs/s
Pages read 291607244, created 3556031, written 502645890
0.00 reads/s, 0.00 creates/s, 0.00 writes/s
Buffer pool hit rate 1000 / 1000, young-making rate 0 / 1000 not 0 / 1000
Pages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s
LRU len: 234465, unzip_LRU len: 0
I/O sum[0]:cur[0], unzip sum[0]:cur[0]
---BUFFER POOL 6
Buffer pool size   346752
Buffer pool size, bytes 5681184768
Free buffers       111898
Database pages     234463
Old database pages 86529
Modified db pages  1780
Pending reads      0
Pending writes: LRU 0, flush list 0, single page 0
Pages made young 57801984, not young 246341442
0.00 youngs/s, 0.00 non-youngs/s
Pages read 293288647, created 3560415, written 507058811
0.00 reads/s, 0.10 creates/s, 0.00 writes/s
Buffer pool hit rate 1000 / 1000, young-making rate 0 / 1000 not 0 / 1000
Pages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s
LRU len: 234463, unzip_LRU len: 0
I/O sum[0]:cur[0], unzip sum[0]:cur[0]
---BUFFER POOL 7
Buffer pool size   346752
Buffer pool size, bytes 5681184768
Free buffers       111964
Database pages     234399
Old database pages 86506
Modified db pages  1710
Pending reads      0
Pending writes: LRU 0, flush list 0, single page 0
Pages made young 58769079, not young 250191377
0.00 youngs/s, 0.00 non-youngs/s
Pages read 297637039, created 3558236, written 503407375
0.00 reads/s, 0.00 creates/s, 0.00 writes/s
Buffer pool hit rate 1000 / 1000, young-making rate 0 / 1000 not 0 / 1000
Pages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s
LRU len: 234399, unzip_LRU len: 0
I/O sum[0]:cur[0], unzip sum[0]:cur[0]
--------------
ROW OPERATIONS
--------------
0 queries inside InnoDB, 0 queries in queue
0 read views open inside InnoDB
0 RW transactions active inside InnoDB
Process ID=24212, Main thread ID=140620911863552, state: sleeping
Number of rows inserted 3586466919, updated 634921403, deleted 348330946, read 1086321884761
83.66 inserts/s, 814.53 updates/s, 1.24 deletes/s, 404265.27 reads/s
----------------------------
END OF INNODB MONITOR OUTPUT
============================
