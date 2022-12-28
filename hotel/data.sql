create database hotel;
use hotel;

create table customer_data(customer_name varchar(20), address varchar (30), in_date varchar(10), out_date varchar(10));
create table roomtype (s_no varchar(5), roomtype varchar(10), rent smallint);
insert into roomtype values ('1','type A',1000);
insert into roomtype values ('2','type B',2000);
insert into roomtype values ('3','type C',3000);
insert into roomtype values ('4','type D',4000);

create table restaurant (s_no tinyint,item_name varchar(10),rate tinyint);
insert into restaurant values(1,"tea",10);
insert into restaurant values(2,"coffee",10);
insert into restaurant values(3,"colddrink",20);
insert into restaurant values(4,"samosa",10);
insert into restaurant values(5,"sandwich",50);
insert into restaurant values(6,"Dhokla",30);
insert into restaurant values(7,"kachori",10);
insert into restaurant values(8,"milk",20);
insert into restaurant values(9,"noodles",50);
insert into restaurant values(10,"pasta",50);

create table laundary(s_no tinyint,item_name varchar(10),rate smallint);
insert into laundary values(1,"pant",10);
insert into laundary values(2,"shirt",10);
insert into laundary values(3,"suit",10);
insert into laundary values(4,"sari",10);

