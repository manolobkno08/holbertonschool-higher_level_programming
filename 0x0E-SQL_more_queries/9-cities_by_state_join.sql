-- List all cities
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.id = states.id
ORDER BY cities.id ASC;
