from app import db


class Tasks(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(255))
    task_date = db.Column(db.Date)
    task_description = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.task_name


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255), nullable=False)
    user_password = db.Column(db.String(255), nullable=False)

    # tasks = db.relationship('Task', backref='user', lazy=True)

    def __repr__(self):
        return '<Name %r>' % self.user_name
