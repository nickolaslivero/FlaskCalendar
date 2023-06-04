import connexion
from flask_sqlalchemy import SQLAlchemy

app = connexion.App(__name__, specification_dir='./')

flask_app = app.app
flask_app.config.from_pyfile('config.py')

db = SQLAlchemy(flask_app)

from views.views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
