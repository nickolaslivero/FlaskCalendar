SECRET_KEY = 'mps'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        user='root',
        password='123456',
        server='127.0.0.1:3306',
        database='calendar'
    )
