
SELECT *
FROM students;

SELECT name,score
FROM students;

SELECT *
FROM students
WHERE score>80;

SELECT *
FROM students
WHERE score>80 AND passed=TRUE;

SELECT *
FROM students
WHERE score>80 AND class=9;

SELECT name
FROM students
WHERE  passed=FALSE;

SELECT DISTINCT class
FROM students;

SELECT *
FROM students
ORDER BY score DESC
LIMIT 5;

SELECT *
FROM students
ORDER BY class ASC,score DESC;

SELECT name,score as Final_score
FROM students;

SELECT name,score
FROM students
WHERE score>75
ORDER BY score DESC
LIMIT 3;

