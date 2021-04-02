DROP DATABASE IF EXISTS fb_prep;
CREATE DATABASE fb_prep;

DROP TABLE IF EXISTS fb_prep.salesperson;
CREATE TABLE IF NOT EXISTS fb_prep.salesperson
(id INT PRIMARY KEY, 
 name varchar(200),
 age INT,
 salary float);


DROP TABLE IF EXISTS fb_prep.customer;
CREATE TABLE IF NOT EXISTS fb_prep.customer
(id INT PRIMARY KEY, 
 name VARCHAR(200),
 city VARCHAR(200),
 industry_type VARCHAR(1));

DROP TABLE IF EXISTS fb_prep.orders;
CREATE TABLE IF NOT EXISTS fb_prep.orders
(number INT PRIMARY KEY, 
 order_date date,
 cust_id int,
 salesperson_id int,
 amount float);
 
 
 INSERT INTO fb_prep.salesperson(id,name,age,salary) VALUES(1, 'Abe',61,140000);
 INSERT INTO fb_prep.salesperson(id,name,age,salary) VALUES(2, 'Bob',34,44000);
 INSERT INTO fb_prep.salesperson(id,name,age,salary) VALUES(5, 'Chris',34,40000);
 INSERT INTO fb_prep.salesperson(id,name,age,salary) VALUES(7, 'Dan',41,52000);
 INSERT INTO fb_prep.salesperson(id,name,age,salary) VALUES(8, 'Kan',57,115000);
 INSERT INTO fb_prep.salesperson(id,name,age,salary) VALUES(11,'Joe',38,38000);
 
 INSERT INTO fb_prep.customer(id,name,city, industry_type) VALUES(4,'Samsonic','pleasant','J');
 INSERT INTO fb_prep.customer(id,name,city, industry_type) VALUES(5,'Panasonic','oaktown','J');
 INSERT INTO fb_prep.customer(id,name,city, industry_type) VALUES(7,'Samony','jackson','B');
 INSERT INTO fb_prep.customer(id,name,city, industry_type) VALUES(9,'Orange','Jackson','B');
 
 INSERT INTO fb_prep.orders(number,order_date,cust_id,salesperson_id,amount) VALUES(10,'1996-08-02',4,2,540);
 INSERT INTO fb_prep.orders(number,order_date,cust_id,salesperson_id,amount) VALUES(20,'1999-01-30',4,8,1800);
 INSERT INTO fb_prep.orders(number,order_date,cust_id,salesperson_id,amount) VALUES(30,'1995-07-14',9,1,460);
 INSERT INTO fb_prep.orders(number,order_date,cust_id,salesperson_id,amount) VALUES(40,'1998-01-29',7,2,2400);
 INSERT INTO fb_prep.orders(number,order_date,cust_id,salesperson_id,amount) VALUES(50,'1998-02-03',6,7,600);
 INSERT INTO fb_prep.orders(number,order_date,cust_id,salesperson_id,amount) VALUES(60,'1998-03-02',6,7,720);
 INSERT INTO fb_prep.orders(number,order_date,cust_id,salesperson_id,amount) VALUES(70,'1998-05-06',9,7,150);

 COMMIT;