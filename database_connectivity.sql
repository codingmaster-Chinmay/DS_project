show databases;
create database mydb;
use mydb;
create table salaryinfo(empid int primary key not null,
empname varchar(45) not null,
empsalary int not null,
emp_mob dec(10) not null
);
show tables;
desc salaryinfo;
insert into salaryinfo values(11,'kunal',23000,8888976579),
(12,'vikas',42000,6279237698),
(13,'deepika',120000,8763528908),
(14,'ankanksha',87000,6736289856),
(15,'ruchir',230000,6527386789);
select*from salaryinfo;