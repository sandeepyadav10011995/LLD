## Why is PostgreSQL voted as the most loved database by Stackoverflow 2022 Developer Survey?

![image](https://user-images.githubusercontent.com/22426280/229983959-29551f80-441c-4c8d-8642-8688eda69e5f.png)

    🔹 OLTP (Online Transaction Processing)
        We can use PostgreSQL for CRUD (Create-Read-Update-Delete) operations.

    🔹 OLAP (Online Analytical Processing)
        We can use PostgreSQL for analytical processing. PostgreSQL is based on HTAP (Hybrid transactional/analytical processing) architecture, 
        so it can handle both OLTP and OLAP well.

    🔹 FDW (Foreign Data Wrapper)
        A FDW is an extension available in PostgreSQL that allows us to access a table or schema in one database from another.

    🔹 Streaming
        PipelineDB is a PostgreSQL extension for high-performance time-series aggregation, designed to power real-time reporting and analytics 
        applications.

    🔹 Geospatial
        PostGIS is a spatial database extender for PostgreSQL object-relational database. It adds support for geographic objects, allowing location 
        queries to be run in SQL.

    🔹 Time Series
        Timescale extends PostgreSQL for time series and analytics. For example, developers can combine relentless streams of financial and tick data 
        with other business data to build new apps and uncover unique insights.

    🔹 Distributed Tables
        CitusData scales Postgres by distributing data & queries. 

## Types Of SQL Joins -:
![image](https://user-images.githubusercontent.com/22426280/230443800-61df5bfd-4808-4ccf-9315-01cf37a231e0.png)

## How SQL works under the hood
* Step 1 - A SQL statement is sent to the database via a transport layer protocol (e.g.TCP).
* Step 2 - The SQL statement is sent to the command parser, where it goes through syntactic and semantic analysis, and a query tree is generated afterward.
* Step 3 - The query tree is sent to the optimizer. The optimizer creates an execution plan. 
* Step 4 - The execution plan is sent to the executor. The executor retrieves data from the execution.
* Step 5 - Access methods provide the data fetching logic required for execution, retrieving data from the storage engine. 
* Step 6 - Access methods decide whether the SQL statement is read-only. If the query is read-only (SELECT statement), it is passed to the buffer manager for further processing. The buffer manager looks for the data in the cache or data files.
* Step 7 - If the statement is an UPDATE or INSERT, it is passed to the transaction manager for further processing.
* Step 8 - During a transaction, the data is in lock mode. This is guaranteed by the lock manager. It also ensures the transaction’s ACID properties. 

![image](https://user-images.githubusercontent.com/22426280/230954311-a8773110-3610-46a8-a848-03e22d2e149e.png)


