# Strategy -: __SQL is an ANSI/ISO standard__
  * Read question + state assumptions.
  * Write down steps of query.
  * Write actual Query.
  * Check Query.
  * Suggest possible improvements.

# SQL Common Commands
___Some of The Most Important SQL Commands___
* __SELECT__ - extracts data from a database
* __UPDATE__ - updates data in a database
* __DELETE__ - deletes data from a database
* __INSERT INTO__ - inserts new data into a database
* __CREATE DATABASE__ - creates a new database
* __ALTER DATABASE__ - modifies a database
* __CREATE TABLE__ - creates a new table
* __ALTER TABLE__ - modifies a table
* __DROP TABLE__ - deletes a table
* __CREATE INDEX__ - creates an index (search key)
* __DROP INDEX__ - deletes an index

## SQL Common Clauses
* __SELECT DISTINCT__ statement is used to return only distinct (different) values.
* __WHERE__ clause is used to filter records.
   * ```
     SELECT column1, column2, ...
     FROM table_name
     WHERE condition;
     ```
   * The WHERE clause is not only used in SELECT statements, it is also used in UPDATE, DELETE, etc.!
* The __AND, OR and NOT__ operators are used to filter records based on more than one condition:
   * The __AND__ operator displays a record if all the conditions separated by AND are TRUE.
   * The __OR__ operator displays a record if any of the conditions separated by OR is TRUE.
   * The __NOT__ operator displays a record if the condition(s) is NOT TRUE.
* __ORDER BY__ keyword is used to sort the result-set in ascending or descending order
   * Sorts the records in ascending order by default.
   * To sort the records in descending order, use the DESC keyword.
   * ```
     SELECT column1, column2, ...
     FROM table_name
     ORDER BY column1, column2, ... ASC|DESC;
     ```
* __INSERT INTO__ statement is used to insert new records in a table. 
   * It is possible to write the INSERT INTO statement in two ways:
    1) Specify both the column names and the values to be inserted:
    2) If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query.

* __SELECT TOP / LIMIT__ clause is used to specify the number of records to return
   * It is useful on large tables with thousands of records. Returning a large number of records can impact performance.
   * Not all database systems support the __SELECT TOP__ clause. MySQL supports the __LIMIT__ clause to select a limited number of records
   * 
    ```
     SELECT column_name(s)
     FROM table_name
     WHERE condition
     LIMIT number;
    ```
* __MIN()__ function returns the __smallest value of the selected column__.
* __MAX()__ function returns the __largest value of the selected column__.
* __COUNT()__ function returns the __number of rows__ that matches a specified criterion
* __LIKE__ operator is used in a WHERE clause to search for a specified pattern in a column.
   * There are two wildcards often used in conjunction with the LIKE operator:
     * The percent sign (%) represents zero, one, or multiple characters
     * The underscore sign (_) represents one, single character
* SQL aliases are used to give a table, or a column in a table, a temporary name.
   * Aliases are often used to make column names more readable.
   * An alias only exists for the duration of that query.
   * An alias is created with the __AS__ keyword.
   * Alias Column Syntax
   ```
   SELECT column_name AS alias_name
   FROM table_name;
   ```
   * Alias Table Syntax
   ```
   SELECT column_name(s)
   FROM table_name AS alias_name;
   ```
* __JOIN__ clause is used to combine rows from two or more tables, based on a related column between them.
* __UNION__ operator is used to combine the result-set of two or more SELECT statements.
   * Every SELECT statement within UNION must have the same number of columns
   * The columns must also have similar data types
   * The columns in every SELECT statement must also be in the same order
   * __Note__ -: __UNION__ operator selects only distinct values by default. To allow duplicate values, use __UNION ALL__

* __GROUP BY__ statement groups rows that have the same values into summary rows 
   * GROUP BY statement is often used with aggregate functions (COUNT(), MAX(), MIN(), SUM(), AVG()) to group the result-set by one or more columns.
* __HAVING__ clause was added to SQL because the WHERE keyword cannot be used with aggregate functions.
   * 
   ```
      SELECT column_name(s)
      FROM table_name
      WHERE condition
      GROUP BY column_name(s)
      HAVING condition
      ORDER BY column_name(s);
   ```
* __EXISTS__ operator is used to test for the existence of any record in a subquery.
   * The EXISTS operator returns TRUE if the subquery returns one or more records
   * 
   ```
      SELECT column_name(s)
      FROM table_name
      WHERE EXISTS
      (SELECT column_name FROM table_name WHERE condition);
   ```  
* __ANY__ operator:  operator --> (=, <>, !=, >, >=, <, or <=)
   * returns a boolean value as a result
   * returns TRUE if ANY of the subquery values meet the condition
* __ALL__ operator:  operator --> (=, <>, !=, >, >=, <, or <=)
   * returns a boolean value as a result
   * returns TRUE if ALL of the subquery values meet the condition
   * is used with SELECT, WHERE and HAVING statements
* __CASE__ expression goes through conditions and returns a value when the first condition is met (like an if-then-else statement). 
   * So, once a condition is true, it will stop reading and return the result. 
   * If no conditions are true, it returns the value in the ELSE clause.
   * If there is no ELSE part and no conditions are true, it returns NULL.
   * Syntax
   ```
      CASE
          WHEN condition1 THEN result1
          WHEN condition2 THEN result2
          WHEN conditionN THEN resultN
          ELSE result
      END;
   ```
