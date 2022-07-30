
## Table 14.10 Online DDL Support for Index Operations

|Operation|V	|Instant|In Place	|Rebuilds Table	|Permits Concurrent DML	|Only Modifies Metadata|
|--|--|--|--|--|--|--|
|Creating or adding a secondary index|5.7	|No|Yes	|No	|Yes	|No|
||8.0	|No	|Yes	|No	|Yes	|No|
|Dropping an index|5.7	|No|Yes	|No	|Yes	|Yes|
||8.0	|No	|Yes	|No	|Yes	|Yes|
|Renaming an index|5.7	|No|Yes	|No	|Yes	|Yes|
||8.0	|No	|Yes	|No	|Yes	|Yes|
|Adding a FULLTEXT index|5.7	|No|Yes*	|No*	|No	|No|
||8.0	|No	|Yes*	|No*	|No	|No|
|Adding a SPATIAL index|5.7	|No|Yes	|No	|No	|No|
||8.0	|No	|Yes	|No	|No	|No|
|Changing the index type|5.7	|No|Yes	|No	|Yes	|Yes|
||8.0	|Yes	|Yes	|No	|Yes	Yes|

## Table 14.11 Online DDL Support for Primary Key Operations

|Operation	|In Place	|Rebuilds Table	|Permits Concurrent DML	|Only Modifies Metadata|
|--|--|--|--|--|
|Adding a primary key	|Yes*	|Yes*	|Yes	|No|
|Dropping a primary key	|No	|Yes	|No	|No|
|Dropping a primary key and adding another	|Yes	|Yes	|Yes	|No|

## Table 14.12 Online DDL Support for Column Operations

|Operation	|In Place	|Rebuilds Table	|Permits Concurrent DML	|Only Modifies Metadata|
|--|--|--|--|--|
|Adding a column	|Yes	|Yes	|Yes*	|No|
|Dropping a column	|Yes	|Yes	|Yes	|No|
|Renaming a column	|Yes	|No	|Yes*	|Yes|
|Reordering columns	|Yes	|Yes	|Yes	|No|
|Setting a column default value	|Yes	|No	|Yes	|Yes|
|Changing the column data type	|No	|Yes	|No	|No|
|Extending VARCHAR column size	|Yes	|No	|Yes	|Yes|
|Dropping the column default value	|Yes	|No	|Yes	|Yes|
|Changing the auto-increment value	|Yes	|No	|Yes	|No*|
|Making a column NULL	|Yes	|Yes*	|Yes	|No|
|Making a column NOT NULL	|Yes*	|Yes*	|Yes	|No|
|Modifying the definition of an ENUM or SET column	|Yes	|No	|Yes	|Yes|

## Table 14.13 Online DDL Support for Generated Column Operations

|Operation	|In Place	|Rebuilds Table	|Permits Concurrent DML	|Only Modifies Metadata|
|--|--|--|--|--|
|Adding a STORED column	|No	|Yes	|No	|No|
|Modifying STORED column order	|No	|Yes	|No	|No|
|Dropping a STORED column	|Yes	|Yes	|Yes	|No|
|Adding a VIRTUAL column	|Yes	|No	|Yes	|Yes|
|Modifying VIRTUAL column order	|No	|Yes	|No	|No|
|Dropping a VIRTUAL column	|Yes	|No	|Yes	|Yes|

## Table 14.14 Online DDL Support for Foreign Key Operations

|Operation	|In Place	|Rebuilds Table	|Permits Concurrent DML	|Only Modifies Metadata|
|--|--|--|--|--|
|Adding a foreign key constraint	|Yes*	|No	|Yes	|Yes|
|Dropping a foreign key constraint	|Yes	|No	|Yes	|Yes|

## Table 14.15 Online DDL Support for Table Operations

|Operation	|In Place	|Rebuilds Table	|Permits Concurrent DML	|Only Modifies Metadata|
|--|--|--|--|--|
|Changing the ROW_FORMAT	|Yes	|Yes	|Yes	|No|
|Changing the KEY_BLOCK_SIZE	|Yes	|Yes	|Yes	|No|
|Setting persistent table statistics	|Yes	|No	|Yes	|Yes|
|Specifying a character set	|Yes	|Yes*	|No	|No|
|Converting a character set	|No	|Yes*	|No	|No|
|Optimizing a table	|Yes*	|Yes	|Yes	|No|
|Rebuilding with the FORCE option	|Yes*	|Yes	|Yes	|No|
|Performing a null rebuild	|Yes*	|Yes	|Yes	|No|
|Renaming a table	|Yes	|No	|Yes	|Yes|

## Table 14.16 Online DDL Support for Tablespace Operations

|Operation	|In Place	|Rebuilds Table	|Permits Concurrent DML	|Only Modifies Metadata|
|--|--|--|--|--|
|Enabling or disabling file-per-table tablespace encryption	|No	|Yes	|No	|No|

## Table 14.17 Online DDL Support for Partitioning Operations

|Partitioning Clause	|In Place	|Permits DML	|Notes|
|--|--|--|--|
|PARTITION BY	|No	|No	|Permits ALGORITHM=COPY, LOCK=DEFAULT/SHARED/EXCLUSIVE|
|ADD PARTITION	|No	|No	|Only permits ALGORITHM=DEFAULT, LOCK=DEFAULT. Does not copy existing data for tables partitioned by RANGE or LIST. Concurrent queries are permitted for tables partitioned by HASH or LIST. MySQL copies the data while holding a shared lock.|
|DROP PARTITION	|No	|No	|Only permits ALGORITHM=DEFAULT, LOCK=DEFAULT. Does not copy existing data for tables partitioned by RANGE or LIST.|
|DISCARD PARTITION	|No	|No	|Only permits ALGORITHM=DEFAULT, LOCK=DEFAULT|
|IMPORT PARTITION	|No	|No	|Only permits ALGORITHM=DEFAULT, LOCK=DEFAULT|
|TRUNCATE PARTITION	|Yes	|Yes	|Does not copy existing data. It merely deletes rows; it does not alter the definition of the table itself, or of any of its partitions.|
|COALESCE PARTITION	|No	|No	|Only permits ALGORITHM=DEFAULT, LOCK=DEFAULT. Concurrent queries are permitted for tables partitioned by HASH or LIST, as MySQL copies the data while holding a shared lock.|
|REORGANIZE PARTITION	|No	|No	|Only permits ALGORITHM=DEFAULT, LOCK=DEFAULT. Concurrent queries are permitted for tables partitioned by LINEAR HASH or LIST. MySQL copies data from affected partitions while holding a shared metadata lock.|
|EXCHANGE PARTITION	|Yes	|Yes	|
|ANALYZE PARTITION	|Yes	|Yes	|
|CHECK PARTITION	|Yes	|Yes	|
|OPTIMIZE PARTITION	|No	|No	|ALGORITHM and LOCK clauses are ignored. Rebuilds the entire table. See Section 22.3.4, “Maintenance of Partitions”.|
|REBUILD PARTITION	|No	|No	|Only permits ALGORITHM=DEFAULT, LOCK=DEFAULT. Concurrent queries are permitted for tables partitioned by LINEAR HASH or LIST. MySQL copies data from affected partitions while holding a shared metadata lock.|
|REPAIR PARTITION	|Yes	|Yes	|
|REMOVE PARTITIONING	|No	|No	|Permits ALGORITHM=COPY, LOCK=DEFAULT/SHARED/EXCLUSIVE|
