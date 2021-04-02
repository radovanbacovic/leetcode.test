--------------------------------------------------------------------------------------------------------
-- a. The names of all salespeople that have an order with Samsonic. 
--------------------------------------------------------------------------------------------------------

SELECT DISTINCT s.name
  FROM fb_prep.salesperson  s
  LEFT JOIN fb_prep.orders  o
    ON s.id      = o.salesperson_id
  LEFT JOIN fb_prep.customer c
    ON o.cust_id = c.id
  WHERE c.name   = 'Samsonic';
  
--------------------------------------------------------------------------------------------------------
-- b. The names of all salespeople that do not have any order with Samsonic. 
--------------------------------------------------------------------------------------------------------
SELECT *
  FROM fb_prep.salesperson  s
  WHERE NOT EXISTS (SELECT 1
                      FROM fb_prep.orders  o
                      LEFT JOIN fb_prep.customer c
                        ON o.cust_id = c.id
                     WHERE c.name = 'Samsonic'
                       AND s.id = o.salesperson_id);


--------------------------------------------------------------------------------------------------------
-- c. The names of salespeople that have 2 or more orders. 
--------------------------------------------------------------------------------------------------------
SELECT s.name,
       COUNT(1)
  FROM fb_prep.salesperson  s
  LEFT JOIN fb_prep.orders o
    ON s.id = o.salesperson_id
 GROUP BY s.name
 HAVING COUNT(1) >= 2;

--------------------------------------------------------------------------------------------------------
-- d. The names and ages of all salespersons must having a salary of 100,000 or greater.
--------------------------------------------------------------------------------------------------------

SELECT s.name,
       s.age
  FROM fb_prep.salesperson  s
 WHERE s.salary >= 100000;
 
  
--------------------------------------------------------------------------------------------------------
-- e. What sales people have sold more than 1400 total units?
--------------------------------------------------------------------------------------------------------

SELECT s.name,
       SUM(IFNULL(o.amount,0))
  FROM fb_prep.salesperson s
  LEFT JOIN fb_prep.orders o
    ON s.id = o.salesperson_id
  GROUP BY s.name
  HAVING SUM(IFNULL(o.amount,0)) > 1400;

--------------------------------------------------------------------------------------------------------
-- f. When was the earliest and latest order made to Samony?
--------------------------------------------------------------------------------------------------------

SELECT MIN(order_date),
       MAX(order_date) 
  FROM customer c
  LEFT JOIN orders o
    ON c.id = o.cust_id 
 WHERE c.name= 'Samony';