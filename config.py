SECRET_KEY = 'mps'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        user='mps',
        password='1qaz2wsx3edc',
        server='localhost:3306',
        database='agenda0'
    )
