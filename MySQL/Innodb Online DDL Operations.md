
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
