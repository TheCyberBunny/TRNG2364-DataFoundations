--Joins
--Inner Join - students who are enrolled in a course
SELECT 
	student.first_name,
	student.last_name,
	course.course_name
FROM enrollment
INNER JOIN student ON enrollment.student_id = student.student_id
INNER JOIN course ON enrollment.course_id = course.course_id;

--Left Join - show all students and their courses
SELECT
	student.first_name,
	student.last_name,
	enrollment.course_id,
	course.course_name
FROM student
LEFT JOIN enrollment ON student.student_id = enrollment.student_id
LEFT JOIN course ON enrollment.course_id = course.course_id;

--Right join - shows all rows from the right table even if there is no match
SELECT
	student.first_name,
	student.last_name,
	enrollment.course_id,
	course.course_name
FROM enrollment
RIGHT JOIN course ON enrollment.course_id = course.course_id
RIGHT JOIN student ON enrollment.student_id = student.student_id;

SELECT
	student.first_name,
	student.last_name,
	enrollment.course_id,
	course.course_name
FROM student
RIGHT JOIN enrollment ON student.student_id = enrollment.student_id
RIGHT JOIN course ON enrollment.course_id = course.course_id;

--Full outer join - show all students and courses even without enrollment
SELECT
	student.first_name,
	student.last_name,
	enrollment.course_id,
	course.course_name
FROM student
FULL JOIN enrollment ON student.student_id = enrollment.student_id
FULL JOIN course ON enrollment.course_id = course.course_id;

--Cross join - show all possible combinations between the joined tables
--not super useful, but possibly used in statistics
--show all possible student-course combinations
SELECT
	student.first_name,
	student.last_name,
	course.course_name
FROM student
CROSS JOIN course;

--Subqueries
SELECT * FROM student;

--Students enrolled in more than one course
SELECT * FROM student
WHERE student_id IN(
	SELECT student_id
	FROM enrollment
	GROUP BY student_id
	HAVING COUNT(course_id) > 1
);

--Courses that no student has enrolled in
SELECT * FROM course
WHERE course_id NOT IN (
	SELECT course_id FROM enrollment
)

--Students who are not enrolled in any course
SELECT * FROM student
WHERE student_id NOT IN(
	SELECT student_id FROM enrollment
)

-- Stored procedures
--are prepared SQL code that you can save and reuse
--good for if you have a sql query that gets used over and over again
--we can call our stored procedures to execute them


CREATE PROCEDURE selectAllStudents()
LANGUAGE plpgsql
AS $$
BEGIN
SELECT * FROM student;
END $$;

CALL selectAllStudents();

--we can give our stored procedures parameters
CREATE PROCEDURE updatemajorstudents(p_major VARCHAR(2), p_student_id INT)
LANGUAGE plpgsql
AS $$
BEGIN
UPDATE student
SET major = p_major
WHERE student_id = p_student_id;
END $$;

CALL selectmajorStudents('CS');


--functions return a value, while stored procedures do not
--functions are mainly used for calculations or building operations into a single DB call
-- $$ marks the beginning and end of a block of executable code
-- DELCARE lets us delcare variables for the function
CREATE OR REPLACE FUNCTION get_course_count(p_student_id INT)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
	total_courses INT;
BEGIN
	SELECT COUNT(*)
	INTO total_courses
	FROM enrollment
	WHERE student_id = p_student_id;
	RETURN total_courses;
END;
$$;

SELECT 
	first_name, 
	last_name, 
	get_course_count(student_id) AS course_count
FROM student;


SELECT * FROM student;