SELECT product , SUM(quantity) Total_quantity
from ACME_data_SQL
GROUP BY product;

SELECT 
CASE
when age < 18 then 'Under 18'
when age between 18 and 24 then '18-24'
when age between 25 and 40 then '25-40'
when age between 40 and 60 then '40-60'
when age > 60 then 'Over 60'
END AS age_group,
SUM(quantity) Total_quantity
from ACME_data_SQL
WHERE product = 'toys'
GROUP BY age_group
ORDER BY Total_quantity;

SELECT 
CASE
when age < 18 then 'Under 18'
when age between 18 and 24 then '18-24'
when age between 25 and 40 then '25-40'
when age between 40 and 60 then '40-60'
when age > 60 then 'Over 60'
END AS age_group,
SUM(quantity) Total_quantity
from ACME_data_SQL
WHERE product = 'toothbrush'
GROUP BY age_group
ORDER BY Total_quantity;

SELECT uk_region, SUM(quantity) Total_quantity
from ACME_data_SQL WHERE product = 'toys'
GROUP BY uk_region;

SELECT uk_region, SUM(quantity) Total_quantity
from ACME_data_SQL WHERE product = 'toothbrush'
GROUP BY uk_region;

SELECT 
CASE
when month in ('Mar', 'Apr', 'May') then 'Spring'
when month in ('Jun', 'Jul', 'Aug') then 'Summer'
when month in ('Sep', 'Oct', 'Nov') then 'Autumn'
when month in ('Dec', 'Jan', 'Feb') then 'Winter'
END AS season,
SUM(quantity) Total_quantity
from ACME_data_SQL
WHERE product = 'toothbrush'
GROUP BY season
ORDER BY Total_quantity;

SELECT 
CASE
when month in ('Mar', 'Apr', 'May') then 'Spring'
when month in ('Jun', 'Jul', 'Aug') then 'Summer'
when month in ('Sep', 'Oct', 'Nov') then 'Autumn'
when month in ('Dec', 'Jan', 'Feb') then 'Winter'
END AS season,
SUM(quantity) Total_quantity
from ACME_data_SQL
WHERE product = 'toys'
GROUP BY season
ORDER BY Total_quantity;
