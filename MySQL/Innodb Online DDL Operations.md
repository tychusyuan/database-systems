
## Table 14.10 Online DDL Support for Index Operations

|Operation	|In Place	|Rebuilds Table	|Permits Concurrent DML	|Only Modifies Metadata|
|--|--|--|--|--|
|Creating or adding a secondary index	|Yes	|No	|Yes	|No|
|Dropping an index	|Yes	|No	|Yes	|Yes|
|Renaming an index	|Yes	|No	|Yes	|Yes|
|Adding a FULLTEXT index	|Yes*	|No*	|No	|No|
|Adding a SPATIAL index	|Yes	|No	|No	|No|
|Changing the index type	|Yes	|No	|Yes	|Yes|
