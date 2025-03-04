-- №1 Список комнат и количество студентов в каждой из них
SELECT rooms, COUNT(students.id) as num_students
FROM rooms
LEFT JOIN students
ON rooms.id = students.room
GROUP BY rooms.id;

-- №2 5 комнат, где самый маленький средний возраст студентов
SELECT rooms.id, AVG(TIMESTAMPDIFF(YEAR, students.birthday, CURDATE())) AS avg_age
FROM rooms
INNER JOIN students
ON rooms.id = student.room
GROUP BY rooms.id
ORDER BY avg_age ASC
LIMIT 5;


-- №3 5 комнат с самой большой разницей в возрасте студентов
SELECT rooms.id, 
MAX(TIMESTAMPDIFF(YEAR, students.birthday, CURDATE())) - MIN(TIMESTAMPDIFF(YEAR, students.birthday, CURDATE())) AS age_diff
FROM rooms
INNER JOIN students
ON rooms.id = student.room
ORDER BY age_diff DESC
LIMIT 5;

-- №4 Список комнат где живут разнополые студенты
SELECT rooms.id 
FROM rooms
INNER JOIN students
ON rooms.id = student.room
GROUP BY rooms.id
HAVING SUM(CASE WHEN sex = 'F' THEN 1 ELSE 0 END) >= 1 
AND SUM(CASE WHEN sex = 'M' THEN 1 ELSE 0 END) >= 1;



-- Индексы
CREATE INDEX idx_rooms_id ON rooms (id);
CREATE INDEX idx_birthday ON students (birthday);
CREATE INDEX idx_sex ON students (sex);