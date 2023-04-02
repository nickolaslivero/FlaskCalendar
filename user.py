import mysql.connector
from flask import abort, make_response

config = {
    'user': 'mps',
    'password': '1qaz2wsx3edc',
    'host': '192.168.0.157',
    'database': 'agenda0'
}

mydb = mysql.connector.connect(**config)
cursor = mydb.cursor()



def read_all():
    query = 'SELECT * FROM users'
    cursor.execute(query)
    result = cursor.fetchall()
    users = []
    for row in result:
        user = {
            'user_id': row[0],
            'user_name': row[1],
            'user_password': row[2],
        }
        users.append(user)
    return users



def create(user):
    user_id = user.get('user_id')
    user_name = user.get('user_name', '')
    user_password = user.get('user_password', '')

    if user_id:
        query = 'INSERT INTO users (user_id, user_name, user_password) VALUES (%s, %s, %s)'
        values = (user_id, user_name, user_password)
        cursor.execute(query, values)
        mydb.commit()
        return user, 201
    else:
        abort(
            406,
            f'user with last name {user_id} already exists',
        )



def read_one(user_id):
    query = 'SELECT * FROM users WHERE user_id = %s'
    values = (user_id,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    if result:
        user = {
            'user_id': result[0],
            'user_name': result[1],
            'user_password': result[2],
        }
        return user
    else:
        abort(404, f'User not found')


def update(user_id, user):
    if user_id:
        query = 'UPDATE users SET user_name = %s'
        values = (user.get('user_name', ''), user_id)
        cursor.execute(query, values)
        mydb.commit()
        if cursor.rowcount > 0:
            user['user_id'] = user_id
            return user
        else:
            abort(
                404,
                f"Person with ID {user_id} not found")


def delete(user_id):
    sql = "DELETE FROM users WHERE user_id = %s"
    val = (user_id,)

    cursor.execute(sql, val)

    if cursor.rowcount == 1:
        mydb.commit()
        return make_response(f"{user_id} successfully deleted", 200)
    else:
        abort(404, f"Person with ID {user_id} not found")

