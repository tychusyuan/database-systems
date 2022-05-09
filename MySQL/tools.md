# Tools

## database info

### 排查 数据库中所有表 大小
```sql
SELECT concat( table_schema, '.', table_name ) table_name,  
concat( round( data_length / ( 1024 *1024*1024 ) , 2 ) , 'G' ) data_length,  
concat( round( index_length / ( 1024 *1024*1024 ) , 2 ) , 'G' ) index_length,  
concat( round( round( data_length + index_length ) / ( 1024 *1024*1024 ) , 2 ) , 'G' ) total_size,  
concat( round( DATA_FREE / ( 1024 *1024*1024 ) , 2 ) , 'G' ) DATA_FREE  
FROM information_schema.TABLES 
ORDER BY information_schema.TABLES.DATA_LENGTH DESC LIMIT 50;
```