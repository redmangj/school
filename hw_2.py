CREATE TABLE departments(
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL
);
CREATE TABLE teachers(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	department_id INT REFERENCES departments(id)
);
CREATE TABLE groups(
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	department_id INT REFERENCES departments(id)
);
CREATE TABLE students(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	group_id INT REFERENCES groups(id)
);

INSERT INTO departments (name) VALUES
('Computer Science'),
('Mathematics'),
('Physics');

INSERT INTO teachers (first_name, last_name, department_id) VALUES
('John', 'Doe', 1),
('Jane', 'Smith', 2),
('Robert', 'Johnson', 3),
('Emily', 'Williams', 1),
('Michael', 'Brown', 2);

INSERT INTO groups (name, department_id) VALUES
('CS50', 1),
('Math101', 2),
('Phys101', 3),
('CS101', 1);

INSERT INTO students (first_name, last_name, group_id) VALUES
('Alice', 'Johnson', 1),
('Bob', 'Smith', 2),
('Charlie', 'Williams', 3),
('David', 'Brown', 1),
('Eva', 'Davis', 2),
('Frank', 'Miller', 3),
('Grace', 'Jones', 4),
('Henry', 'Anderson', 1),
('Ivy', 'Moore', 2),
('Jack', 'Taylor', 3),
('Kate', 'White', 4),
('Leo', 'Martin', 1),
('Mia', 'Young', 2),
('Noah', 'Lee', 3),
('Olivia', 'Harris', 4),
('Paul', 'Clark', 1),
('Quinn', 'Evans', 2),
('Ryan', 'Wright', 3),
('Sophia', 'Walker', 4),
('Tyler', 'Hill', 1);


select first_name as Ім’я, last_name as Прізвище, name as Назва_групи
from students
INNER JOIN groups ON (groups.id = students.group_id);

select first_name as Ім’я, last_name as Прізвище, name as Назва_кафедри
from teachers
INNER JOIN departments ON (departments.id = teachers.department_id);


select
CONCAT(students.first_name,' ', students.last_name) AS  students_names,
groups.name as groups,
departments.name as departments,
CONCAT(teachers.first_name,' ', teachers.last_name) AS  teachers_name
FROM students
join groups on groups.id = students.group_id
join departments on departments.id = groups.department_id
join teachers on departments.id = teachers.department_id
WHERE students.last_name = 'Smith'
or students.last_name = 'Williams'
or students.last_name = 'Johnson'
ORDER BY groups.name, students.last_name
;
