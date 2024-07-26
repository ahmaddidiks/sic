## SQL Query

``` sql

-- SQL playground : https://sqliteonline.com/



-- JALANKAN SCRIPT DALAM KOTAK TERLEBIH DAHULU UNTUK MEMBUAT TABLE DAN DATANTA      
------------------------------------------------------------------------------------------------
-- buat table
CREATE TABLE IF NOT EXISTS student_grades (
  exam_result_id INTEGER PRIMARY KEY,
  name VARCHAR(50),
  subject VARCHAR(50),
  score INT,
  exam_date VARCHAR(50) 
);

-- isi data ke table
insert into student_grades values(111,'Alice','Physics', 9, '2 February 2020');
insert into student_grades values(112,'Alice','Math', 8, '3 March 2020');
insert into student_grades values(113,'Alice','CS', 6, '1 January 2020');
insert into student_grades values(114,'Bob','Geograpgy', 5, '2 February 2020');
insert into student_grades values(115,'Bob','Physics', 7, '1 January 2020');
insert into student_grades values(116,'Charles','Physics', NULL, '1 August 2020');
------------------------------------------------------------------------------------------------

-- JALANKAN SCRIPT DIBAWHA SATU PER SATU

-- select score
SELECT score FROM student_grades

-- SELECT can rename and reorder columns
SELECT score as grade, name FROM student_grades

-- SELECT can define new columns
SELECT score+1 as augmented_score FROM student_grades


-- SELECT * to choose all columns
SELECT * FROM student_grades

-- SELECT and EXCEPT to exclude columns
--

-- where
SELECT * FROM student_grades
WHERE name='Alice';

-- IN
SELECT * FROM student_grades
WHERE name IN('Alice', 'Bob');

-- AND
SELECT * FROM student_grades
WHERE name IN('Alice', 'Bob')
and score>=7;

-- isNull filter
SELECT * FROM student_grades
WHERE score is NOT NULL;

-- comment
-- Select Alice and Bob’s good exam results 
SELECT * FROM student_grades
WHERE name IN ('Alice', 'Bob')
AND score >= 7;

-- limit
SELECT * FROM student_grades
LIMIT 4;

-- distinct
SELECT DISTINCT name FROM student_grades;

-- min, max, count
SELECT min (exam_result_id) as min_id,
max (exam_result_id) as max_id,
count (score) as count_score
FROM student_grades;

-- min, max, avg
SELECT name,
MIN(exam_result_id) AS min_id,
MAX(exam_result_id) AS max_id,
AVG(score) AS avg_score
FROM student_grades
GROUP BY name

--order by
SELECT * FROM student_grades
ORDER BY score DESC; -- ASC

-- challenge
-- Coba buat sendiri ya

```