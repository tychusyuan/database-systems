
## Table 14.10 Online DDL Support for Index Operations

|Operation	|In Place	|Rebuilds Table	|Permits Concurrent DML	|Only Modifies Metadata|
|--|--|--|--|--|
|Creating or adding a secondary index	|Yes	|No	|Yes	|No|
|Dropping an index	|Yes	|No	|Yes	|Yes|
|Renaming an index	|Yes	|No	|Yes	|Yes|
|Adding a FULLTEXT index	|Yes*	|No*	|No	|No|
|Adding a SPATIAL index	|Yes	|No	|No	|No|
|Changing the index type	|Yes	|No	|Yes	|Yes|

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
