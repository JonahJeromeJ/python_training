-- create table user12(
-- id int not null,
-- name varchar(50),
-- email varchar(50),
-- password varchar(50),
-- primary key(id))

-- ALTER TABLE user12
-- ADD countrty varchar(50);
 -- insert into user12(id,name,email,password,countrty)values
--  (2,"qwert","qwert@gmail.com","6565656","bgl"),
--  (21,"qwert2","qwert2@gmail.com","65656565","rlf"),
--  (42,"qwert3","qwert3@gmail.com","45656565","tyggg"),
--  (213,"qwert7","qwer7t@gmail.com","6565656565","ttdtdtu")
-- select * from user

-- create table city1(
-- id int not null,
-- name varchar(50),
-- country varchar(50),
-- primary key(id))


-- TRUNCATE TABLE city;


-- insert into city1 (id,name,country)values(1,"qwert","bgl"),(2,"qwert2","rlf"),(3,"qwert3","tyggg"),(4,"qwert7","ttdtdtu"),(4,"qwert2727","tt22dtdtu")
--  TRUNCATE TABLE city1;
--   insert into city1 (id,name,country)values(1,"mumbai","india"),(2,"pune","usa"),(3,"wall street","uk"),(4,"agatha","chile")
-- ALTER TABLE user12
-- DROP COLUMN password;

-- create table city2(
-- id int not null,
-- name varchar(50),
-- email varchar(50),
-- city_id varchar(50),
-- primary key(id))




-- insert into city2 (id,name,email)values(1,"test1","qwerty@gmail.com"),(2,"test2","qwerty2@gmail.com"),(3,"test3","qwerty3@gmail.com"),(4,"test4","qwerty4@gmail.com")
-- select * from city2 join city1 on city2.city_id= city1.id where city1.id=3

-- create table user12(
-- id int not null,
-- name varchar(50),
-- email varchar(50),
-- password varchar(50),
-- primary key(id))

-- ALTER TABLE user12
-- ADD countrty varchar(50);
 -- insert into user12(id,name,email,password,countrty)values
--  (2,"qwert","qwert@gmail.com","6565656","bgl"),
--  (21,"qwert2","qwert2@gmail.com","65656565","rlf"),
--  (42,"qwert3","qwert3@gmail.com","45656565","tyggg"),
--  (213,"qwert7","qwer7t@gmail.com","6565656565","ttdtdtu")
-- select * from user

-- create table city1(
-- id int not null,
-- name varchar(50),
-- country varchar(50),
-- primary key(id))


-- TRUNCATE TABLE city;


-- insert into city1 (id,name,country)values(1,"qwert","bgl"),(2,"qwert2","rlf"),(3,"qwert3","tyggg"),(4,"qwert7","ttdtdtu"),(4,"qwert2727","tt22dtdtu")
--  TRUNCATE TABLE city1;
--   insert into city1 (id,name,country)values(1,"mumbai","india"),(2,"pune","usa"),(3,"wall street","uk"),(4,"agatha","chile")
-- ALTER TABLE user12
-- DROP COLUMN password;

-- create table city2(
-- id int not null,
-- name varchar(50),
-- email varchar(50),
-- city_id varchar(50),
-- primary key(id))






-- insert into city2 (id,name,email)values(1,"test1","qwerty@gmail.com"),(2,"test2","qwerty2@gmail.com"),(3,"test3","qwerty3@gmail.com"),(4,"test4","qwerty4@gmail.com")
-- select * from city2  join city1 on city2.city_id= city1.id 


-- ALTER TABLE city2
-- ADD city_id varchar(50)




-- ALTER TABLE city2
-- ADD PRIMARY KEY (city_id);

-- ALTER TABLE city2
-- DROP PRIMARY KEY


-- ALTER TABLE city2
-- ADD PRIMARY KEY (city_id);

-- select * from city2 
-- update city2 set id= 6 where city_id= '6'
-- delete from city2 where city_id= '6'