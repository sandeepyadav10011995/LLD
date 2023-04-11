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
   * ![image](https://user-images.githubusercontent.com/22426280/231045734-7bd655f0-1d1f-4766-9c6f-cef33ba8769d.png)
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
   
### 
* Window functions: Window functions are used to perform calculations on a specific window or subset of rows within a result set. 
   * The most commonly used window functions include ROW_NUMBER(), RANK(), DENSE_RANK(), and NTILE(). 
   * Here's an example of how to use the ROW_NUMBER() function:
   ```
      SELECT product_name, product_price, 
          ROW_NUMBER() OVER (ORDER BY product_price DESC) AS rank
      FROM products;
   ```
   * This query returns the product name, price, and the row number of each product based on its price, ordered from highest to lowest.
* RANK: RANK is a ranking function that assigns a rank to each row within a result set based on a specified column. 
   * If there are ties, the same rank is assigned to all rows with the same value. 
   * Here's an example of how to use the RANK function:
   ```
      SELECT product_name, product_price, 
       RANK() OVER (ORDER BY product_price DESC) AS rank
      FROM products;
   ```
   * This query returns the product name, price, and the rank of each product based on its price, ordered from highest to lowest. 
   * If there are two products with the same price, they will be assigned the same rank.

## SQL Procedure
* A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.
* Syntax -:
   ```
   CREATE PROCEDURE procedure_name
   AS
   sql_statement
   GO;
   EXEC procedure_name;
   
   --------------EXAMPLE----------------------
   CREATE PROCEDURE SelectAllCustomers
   AS
   SELECT * FROM Customers
   GO;
   
   Execute the stored procedure above as follows:
   Example
   EXEC SelectAllCustomers;
   ```
## SQL Comments
   * Single line comments start with --
   * Multi-line comments start with /* and end with */ 

## BACKUP DB 
* __BACKUP DATABASE__ statement is used in SQL Server to create a full back up of an existing SQL database.
   * Syntax -:
   ```
      BACKUP DATABASE databasename
      TO DISK = 'filepath';
   ```
* __BACKUP WITH DIFFERENTIAL__ -:A differential back up only backs up the parts of the database that have changed since the last full database backup. 
   * Syntax -:
   ```
      BACKUP DATABASE databasename
      TO DISK = 'filepath'
      WITH DIFFERENTIAL;
   ```
## CHECK 
* __CHECK__ constraint is used to limit the value range that can be placed in a column
* Syntax -:
   ```
      CREATE TABLE Persons (
          ID int NOT NULL,
          LastName varchar(255) NOT NULL,
          FirstName varchar(255),
          Age int,
          CHECK (Age>=18)
      );
   ```
 
## AUTOINCREMENT
* Auto-increment allows a unique number to be generated automatically when a new record is inserted into a table.
* Often this is the primary key field that we would like to be created automatically every time a new record is inserted.

## SQL VIEWS
* A view is a virtual table based on the result-set of an SQL statement.
* A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database.
* You can add SQL statements and functions to a view and present the data as if the data were coming from one single table.
* A view is created with the CREATE VIEW statement. 
* Syntax -:
   ```
      CREATE VIEW view_name AS
      SELECT column1, column2, ...
      FROM table_name
      WHERE condition;
   ```
* __Note__: A view always shows up-to-date data! The database engine recreates the view, every time a user queries it.
* A view can be updated with the __CREATE OR REPLACE VIEW__ statement.
* A view is deleted with the __DROP VIEW__ statement.
 
# SQL Questions:
* __Write a SQL Query to count the number of unique users who logged in from both iPhone and web where iPhone Logs and web logs are in Distinct relations.__
   * __Assumptions__ -: 
      * iphone : ts | userId | iphoneSessionId
      * web :    ts | userId | webSessionId

   * __Solution Strategy__ -:
      * join web and iphone tables
      * Match by day(ts) and userId
      * Group By day and count numUsers
      * Final Table : day | numUsers

   * __Final Query__
       ```
          SELECT DATE_TRUNC('day', i.ts) AS day,
                 COUNT(DISTINCT i.userId) AS numUsers
          FROM iphone i
          JOIN web w
               ON i.userdId = w.userId
               AND DATE_TRUNC('day', i.ts) = DATE_TRUNC('day', w.ts)
          GROUP BY 1
       ```
* Write a SQL Query to "Find the business and the reviews_text that received the highest number of "cool" votes"
   * __Assumptions__ -: 
      * yelp_reviews : business_name | review_text | review_id | user_id | cool | funny | ...

   * __Solution Strategy__ -:
      * ORDER BY cool DESC
      * SELECT business_name, review_text
      * LIMIT 1
      * Final Table : business_name | review_text

   * __Final Query__
       ```
          SELECT business_name, 
                 review_text
          FROM yelp_reviews
          ORDER BY cool DESC
          LIMIT 1
       ```
 * __Write a SQL Query to "Number of conversations by each user". Find out the number of conversations (send or receive) by each user by date__
   * __Assumptions__ -: 
      * fb_messages : id | date | user1 | user2 | msg_count

   * __Solution Strategy__ -:
      * Get msg_count from received
      * Union ALL with Sent
      * Final Table : date | user1 | msg_count

   * __Final Query__
       ```
          (SELECT date, 
                 user1,
                 msg_count
          FROM fb_messages)
          UNION ALL (As we want the duplicates too)
          (SELECT date,
                 user2,
                 msg_count
          FROM fb_messages)
       ```
 
* __Write a SQL Query to "Find out the overall friend acceptance rate for each day."__
   * __Assumptions__ -: 
      * friend_requests : ds | sender | receiver | action(SENT, ACCEPTED, REJECTED ETC..)
      * 

   * __Solution Strategy__ -:
      * GROUP By ds
      * accepted/COUNT(actions)*100
      * Final Table : ds | friend_acceptance_rate --> ACCEPTED/TOTAL *100

   * __Final Query__
       ```
          SELECT ds,
                 COUNT(
                      CASE
                          WHEN action = 'ACCEPTED' THEN 1
                          ELSE NULL END) * 1.0 / COUNT(action) * 100 AS friend_acceptance_rate
          FROM friend_requests
          GROUP By 1
       ```
 
* __Write a SQL Query to "DOWNLOAD FACTS : Find the total number of downloads for paying and non-paying users by date and include only records where non-paying customers have more downloads than payong customers. The output should be sorted by earliest date first and contain 3 columns date, non-paying downloads, paying downloads "__
   * __Assumptions__ -: 
      * ms_user_dimensions : user_id | acc_id
      * ms_acc_dimensions : user_id | paying_customers
      * ms_downbloads_facts : date | user_id | downloads

   * __Solution Strategy__ -:
      * join ms_user_dimensions, ms_acc_dimensions, ms_downbloads_facts
      * GROUP BY date
      * SUM all downloads for paying and non-paying customers
      * ORDER BY date
      * non-paying customers > paying customers
      * Final Table : date | non-payng downloads | paying downloads

   * __Final Query__ --> common table expression (CTE)
       ```
          WITH temp AS(
               SELECT date,
                      SUM(CASE
                          WHEN paying_customer = 'no' THEN downloads END) AS non_paying,
                          SUM(CASE
                          WHEN paying_customer = 'yes' THEN downloads END) AS paying
               FROM ms_user_dimensions u
               JOIN ms_acc_dimensions a
                    ON u.acc_id = a.acc_id 
               JOIN ms_downbloads_facts f
                    ON u.user_id = f.user_id
               GROUP BY 1
               ORDER BY 1
               )

          SELECT *
          FROM temp
          WHERE non_paying > paying
       ```

* __Write a SQL Query to "Employee Project Budgets: Find the top five most expensive projects by the amount of amount of budget alloacted to each employee on the project. Excludes project with 0 employees. Assume each employee works on only one project. The output should be the project title and the budget that's allocated to each employee (i.e, budget-to-employee-ratio). Display the top 5 projects with the highest budget-to-employee ratio first."__
   * __Assumptions__ -: 
      * ms_projects : id | title | budget
      * ms_emp_projects : emp_id | project_id

   * __Solution Strategy__ -:
      * INNER JOIN ms_projects and ms_emp_projects
      * GROUP BY title
      * budget/COUNT(employee)
      * ORDER BY budget/COUNT(employee)
      * LIMIT 5
      * Final Table : project | budget_emp_ratio = budget/count(employee)

   * __Final Query__
       ```
          SELECT title AS project,
                 budget/COUNT(emp_id) AS budget_emp_ratio
          FROM ms_projects p
          INNER_JOIN ms_emp_projects e
               ON p.id = e.project_id
          GROUP BY 1
          ORDER BY 2 DESC
          LIMIT 5
       ```

* __Write a SQL Query to "Min, Avg, Max Price Per Review Qualification: Find the min, avg, max rental price for each review qualification category. The review qualification category is a classifcation applied to each rental property based on the number of reviews the property has. It is defined as below -:__
   *  0 reviews : NO
   *  1 to 5 reviews : FEW
   *  6 to 15 reviews : SOME
   *  16 to 40 reviews : MANY
   *  more than 40 reviews : ALOT
   * __Assumptions__ -: 
      * airbnb_search_details

   * __Solution Strategy__ -:
      * do classification -> CASE
      * GROUP BY qualification category
      * Aggregate min, avg, max price
      * CTE
      * Final Table : review_qualification | min | avg | max

   * __Final Query__
       ```
          WITH reviews AS
               (SELECT CASE
                          WHEN number_of_reviews = 0 THEN 'NO'
                          WHEN number_of_reviews BETWEEN 1 AND 5 THEN 'FEW'
                          WHEN number_of_reviews BETWEEN 6 AND 15 THEN 'SOME'
                          WHEN number_of_reviews BETWEEN 16 AND 40 THEN 'MANY'
                          ELSE 'A LOT' END AS review_qualification,
                          price
               FROM airbnb_search_details)
          SELECT review_qualification,
                 MIN(price) AS min_price,
                 AVG(price) AS avg_price,
                 MAX(price) AS max_price,
          FROM reviews
          GROUP BY 1
       ```
 
 * __Write a SQL Query to "Average Percentile: Find the email activity percentile for each user. email activity percentile is defined by the total number of emails sent. The user with the highest number of emails sent will have a percentile of 1 and so on. Ouput the user, total emails and their activity percentile and orders records by the total emails in descending order."__
   * __Assumptions__ -: 
      * google_gmail_emails : id | from_user | to_user | day

   * __Solution Strategy__ -:
      * GROUP By from_user
      * COUNT(*)
      * ROW_NUMBER -> WINDOW FUNCTION
      * Final Table : user | tital_emails | ntile

   * __Final Query__
       ```
          SELECT from_user,
                 COUNT(*) AS total_emails,
                 ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS ntile
          FROM google_gmail_emails
          GROUP BY 1
          
          Alternate Solution -:
          WITH temp AS (SELECT from_user,
                 COUNT(*) AS total_emails,
          FROM google_gmail_emails
          GROUP BY 1)
          
          SELECT *,
                 NTILE(100) OVER (ORDER BY total_emails DESC) AS 
          FROM temp
       ```
       
* __Write a SQL Query to "GROWTH OF AIRBNB : Estimate the growth of Airbnb each year using the number of hosts registered as the growth metric. The rate of grwoth is calculated by taking ((number of hosts registered in the current year - number of hosts registered in the previous year)/(number of hosts registered in the previous year) mul by 100"__
   * __Assumptions__ -: 
      * airbnb_search_details : 

   * __Solution Strategy__ -:
      * get year  and num_hosts
      * left self join on prev_year = curr_year-1
      * curr_year | num_hosts_curr | num_hosts_prev | growth_rate
      * (num_hosts_curr - num_hosts_prev) / num_hosts_prev * 100
      * ROUND growth_rate
      * Order BY curr_year
      * Final Table : year | num_hosts_curr | num_hosts_prev | growth_rate

   * __Final Query__
       ```
          WITH registers AS
               (SELECT EXTRACT(year FROM hosts_since) AS year,
                      COUNT(id) AS num_hosts
               FROM airbnb_search_details
               GROUP BY 1)
         
          SELECT curr_year.year AS year,
                curr_year.num_hosts as num_hosts_curr,
                prev_year.num_hosts as num_hosts_prev,
                (curr_year.num_hosts-curr-prev_year.num_hosts*1.0)/prev_year.num_hosts * 100 as growth_rate
          FROM registers curr_year
          LEFT JOIN register prev_year
              ON prev_year.year = curr_year.year - 1
          ORDER BY 1    
       ```       
 

 
