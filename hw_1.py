CREATE TABLE actors (
id SERIAL PRIMARY KEY,
actor VARCHAR(255) NOT NULL
);

INSERT INTO actors (actor)
values 
('Jon'), 
('Don'),
('Ann');

CREATE TABLE directors (
id SERIAL PRIMARY KEY, 
director VARCHAR(255) NOT NULL
);

INSERT INTO directors (director)
VALUES 
('Karen'), 
('Bob'), 
('Ann'), 
('Jon');

CREATE TABLE movie (
	id SERIAL PRIMARY KEY, 
	film VARCHAR(255) NOT NULL, 
	actor_id int
		REFERENCES actors(id), 
	director_id int
		REFERENCES directors(id));

INSERT INTO movie (film, actor_id, director_id)
VALUES 
('Revenge', '2', '4'),
('Revenge 2', '1', '1'),
('Revenge 3', '3', '1'),
('Revenge 4', '3', '3'),
('Revenge 5', '2', '2');
