create database engineer_data;

use engineer_data;

select * from dbo.agents;
select * from dbo.calls;
select * from dbo.customers;

--EXERCISE NUMER 1: extract agents from database whose name starts with M or ends with O
select name from dbo.agents
where name like 'M%' OR name like '%o';

--EXERCISE NUMER 2: write a query that produces a list, in alphabetical order, of all the different occupations
-- in the customer table that contain the word Engineer.
select * from dbo.customers
where occupation = '"Engineer'
order by name ASC;

select distinct occupation from dbo.customers
where occupation LIKE '%Engineer%'
order by occupation;
 
--EXERCISE NUMBER 3:
select customerid, name,
case
	when Age >= '30' then 'Yes'
	when Age <= '30' then 'No'
	else  'Missing Data'
end as Over30
from customers
order by name ASC;

--EXERCISE NUMBER 4:
select calls.callid, customers.customerid, customers.name, calls.productsold,
case
	when Age >= '30' then 'Yes'
	when Age <= '30' then 'No'
	else  'Missing Data'
end as Over30
from customers
join calls on calls.customerid = customers.customerid
where occupation like '%Engineer%'
order by name ASC;


--EXERCISE NUMBER 5:
--1) calcular las ventas totales y las llamadas totales realizadas a los clientes de la profesion de ingeniería
select COUNT(calls.pickedup) as LlamadasTotales , sum(calls.productsold) as VentasTotales, customers.occupation
from calls
join customers on customers.customerid = calls.customerid
where occupation like '%Engineer%' and productsold = 1;

SELECT SUM(productsold) AS 'VENTAS', COUNT(*) AS Ncalls
from customers Cu
join calls Ca ON Ca.customerid = Cu.customerid
where occupation like '%Engineer%'

--2) calcular la misma metricas para toda la base de clientes
SELECT SUM(productsold) AS 'VENTAS', COUNT(*) AS Ncalls
from customers Cu
join calls Ca ON Ca.customerid = Cu.customerid
where occupation not like '%Engineer%'

--EXERCISE NUMBER 6:
select agents.name as AgentName, count(calls.agentid) as Ncalls, max(calls.duration) as Longest, min(calls.duration) as Shortest,
round(avg(calls.duration),2) as AvgDuration, count(calls.productsold) as TotalSales
from calls
join agents on calls.agentid = agents.agentid
where calls.pickedup = 1
group by agents.name
order by agents.name ASC;

--EXERCISE NUMBER 7:
--Escribir una consulta que extraiga dos métricas del desempeño de los agentes de ventas que le interesan a su empresa: 
--1)Para cada agente, cuántos segundos en promedio les toma vender un producto cuando tienen éxito.
--2)Para cada agente, cuántos segundos en promedio permanecen en el teléfono antes de darse por vencidos cuando no tienen éxito.

SELECT a.name, 
  	SUM( CASE
			WHEN productsold = 0 THEN duration
			ELSE 0
		END)/SUM(
		CASE
			WHEN productsold = 0 THEN 1
			ELSE 0
		END)
 AS avgWhenNotSold,
 	SUM(
		CASE 
			WHEN productsold = 1 THEN duration
			ELSE 0
		END)/SUM(
			CASE WHEN productsold = 1 THEN 1
			ELSE 0
		END)
 AS avgWhenSold
FROM calls c
JOIN agents a ON c.agentid = a.agentid
GROUP BY a.name
ORDER BY 1;