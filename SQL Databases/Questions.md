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
* __Write a SQL Query to "Find the business and the reviews_text that received the highest number of "cool" votes"__
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
 
In SQL, both DISTINCT and GROUP BY are used to retrieve unique values from a table or a result set. However, there are some differences between the two:
  * DISTINCT is used to remove duplicates from a single column or a set of columns in the result set. It returns a distinct set of values for the selected column(s) while       maintaining the original order of the data. For example, the following query will return a list of unique countries from the customers table:
  ```
  SELECT DISTINCT country
  FROM customers;
  ```
  * GROUP BY is used to group the rows in a table based on one or more columns, and perform aggregate functions on each group. It returns one row for each group, with the       group column(s) and the result of the aggregate function(s). For example, the following query will group the customers by country and return the number of customers in       each country:
  ```
  SELECT country, COUNT(*) as num_customers
  FROM customers
  GROUP BY country;
  ```
**In summary, DISTINCT is used to retrieve unique values from one or more columns, while GROUP BY is used to group rows based on one or more columns and perform aggregate functions on each group.**
 
