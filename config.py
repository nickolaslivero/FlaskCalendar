SECRET_KEY = 'mps'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        user='root',
        password='Ser3@ult',
        server='localhost:3306',
        database='agenda0'
    )
