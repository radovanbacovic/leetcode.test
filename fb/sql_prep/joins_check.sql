SELECT *
  FROM department;
  
SELECT *
  FROM employee;
  
  

SELECT d.departmentname, count(e.lastname)
  FROM employee e
  LEFT JOIN department d
 on e.departmentid = d.departmentid
 GROUP BY d.departmentname;
 

SELECT count(1),
       count(departmentid),
       count(distinct departmentid)
  FROM employee;  
  
SELECT AVG(departmentid),SUM(Departmentid)/count(1),avg(distinct departmentid)
  FROM employee
  ORDER BY DepartmentID IS NULL DESC;    