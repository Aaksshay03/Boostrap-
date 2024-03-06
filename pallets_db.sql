create database project1;
use project1;
create table  pallets(
sno int primary key,
Date_ varchar (20),
CustName varchar(5),
City varchar(40),
Region varchar(40),
State varchar(40),
Product_Code varchar (40),
Transcation_Type varchar(40),
Qty int,
WHName int);
select *  from pallets;

load data infile 'C:/Program Files/MySQL/MySQL Server 8.0/Uploads/pallet_Masked_fulldata.csv'
into table pallets
fields terminated by ","
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;
select *  from pallets;


#mean
select avg(Qty) as mean_Qty from pallets;

#meadian
select QTY as median_QTY
from(
select QTY ,
row_number() over(order by QTY)  as row_num,
count(*) over() as total_count
from pallets
)as subquery 
 where row_num = (total_count +1)/2 or row_num = (total_count +2)/2;
# mode
select QTY as mode_QTY
from pallets
group by QTY
having count(QTY) = (
select max(QTYcount)
from(
select QTY, count(QTY) as QTYcount
from pallets
group by QTY 
)as subquery
);


#SECOND MOMENT OF BUSINESS DECISION

# standard deviation

select stddev(QTY) as QTY_stddev
from pallets;

# range

select max(QTY) - min(QTY) as
 QTY_ramge
 from pallets;
 
 
 # variance
 
 select variance(QTY)  as
 QTY_variance
 from pallets;
 
 # Third moment of business decision
 
 #skewness
 
 select
 (
 sum(power(QTY-(select avg(QTY) from pallets),3))/
 (count(*)*power((select stddev(QTY) from pallets),3))
 ) as skewness
 from pallets;
 
 # four momentof business decision
 
 # kurtosis
 
 select
 (
 (sum(power(QTY-(select avg(QTY) from pallets),4))/
 (count(*)* power((select stddev(QTY) from pallets),4))) - 3
 ) as kurtosis
 from pallets;
 
 
 
 