
```sql
select d.*,b.*,e.*,c.* from information_schema.innodb_lock_waits as a  
inner join information_schema.innodb_locks as b on b.lock_trx_id = a.blocking_trx_id  
inner join information_schema.innodb_locks as c on c.lock_trx_id = a.requesting_trx_id 
inner join information_schema.innodb_trx as d on d.trx_id = a.blocking_trx_id 
inner join information_schema.innodb_trx as e on e.trx_id = a.requesting_trx_id\G
```
