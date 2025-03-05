-- №1 Rooms list and amount of students in each of them.
SELECT rooms.id, COUNT(students.id) as num_students
FROM rooms
LEFT JOIN students
ON rooms.id = students.room
GROUP BY rooms.id, rooms.name;
-- №2 5 rooms with the smallest average age of students.
SELECT rooms.id, CAST(AVG(TIMESTAMPDIFF(YEAR, students.birthday, CURDATE())) AS FLOAT) AS avg_age
FROM rooms
INNER JOIN students
ON rooms.id = students.room
GROUP BY rooms.id, rooms.name
ORDER BY avg_age ASC
LIMIT 5;
-- №3 5 rooms with the biggesst difference in students age.
SELECT rooms.id, 
MAX(TIMESTAMPDIFF(YEAR, students.birthday, CURDATE())) - MIN(TIMESTAMPDIFF(YEAR, students.birthday, CURDATE())) AS age_diff
FROM rooms
INNER JOIN students
ON rooms.id = students.room
GROUP BY rooms.id, rooms.name
ORDER BY age_diff DESC
LIMIT 5;
-- №4 List of rooms where students of different sexes live
SELECT rooms.id 
FROM rooms
INNER JOIN students
ON rooms.id = students.room
GROUP BY rooms.id, rooms.name
HAVING COUNT(DISTINCT sex > 1);