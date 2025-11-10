examples = [
{
"user_input": "What are total Apple sales in 2024?",
"sql": """SELECT SUM(total_price) AS total_apple_sales
FROM apple_sales2024
WHERE EXTRACT(YEAR FROM selling_date) = 2024"""
},
{
"user_input": "What are total Samsung sales in 2024?",
"sql": """SELECT SUM(total_price) AS total_samsung_sales
FROM samsung_sales2024
WHERE EXTRACT(YEAR FROM selling_date) = 2024"""
},
{
"user_input": "Compare total Apple and Samsung sales in 2024.",
"sql": """WITH apple AS (
  SELECT SUM(total_price) AS apple_sales FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
),
samsung AS (
  SELECT SUM(total_price) AS samsung_sales FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
)
SELECT a.apple_sales, s.samsung_sales FROM apple a CROSS JOIN samsung s"""
},
{
"user_input": "Show total quantity of Apple products sold in 2024.",
"sql": """SELECT SUM(quantity) AS total_apple_quantity
FROM apple_sales2024
WHERE EXTRACT(YEAR FROM selling_date) = 2024"""
},
{
"user_input": "Show total quantity of Samsung products sold in 2024.",
"sql": """SELECT SUM(quantity) AS total_samsung_quantity
FROM samsung_sales2024
WHERE EXTRACT(YEAR FROM selling_date) = 2024"""
},
{
"user_input": "What are Apple's month-wise sales in 2024?",
"sql": """SELECT
  EXTRACT(MONTH FROM selling_date) AS month,
  SUM(total_price) AS apple_sales
FROM apple_sales2024
WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY month
ORDER BY month;
"""
},
{
"user_input": "What are Samsung's month-wise sales in 2024?",
"sql": """SELECT
  EXTRACT(MONTH FROM selling_date) AS month,
  SUM(total_price) AS samsung_sales
FROM samsung_sales2024
WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY month
ORDER BY month;
"""
},
{
"user_input": "Show month-wise Apple sales in 2024.",
"sql": """SELECT EXTRACT(MONTH FROM selling_date) AS month,
SUM(total_price) AS monthly_sales
FROM apple_sales2024
WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY month ORDER BY month"""
},
{
"user_input": "Show month-wise Samsung sales in 2024.",
"sql": """SELECT EXTRACT(MONTH FROM selling_date) AS month,
SUM(total_price) AS monthly_sales
FROM samsung_sales2024
WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY month ORDER BY month"""
},
{
"user_input": "Compare Apple and Samsung month-wise sales in 2024.",
"sql": """WITH apple AS (
  SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS apple_sales
  FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024 GROUP BY month
),
samsung AS (
  SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024 GROUP BY month
)
SELECT COALESCE(a.month, s.month) AS month, a.apple_sales, s.samsung_sales
FROM apple a FULL OUTER JOIN samsung s ON a.month = s.month ORDER BY month"""
},
{
"user_input": "Show Apple’s city-wise total sales in 2024.",
"sql": """SELECT city, SUM(total_price) AS city_sales
FROM apple_sales2024
WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY city ORDER BY city_sales DESC"""
},
{
"user_input": "Show Samsung’s city-wise total sales in 2024.",
"sql": """SELECT city, SUM(total_price) AS city_sales
FROM samsung_sales2024
WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY city ORDER BY city_sales DESC"""
},
{
"user_input": "Compare city-wise sales of Apple and Samsung in 2024.",
"sql": """WITH apple AS (
  SELECT city, SUM(total_price) AS apple_sales FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024 GROUP BY city
),
samsung AS (
  SELECT city, SUM(total_price) AS samsung_sales FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024 GROUP BY city
)
SELECT COALESCE(a.city, s.city) AS city, a.apple_sales, s.samsung_sales
FROM apple a FULL OUTER JOIN samsung s ON a.city = s.city ORDER BY city"""
},
{
"user_input": "Which Apple product generated the highest sales in 2024?",
"sql": """SELECT product_name, SUM(total_price) AS total_sales
FROM apple_sales2024
WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY product_name ORDER BY total_sales DESC LIMIT 1"""
},
{
"user_input": "Which Samsung product generated the highest sales in 2024?",
"sql": """SELECT product_name, SUM(total_price) AS total_sales
FROM samsung_sales2024
WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY product_name ORDER BY total_sales DESC LIMIT 1"""
},
{
"user_input": "Show top 5 most sold Apple products in 2024.",
"sql": """SELECT product_name, SUM(quantity) AS total_quantity
FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY product_name ORDER BY total_quantity DESC LIMIT 5"""
},
{
"user_input": "Show top 5 most sold Samsung products in 2024.",
"sql": """SELECT product_name, SUM(quantity) AS total_quantity
FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY product_name ORDER BY total_quantity DESC LIMIT 5"""
},
{
"user_input": "Which Apple product had the highest profit in 2024?",
"sql": """SELECT product_name, SUM(selling_price - cost_price) AS total_profit
FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY product_name ORDER BY total_profit DESC LIMIT 1"""
},
{
"user_input": "Show Apple’s product-wise sales and profit in 2024.",
"sql": """SELECT product_name, SUM(quantity) AS total_quantity,
SUM(selling_price - cost_price) AS total_profit
FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY product_name ORDER BY total_profit DESC"""
},
{
"user_input": "Compare product-wise total sales for Apple and Samsung.",
"sql": """WITH apple AS (
  SELECT product_name, SUM(total_price) AS apple_sales
  FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY product_name
),
samsung AS (
  SELECT product_name, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY product_name
)
SELECT COALESCE(a.product_name, s.product_name) AS product_name,
a.apple_sales, s.samsung_sales
FROM apple a FULL OUTER JOIN samsung s ON a.product_name = s.product_name"""
},
{
"user_input": "Show month-wise profit for Apple in 2024.",
"sql": """SELECT EXTRACT(MONTH FROM selling_date) AS month,
SUM(selling_price - cost_price) AS total_profit
FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY month ORDER BY month"""
},
{
"user_input": "Compare month-wise profit for Apple and Samsung in 2024.",
"sql": """WITH apple AS (
  SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(selling_price - cost_price) AS apple_profit
  FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024 GROUP BY month
),
samsung AS (
  SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(selling_price - cost_price) AS samsung_profit
  FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024 GROUP BY month
)
SELECT COALESCE(a.month, s.month) AS month, a.apple_profit, s.samsung_profit
FROM apple a FULL OUTER JOIN samsung s ON a.month = s.month ORDER BY month"""
},
{
"user_input": "What is the total profit made by Apple in 2024?",
"sql": """SELECT SUM(selling_price - cost_price) AS total_profit
FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024"""
},
{
"user_input": "What is the total profit made by Samsung in 2024?",
"sql": """SELECT SUM(selling_price - cost_price) AS total_profit
FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024"""
},
{
"user_input": "What is the average selling price of Apple products in 2024?",
"sql": """SELECT AVG(selling_price) AS avg_selling_price
FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024"""
},
{
"user_input": "What is the average cost price of Samsung products in 2024?",
"sql": """SELECT AVG(cost_price) AS avg_cost_price
FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024"""
},
{
"user_input": "Compare average selling price of Apple and Samsung products in 2024.",
"sql": """WITH apple AS (
  SELECT AVG(selling_price) AS apple_avg_price FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
),
samsung AS (
  SELECT AVG(selling_price) AS samsung_avg_price FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
)
SELECT a.apple_avg_price, s.samsung_avg_price FROM apple a CROSS JOIN samsung s"""
},
{
"user_input": "Show total Apple sales per product in each city in 2024.",
"sql": """SELECT city, product_name, SUM(total_price) AS total_sales
FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY city, product_name ORDER BY city"""
},
{
"user_input": "Show Samsung’s product-wise sales by city in 2024.",
"sql": """SELECT city, product_name, SUM(total_price) AS total_sales
FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY city, product_name ORDER BY city"""
},
{
"user_input": "List top 3 cities with highest Apple sales in 2024.",
"sql": """SELECT city, SUM(total_price) AS total_sales
FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY city ORDER BY total_sales DESC LIMIT 3"""
},
{
"user_input": "List top 3 cities with highest Samsung sales in 2024.",
"sql": """SELECT city, SUM(total_price) AS total_sales
FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY city ORDER BY total_sales DESC LIMIT 3"""
},
{
"user_input": "Show all Apple products sold in Mumbai in 2024.",
"sql": """SELECT product_name, SUM(quantity) AS total_quantity
FROM apple_sales2024 WHERE city = 'Mumbai' AND EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY product_name ORDER BY total_quantity DESC"""
},
{
"user_input": "Compare Apple and Samsung total sales in Delhi.",
"sql": """WITH apple AS (
  SELECT SUM(total_price) AS apple_sales FROM apple_sales2024
  WHERE city = 'Delhi' AND EXTRACT(YEAR FROM selling_date) = 2024
),
samsung AS (
  SELECT SUM(total_price) AS samsung_sales FROM samsung_sales2024
  WHERE city = 'Delhi' AND EXTRACT(YEAR FROM selling_date) = 2024
)
SELECT a.apple_sales, s.samsung_sales FROM apple a CROSS JOIN samsung s"""
},
{
"user_input": "Show day-wise Apple sales for January 2024.",
"sql": """SELECT selling_date, SUM(total_price) AS daily_sales
FROM apple_sales2024
WHERE EXTRACT(MONTH FROM selling_date) = 1 AND EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY selling_date ORDER BY selling_date"""
},
{
"user_input": "Show day-wise Samsung sales for January 2024.",
"sql": """SELECT selling_date, SUM(total_price) AS daily_sales
FROM samsung_sales2024
WHERE EXTRACT(MONTH FROM selling_date) = 1 AND EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY selling_date ORDER BY selling_date"""
},
{
"user_input": "Which city sold the most Apple products by quantity?",
"sql": """SELECT city, SUM(quantity) AS total_quantity
FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY city ORDER BY total_quantity DESC LIMIT 1"""
},
{
"user_input": "Which product had the lowest profit margin for Apple in 2024?",
"sql": """SELECT product_name, SUM(selling_price - cost_price) AS total_profit
FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY product_name ORDER BY total_profit ASC LIMIT 1"""
},
{
"user_input": "What percentage of total sales came from Mumbai for Apple in 2024?",
"sql": """WITH total AS (
  SELECT SUM(total_price) AS total_sales FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
),
mumbai AS (
  SELECT SUM(total_price) AS mumbai_sales FROM apple_sales2024 WHERE city = 'Mumbai' AND EXTRACT(YEAR FROM selling_date) = 2024
)
SELECT (m.mumbai_sales * 100.0 / t.total_sales) AS mumbai_percentage
FROM total t, mumbai m"""
},
{
"user_input": "Show month-wise average quantity sold for Apple.",
"sql": """SELECT EXTRACT(MONTH FROM selling_date) AS month, AVG(quantity) AS avg_quantity
FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
GROUP BY month ORDER BY month"""
},
{
"user_input": "Show Apple’s total cost, total revenue, and profit in 2024.",
"sql": """SELECT SUM(cost_price * quantity) AS total_cost,
SUM(total_price) AS total_revenue,
SUM(total_price - cost_price * quantity) AS total_profit
FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024"""
},
{
"user_input": "Show Samsung’s total cost, total revenue, and profit in 2024.",
"sql": """SELECT SUM(cost_price * quantity) AS total_cost,
SUM(total_price) AS total_revenue,
SUM(total_price - cost_price * quantity) AS total_profit
FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024"""
},
{
  "user_input": "List all Apple products sold in Mumbai.",
  "sql": """SELECT DISTINCT product_name 
  FROM apple_sales2024 
  WHERE city = 'Mumbai';"""
},
{
  "user_input": "Show total Samsung sales from Delhi.",
  "sql": """SELECT SUM(total_price) AS total_sales 
  FROM samsung_sales2024 
  WHERE city = 'Delhi';"""
},
{
  "user_input": "Find the total revenue from all cities for Apple.",
  "sql": """SELECT city, SUM(total_price) AS total_revenue 
  FROM apple_sales2024 
  GROUP BY city;"""
},
{
  "user_input": "Which city had the highest Samsung sales?",
  "sql": """SELECT city, SUM(total_price) AS total_sales 
  FROM samsung_sales2024 
  GROUP BY city 
  ORDER BY total_sales DESC 
  LIMIT 1;"""
},
{
  "user_input": "What is the average selling price of Apple products?",
  "sql": """SELECT AVG(selling_price) AS avg_price 
  FROM apple_sales2024;"""
},
{
  "user_input": "Find the average profit per Samsung product.",
  "sql": """SELECT AVG(selling_price - cost_price) AS avg_profit 
  FROM samsung_sales2024;"""
},
{
  "user_input": "Show the total quantity of Apple items sold in January 2024.",
  "sql": """SELECT SUM(quantity) AS total_quantity 
  FROM apple_sales2024 
  WHERE EXTRACT(MONTH FROM selling_date) = 1;"""
},
{
  "user_input": "Show the most sold Samsung product by quantity.",
  "sql": """SELECT product_name, SUM(quantity) AS total_quantity 
  FROM samsung_sales2024 
  GROUP BY product_name 
  ORDER BY total_quantity DESC 
  LIMIT 1;"""
},
{
  "user_input": "List the cities where Apple sales exceeded 1 million.",
  "sql": """SELECT city, SUM(total_price) AS total_sales 
  FROM apple_sales2024 
  GROUP BY city 
  HAVING SUM(total_price) > 1000000;"""
},
{
  "user_input": "Show all Samsung sales made after July 2024.",
  "sql": """SELECT * FROM samsung_sales2024 
  WHERE selling_date > '2024-07-01';"""
},
{
  "user_input": "What is the total cost price for Apple in Kolkata?",
  "sql": """SELECT SUM(cost_price * quantity) AS total_cost 
  FROM apple_sales2024 
  WHERE city = 'Kolkata';"""
},
{
  "user_input": "Show the top 5 Samsung products by total sales amount.",
  "sql": """SELECT product_name, SUM(total_price) AS total_sales 
  FROM samsung_sales2024 
  GROUP BY product_name 
  ORDER BY total_sales DESC 
  LIMIT 5;"""
},
{
  "user_input": "Get the monthly Apple sales for 2024.",
  "sql": """SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS total_sales 
  FROM apple_sales2024 
  WHERE EXTRACT(YEAR FROM selling_date) = 2024 
  GROUP BY month 
  ORDER BY month;"""
},
{
  "user_input": "Find the month with lowest Samsung sales in 2024.",
  "sql": """SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS total_sales 
  FROM samsung_sales2024 
  WHERE EXTRACT(YEAR FROM selling_date) = 2024 
  GROUP BY month 
  ORDER BY total_sales ASC 
  LIMIT 1;"""
},
{
  "user_input": "Find Apple’s total profit in Chennai.",
  "sql": """SELECT SUM((selling_price - cost_price) * quantity) AS total_profit 
  FROM apple_sales2024 
  WHERE city = 'Chennai';"""
},
{
  "user_input": "Show Samsung’s average revenue per product.",
  "sql": """SELECT AVG(total_price) AS avg_revenue 
  FROM samsung_sales2024;"""
},
{
  "user_input": "Which Apple product generated the most revenue?",
  "sql": """SELECT product_name, SUM(total_price) AS total_revenue 
  FROM apple_sales2024 
  GROUP BY product_name 
  ORDER BY total_revenue DESC 
  LIMIT 1;"""
},
{
  "user_input": "Show Apple and Samsung total combined sales.",
  "sql": """SELECT 
    (SELECT SUM(total_price) FROM apple_sales2024) + 
    (SELECT SUM(total_price) FROM samsung_sales2024) AS total_combined_sales;"""
},
{
  "user_input": "Get Samsung sales per city sorted alphabetically.",
  "sql": """SELECT city, SUM(total_price) AS total_sales 
  FROM samsung_sales2024 
  GROUP BY city 
  ORDER BY city;"""
},
{
  "user_input": "Show all Apple transactions where quantity > 5.",
  "sql": """SELECT * FROM apple_sales2024 
  WHERE quantity > 5;"""
},
{
  "user_input": "Find total Apple products sold in each city.",
  "sql": """SELECT city, COUNT(DISTINCT product_id) AS total_products 
  FROM apple_sales2024 
  GROUP BY city;"""
},
{
  "user_input": "Which Samsung product had the highest average selling price?",
  "sql": """SELECT product_name, AVG(selling_price) AS avg_price 
  FROM samsung_sales2024 
  GROUP BY product_name 
  ORDER BY avg_price DESC 
  LIMIT 1;"""
},
{
  "user_input": "List Apple products sold on 1st January 2024.",
  "sql": """SELECT * FROM apple_sales2024 
  WHERE selling_date = '2024-01-01';"""
},
{
  "user_input": "Find total Samsung sales in Bangalore for the first quarter.",
  "sql": """SELECT SUM(total_price) AS total_sales 
  FROM samsung_sales2024 
  WHERE city = 'Bangalore' 
  AND EXTRACT(MONTH FROM selling_date) BETWEEN 1 AND 3;"""
},
{
  "user_input": "Which city had the least Apple sales?",
  "sql": """SELECT city, SUM(total_price) AS total_sales 
  FROM apple_sales2024 
  GROUP BY city 
  ORDER BY total_sales ASC 
  LIMIT 1;"""
},
{
  "user_input": "Find top 3 cities with highest Samsung quantity sold.",
  "sql": """SELECT city, SUM(quantity) AS total_quantity 
  FROM samsung_sales2024 
  GROUP BY city 
  ORDER BY total_quantity DESC 
  LIMIT 3;"""
},
{
  "user_input": "Show Apple sales grouped by product name.",
  "sql": """SELECT product_name, SUM(total_price) AS total_sales 
  FROM apple_sales2024 
  GROUP BY product_name;"""
},
{
  "user_input": "Calculate total Samsung profit across all cities.",
  "sql": """SELECT SUM((selling_price - cost_price) * quantity) AS total_profit 
  FROM samsung_sales2024;"""
},
{
  "user_input": "List all cities where both Apple and Samsung products were sold.",
  "sql": """SELECT DISTINCT a.city 
  FROM apple_sales2024 a 
  INNER JOIN samsung_sales2024 s 
  ON a.city = s.city;"""
},
{
  "user_input": "Find the ratio of Apple to Samsung total sales.",
  "sql": """SELECT 
    (SELECT SUM(total_price) FROM apple_sales2024)::FLOAT / 
    (SELECT SUM(total_price) FROM samsung_sales2024)::FLOAT AS sales_ratio;"""
},
{
  "user_input": "Which month saw the highest Apple sales in 2024?",
  "sql": """SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS total_sales 
  FROM apple_sales2024 
  WHERE EXTRACT(YEAR FROM selling_date) = 2024 
  GROUP BY month 
  ORDER BY total_sales DESC 
  LIMIT 1;"""
},
{
  "user_input": "Show Samsung’s total revenue in Pune.",
  "sql": """SELECT SUM(total_price) AS total_revenue 
  FROM samsung_sales2024 
  WHERE city = 'Pune';"""
},
{
  "user_input": "How many Apple items were sold in total?",
  "sql": """SELECT SUM(quantity) AS total_items 
  FROM apple_sales2024;"""
},
{
  "user_input": "Display all Samsung transactions for product Galaxy S24.",
  "sql": """SELECT * FROM samsung_sales2024 
  WHERE product_name = 'Galaxy S24';"""
},
{
  "user_input": "Get average quantity sold per city for Apple.",
  "sql": """SELECT city, AVG(quantity) AS avg_quantity 
  FROM apple_sales2024 
  GROUP BY city;"""
},
{
  "user_input": "Show top 10 Samsung sales by total price.",
  "sql": """SELECT * FROM samsung_sales2024 
  ORDER BY total_price DESC 
  LIMIT 10;"""
},
{
  "user_input": "Find Apple products sold in both Mumbai and Delhi.",
  "sql": """SELECT DISTINCT product_name 
  FROM apple_sales2024 
  WHERE city IN ('Mumbai', 'Delhi');"""
},
{
  "user_input": "Get Apple sales where cost price is greater than 10000.",
  "sql": """SELECT * FROM apple_sales2024 
  WHERE cost_price > 10000;"""
},
{
  "user_input": "Find the day with maximum Samsung sales.",
  "sql": """SELECT selling_date, SUM(total_price) AS total_sales 
  FROM samsung_sales2024 
  GROUP BY selling_date 
  ORDER BY total_sales DESC 
  LIMIT 1;"""
},
{
  "user_input": "What was Apple’s average selling price in Delhi?",
  "sql": """SELECT AVG(selling_price) AS avg_price 
  FROM apple_sales2024 
  WHERE city = 'Delhi';"""
},
{
  "user_input": "What are total Apple vs Samsung sales in 2024?",
  "sql": """SELECT
  (SELECT SUM(total_price) FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024) AS total_apple_sales,
  (SELECT SUM(total_price) FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024) AS total_samsung_sales;"""
},
{
  "user_input": "Compare total monthly Apple and Samsung sales for 2024.",
  "sql": """SELECT
  COALESCE(a.month, s.month) AS month,
  a.apple_sales,
  s.samsung_sales
  FROM
  (SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS apple_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY month) a
  FULL OUTER JOIN
  (SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY month) s
  ON a.month = s.month
  ORDER BY month;"""
},
{
  "user_input": "Which brand made more total sales in 2024?",
  "sql": """SELECT
  CASE
  WHEN apple_sales > samsung_sales THEN 'Apple'
  WHEN samsung_sales > apple_sales THEN 'Samsung'
  ELSE 'Equal'
  END AS top_brand,
  apple_sales,
  samsung_sales
  FROM (
  SELECT
  (SELECT SUM(total_price) FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024) AS apple_sales,
  (SELECT SUM(total_price) FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024) AS samsung_sales
  ) t;"""
},
{
  "user_input": "Show total Apple and Samsung sales by city for 2024.",
  "sql": """SELECT
  COALESCE(a.city, s.city) AS city,
  a.apple_sales,
  s.samsung_sales
  FROM
  (SELECT city, SUM(total_price) AS apple_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) a
  FULL OUTER JOIN
  (SELECT city, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) s
  ON a.city = s.city
  ORDER BY city;"""
},
{
  "user_input": "Which city had higher Apple sales compared to Samsung in 2024?",
  "sql": """SELECT
  COALESCE(a.city, s.city) AS city,
  a.apple_sales,
  s.samsung_sales
  FROM
  (SELECT city, SUM(total_price) AS apple_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) a
  FULL OUTER JOIN
  (SELECT city, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) s
  ON a.city = s.city
  WHERE a.apple_sales > COALESCE(s.samsung_sales, 0)
  ORDER BY a.apple_sales DESC;"""
},
{
  "user_input": "Find month-wise difference in sales of Apple and Samsung in 2024.",
  "sql": """SELECT
  COALESCE(a.month, s.month) AS month,
  COALESCE(a.apple_sales, 0) - COALESCE(s.samsung_sales, 0) AS sales_difference
  FROM
  (SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS apple_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY month) a
  FULL OUTER JOIN
  (SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY month) s
  ON a.month = s.month
  ORDER BY month;"""
},
{
  "user_input": "Get Apple and Samsung combined monthly sales for 2024.",
  "sql": """SELECT
  COALESCE(a.month, s.month) AS month,
  COALESCE(a.apple_sales, 0) + COALESCE(s.samsung_sales, 0) AS total_sales
  FROM
  (SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS apple_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY month) a
  FULL OUTER JOIN
  (SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY month) s
  ON a.month = s.month
  ORDER BY month;"""
},
{
  "user_input": "Calculate the percentage share of Apple and Samsung sales in 2024.",
  "sql": """WITH totals AS (
  SELECT
  (SELECT SUM(total_price) FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024) AS apple_sales,
  (SELECT SUM(total_price) FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024) AS samsung_sales
  )
  SELECT
  apple_sales,
  samsung_sales,
  ROUND(apple_sales * 100.0 / (apple_sales + samsung_sales), 2) AS apple_share_percent,
  ROUND(samsung_sales * 100.0 / (apple_sales + samsung_sales), 2) AS samsung_share_percent
  FROM totals;"""
},
{
  "user_input": "Compare quarterly Apple and Samsung sales for 2024.",
  "sql": """SELECT
  COALESCE(a.quarter, s.quarter) AS quarter,
  a.apple_sales,
  s.samsung_sales
  FROM
  (SELECT CEIL(EXTRACT(MONTH FROM selling_date)/3.0) AS quarter, SUM(total_price) AS apple_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY quarter) a
  FULL OUTER JOIN
  (SELECT CEIL(EXTRACT(MONTH FROM selling_date)/3.0) AS quarter, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY quarter) s
  ON a.quarter = s.quarter
  ORDER BY quarter;"""
},
{
  "user_input": "Find total Apple and Samsung sales combined by city in 2024.",
  "sql": """SELECT city, SUM(total_price) AS combined_sales
  FROM (
  SELECT city, total_price FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
  UNION ALL
  SELECT city, total_price FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
  ) all_sales
  GROUP BY city
  ORDER BY combined_sales DESC;"""
},
{
  "user_input": "Plot a graph of month-wise Apple vs Samsung sales in 2024.",
  "sql": """WITH apple AS (
  SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS apple_sales
  FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024 GROUP BY month
  ),
  samsung AS (
    SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS samsung_sales
    FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024 GROUP BY month
  )
  SELECT COALESCE(a.month, s.month) AS month, a.apple_sales, s.samsung_sales
  FROM apple a FULL OUTER JOIN samsung s ON a.month = s.month ORDER BY month"""
},
{
  "user_input": "What is Apple vs Samsung's month-wise sales in 2024?",
  "sql": """SELECT
  COALESCE(a.month, s.month) AS month,
  SUM(a.total_price) AS total_apple_sales,
  SUM(s.total_price) AS total_samsung_sales
  FROM
  (SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS total_price
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY month) a
  FULL OUTER JOIN
  (SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS total_price
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY month) s
  ON a.month = s.month
  GROUP BY a.month, s.month"""
},
{
  "user_input": "Which city had the most Apple sales in 2024?",
  "sql": """SELECT city, SUM(total_price) AS apple_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city
  ORDER BY apple_sales DESC
  LIMIT 1;"""
},
{
  "user_input": "Which city had the highest Samsung sales in 2024?",
  "sql": """SELECT city, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city
  ORDER BY samsung_sales DESC
  LIMIT 1;"""
},
{
  "user_input": "List top 5 cities with highest Apple sales in 2024.",
  "sql": """SELECT city, SUM(total_price) AS total_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city
  ORDER BY total_sales DESC
  LIMIT 5;"""
},
{
  "user_input": "List top 5 cities with highest Samsung sales in 2024.",
  "sql": """SELECT city, SUM(total_price) AS total_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city
  ORDER BY total_sales DESC
  LIMIT 5;"""
},
{
  "user_input": "Plot a pie chart of month-wise Apple sales in 2024.",
  "sql": """SELECT EXTRACT(MONTH FROM selling_date) AS month, SUM(total_price) AS apple_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY month
  ORDER BY month"""
},
{
  "user_input": "Plot a graph of total Apple vs Samsung sales in 2024.",
  "sql": """SELECT
  (SELECT SUM(total_price) FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024) AS total_apple_sales,
  (SELECT SUM(total_price) FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024) AS total_samsung_sales"""
},
{
  "user_input": "Which city had higher Apple sales compared to Samsung in 2024?",
  "sql": """SELECT
  COALESCE(a.city, s.city) AS city,
  a.apple_sales,
  s.samsung_sales
  FROM
  (SELECT city, SUM(total_price) AS apple_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) a
  FULL OUTER JOIN
  (SELECT city, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) s
  ON a.city = s.city
  WHERE a.apple_sales > COALESCE(s.samsung_sales, 0)
  ORDER BY a.apple_sales DESC;"""
},
{
  "user_input": "Which city had higher Samsung sales compared to Apple in 2024?",
  "sql": """SELECT
  COALESCE(a.city, s.city) AS city,
  a.apple_sales,
  s.samsung_sales
  FROM
  (SELECT city, SUM(total_price) AS apple_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) a
  FULL OUTER JOIN
  (SELECT city, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) s
  ON a.city = s.city
  WHERE s.samsung_sales > COALESCE(a.apple_sales, 0)
  ORDER BY s.samsung_sales DESC;"""
},
{
  "user_input": "Show top 3 cities where Apple outsold Samsung in 2024.",
  "sql": """SELECT
  COALESCE(a.city, s.city) AS city,
  a.apple_sales,
  s.samsung_sales,
  (a.apple_sales - COALESCE(s.samsung_sales, 0)) AS sales_difference
  FROM
  (SELECT city, SUM(total_price) AS apple_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) a
  FULL OUTER JOIN
  (SELECT city, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) s
  ON a.city = s.city
  WHERE a.apple_sales > COALESCE(s.samsung_sales, 0)
  ORDER BY sales_difference DESC
  LIMIT 3;"""
},
{
  "user_input": "Which city recorded the smallest Apple sales in 2024?",
  "sql": """SELECT city, SUM(total_price) AS apple_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city
  ORDER BY apple_sales ASC
  LIMIT 1;"""
},
{
  "user_input": "Which city recorded the smallest Samsung sales in 2024?",
  "sql": """SELECT city, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city
  ORDER BY samsung_sales ASC
  LIMIT 1;"""
},
{
  "user_input": "Show total Apple and Samsung sales combined per city in 2024.",
  "sql": """SELECT city, SUM(total_price) AS total_sales
  FROM (
  SELECT city, total_price FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
  UNION ALL
  SELECT city, total_price FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
  ) combined
  GROUP BY city
  ORDER BY total_sales DESC;"""
},
{
  "user_input": "Find city-wise profit comparison between Apple and Samsung in 2024.",
  "sql": """SELECT
  COALESCE(a.city, s.city) AS city,
  a.apple_profit,
  s.samsung_profit
  FROM
  (SELECT city, SUM(selling_price - cost_price) AS apple_profit
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) a
  FULL OUTER JOIN
  (SELECT city, SUM(selling_price - cost_price) AS samsung_profit
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) s
  ON a.city = s.city
  ORDER BY city;"""
},
{
  "user_input": "Show Apple and Samsung sales difference by city for 2024.",
  "sql": """SELECT
  COALESCE(a.city, s.city) AS city,
  COALESCE(a.apple_sales, 0) - COALESCE(s.samsung_sales, 0) AS sales_difference
  FROM
  (SELECT city, SUM(total_price) AS apple_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) a
  FULL OUTER JOIN
  (SELECT city, SUM(total_price) AS samsung_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city) s
  ON a.city = s.city
  ORDER BY sales_difference DESC;"""
},
{
  "user_input": "Find the average Apple sales per city in 2024.",
  "sql": """SELECT city, AVG(total_price) AS avg_sales
  FROM apple_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city
  ORDER BY avg_sales DESC;"""
},
{
  "user_input": "Find the average Samsung sales per city in 2024.",
  "sql": """SELECT city, AVG(total_price) AS avg_sales
  FROM samsung_sales2024
  WHERE EXTRACT(YEAR FROM selling_date) = 2024
  GROUP BY city
  ORDER BY avg_sales DESC;"""
},
{
  "user_input": "Compare Apple and Samsung sales percentage share in each city for 2024.",
  "sql": """WITH totals AS (
  SELECT city,
  SUM(CASE WHEN brand = 'Apple' THEN total_price ELSE 0 END) AS apple_sales,
  SUM(CASE WHEN brand = 'Samsung' THEN total_price ELSE 0 END) AS samsung_sales
  FROM (
  SELECT 'Apple' AS brand, city, total_price FROM apple_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
  UNION ALL
  SELECT 'Samsung' AS brand, city, total_price FROM samsung_sales2024 WHERE EXTRACT(YEAR FROM selling_date) = 2024
  ) all_sales
  GROUP BY city
  )
  SELECT city,
  apple_sales,
  samsung_sales,
  ROUND(apple_sales * 100.0 / (apple_sales + samsung_sales), 2) AS apple_percent,
  ROUND(samsung_sales * 100.0 / (apple_sales + samsung_sales), 2) AS samsung_percent
  FROM totals
  ORDER BY city;"""
}
]
