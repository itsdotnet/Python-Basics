--  najot talim database
create database najot_talim;
-- use 
use najot_talim
-- users columns 
create table users(id serial,name varchar(25),surname varchar(20),age tinyint,username text,password text,gender varchar (20));
-- inserting
insert into users values(null,"Gulchapchap","Eshmatova",16,"lampada","parol","F");
insert into users values(null,"G'ishmat","Norinov",14,"bigbitn","ollika45","M");
insert into users values(null,"Tesha","Wakhidow",23,"user456312","user456312","M");
insert into users values(null,"Abror","Wakhidow",15,"newone","password","M");
insert into users values(null,"Gulnoza","Olmayeva",21,"tin_pin","old_pass","F");
insert into users values(null,"Aziza","Posva",18,"pypone","osmanko","F");
insert into users values(null,"Kolim","Polizov",14,"pospone","15op01Q","M");
insert into users values(null,"Gulchapchap","Eshmatova",16,"lampada","parol","F");
insert into users values(null,"G'ishmat","Norinov",14,"bigbitn","ollika45","M");
insert into users values(null,"Tesha","Wakhidow",23,"user456312","user456312","M");
insert into users values(null,"Abror","Wakhidow",15,"newone","password","M");
insert into users values(null,"Gulnoza","Olmayeva",21,"tin_pin","old_pass","F");
insert into users values(null,"Aziza","Posva",18,"pypone","osmanko","F");
insert into users values(null,"Kolim","Polizov",14,"pospone","15op01Q","M");
insert into users values(null,"Kozim","Poli",31,"pospone","15op01Q","M");
insert into users values(null,"Azizasa","Podsava",32,"qwerty","osmans464d","F");
insert into users values(null,"Azza","Podsakov",12,"qwerty","ospolno","F");
insert into users values(null,"Ali","Pakov",17,"qwerty","ospolno","M");
insert into users values(null,"Zaza","Lakov",17,"qyposy","opda35olno","M");
-- solution starts here
-- 1
select * from users where age > 15 and age < 30;
-- 2
select (select count(*) from users where age = 17) as soni;
-- 3
select * from users where name like "A%";
-- 4
select * from users where gender = "F";
-- 5
select * from users where name = "Gulnoza" or name = "Abror" or name = "Ali";
-- 6
delete from users where gender = 'F';
-- 7
select * from users having age = (select max(age) from users);
-- 8
update users set password = 'qwer1234' where name = "Abror" or name = "Gulnoza";

