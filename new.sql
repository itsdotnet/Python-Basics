-- users uchun commandalar vazifa sifatida
-- 1 
select * from users where gender='Male'
-- 2 
select * from users having length(first_name)+length(last_name)>10;
-- 3
select * from users where first_name like "%a%";
-- 4
select * from users where gender='Male' limit 10;
-- 5
select (select count(gender) from users where gender = 'Female') as ayol_userlar_soni;