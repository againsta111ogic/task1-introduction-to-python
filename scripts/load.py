import json
from db.db_connector import connect_to_db

rooms_query = 'INSERT INTO rooms (id, name) VALUES (%s, %s)'
students_query = 'INSERT INTO students (id, name, room, sex) VALUES (%s, %s, %s, %s)'

def load_data(rooms_file, students_file):

    db = connect_to_db()
    mycursor = db.cursor()

    with open(rooms_file, 'r') as f:
        rooms_data = json.load(f)
        for room in rooms_data:
            mycursor.execute(rooms_query, (room['id'], room['name']))
    
    with open(students_file, 'r') as f:
        students_data = json.load(f)
        for student in students_data:
            mycursor.execute(students_query, (student['id'], student['name'], student['room'], student['sex']))

    db.commit()
    mycursor.close()
    db.close()
