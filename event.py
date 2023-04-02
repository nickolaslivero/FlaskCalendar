from flask import abort, make_response
import mysql.connector

config = {
    'user': 'mps',
    'password': '1qaz2wsx3edc',
    'host': '192.168.0.157',
    'database': 'agenda0'
}

mydb = mysql.connector.connect(**config)
mycursor = mydb.cursor()

def read_all():
    mycursor.execute("SELECT * FROM tasks")
    rows = mycursor.fetchall()

    tasks = []
    for row in rows:
        tasks.append({
            'task_id': row[0],
            'task_name': row[1],
            'task_date': row[2],
            'task_description': row[3],
            'user_id': row[4]
        })

    return tasks


def create(task):
    task_id = task.get('task_id')
    task_name = task.get('task_name', '')
    task_date = task.get('task_date')
    task_description = task.get('task_description')
    user_id = task.get('user_id')

    sql = "INSERT INTO tasks (task_id, task_name, task_date, task_description, user_id) VALUES (%s, %s, %s, %s, %s)"
    val = (task_id, task_name, task_date, task_description, user_id)
    mycursor.execute(sql, val)
    mydb.commit()

    return task, 201


def read_one(task_id):
    mycursor.execute("SELECT * FROM tasks WHERE task_id = %s", (task_id,))
    row = mycursor.fetchone()

    if row is not None:
        return {
            'task_id': row[0],
            'task_name': row[1],
            'task_date': row[2],
            'task_description': row[3],
            'user_id': row[4]
        }
    else:
        abort(404, f'Event not found')


def update(task_id, event):
    task_name = event.get('task_name', '')
    task_description = event.get('task_description')

    sql = "UPDATE tasks SET task_name = %s, task_description = %s WHERE task_id = %s"
    val = (task_name, task_description, task_id)
    mycursor.execute(sql, val)
    mydb.commit()

    if mycursor.rowcount > 0:
        return {
            'task_id': task_id,
            'task_name': task_name,
            'task_date': event.get('task_date'),
            'task_description': task_description,
            'user_id': event.get('user_id')
        }
    else:
        abort(
            404,
            f"Event with ID {task_id} not found"
        )


def delete(task_id):
    mycursor.execute("DELETE FROM tasks WHERE task_id = %s", (task_id,))
    mydb.commit()

    if mycursor.rowcount > 0:
        return make_response(
            f"{task_id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Event with ID {task_id} not found"
        )
