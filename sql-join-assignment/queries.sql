-- CREATE TABLE users(
--     user_id INTEGER PRIMARY KEY,
--     name text,
--     signup_date DATE
-- );
-- CREATE TABLE orders(
--     order_id INTEGER PRIMARY KEY,
--     user_id INTEGER,
--     amount INTEGER
-- );
-- CREATE TABLE activity(
--     user_id INTEGER,
--     login_count INTEGER
-- );
-- INSERT into users(user_id,name,signup_date) VALUES
-- (1,'Aarav','2023-01-10'),
-- (2,'Diya','2023-02-14'),
-- (3,'Rohan','2023-03-01'),
-- (4,'Meera','2023-04-11'),
-- (5,'Kabir','2023-05-06');

-- INSERT into orders(order_id,user_id,amount) VALUES
-- (101,1,500),
-- (102,1,700),
-- (103,2,300),
-- (104,4,900),
-- (105,4,400);

-- INSERT into activity(user_id,login_count) VALUES
-- (1,25),
-- (2,10),
-- (3,5),
-- (5,12);

SELECT users.name,orders.amount 
FROM users 
INNER JOIN orders ON users.user_id=orders.user_id;

SELECT users.name, sum(orders.amount) as Total_sum
FROM users 
INNER JOIN orders ON users.user_id=orders.user_id
GROUP BY users.user_id, users.name;

SELECT users.name, activity.login_count
FROM users
LEFT JOIN activity ON users.user_id=activity.user_id;

SELECT users.user_id,users.name,orders.amount
FROM users 
LEFT JOIN orders ON users.user_id=orders.user_id
WHERE orders.amount IS NULL;

SELECT users.user_id,users.name, sum(orders.amount) as sum_total_amount,activity.login_count
FROM users 
LEFT JOIN orders ON users.user_id=orders.user_id
LEFT JOIN activity ON users.user_id=activity.user_id
GROUP BY users.name;

SELECT users.user_id,users.name,orders.amount
FROM users 
LEFT JOIN orders ON users.user_id=orders.user_id
WHERE orders.amount >400;

SELECT users.user_id,sum(orders.amount) as total_sum,users.name
FROM users 
LEFT JOIN orders ON users.user_id=orders.user_id
GROUP BY users.name
ORDER BY total_sum DESC
LIMIT 3;

SELECT users.user_id,users.name,sum(orders.amount) as sum_total_amount,activity.login_count
FROM users 
LEFT JOIN orders ON users.user_id=orders.user_id
LEFT JOIN activity ON users.user_id=activity.user_id
GROUP BY users.name
ORDER BY sum_total_amount DESC, activity.login_count DESC;

SELECT users.user_id,users.name,avg(orders.amount) as average_order_amount
FROM users 
LEFT JOIN orders ON users.user_id=orders.user_id
GROUP BY users.name;

SELECT users.user_id,users.name,sum(orders.amount) as sum_total_amount,activity.login_count
FROM users 
LEFT JOIN orders ON users.user_id=orders.user_id
LEFT JOIN activity ON users.user_id=activity.user_id
GROUP BY users.name
ORDER BY sum_total_amount DESC
LIMIT 3;