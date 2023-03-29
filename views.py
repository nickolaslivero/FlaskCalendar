from flask import render_template, redirect, request, url_for, session, flash
from app import app, db
from models import Tasks, Users

usuario = None


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == 'POST':
        # usuario = request.form['usuario']
        # senha = request.form['senha']
        return redirect(url_for('login'))
    else:
        return render_template('cadastro.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        global usuario
        usuario = Users.query.filter_by(user_name=request.form['usuario']).first()
        senha = request.form['senha']

        if usuario and senha == usuario.user_password:
            session['user'] = usuario.user_name
            flash('Olá, ' + session['user'] + ' você está logado.')
            return redirect(url_for('calendar'))
        else:
            flash('Usuário ou Senha inválidos')
            return redirect('/login')
    else:
        return render_template('login.html')


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session['user'] = None
    flash('Você foi deslogado.')
    return redirect('/login')


@app.route("/calendar", methods=["GET", "POST"])
def calendar():
    task_list = Tasks.query.order_by(Tasks.task_id).filter_by(user_id=usuario.user_id)
    return render_template('calendar.html', tasks=task_list)


@app.route("/newevent", methods=["GET", "POST"])
def newevent():
    if 'user' not in session or session['user'] is None:
        return redirect('/login')
    return render_template('newevent.html')


@app.route("/createevent", methods=["GET", "POST"])
def createevent():
    task_name = request.form['nome']
    task_date = request.form['data']
    task_description = request.form['desc']

    event = Tasks.query.filter_by(task_name=request.form['nome']).first()
    if event:
        flash('Tarefa já existente')
        return redirect(url_for('calendar'))

    new_event = Tasks(task_name=task_name, task_date=task_date, task_description=task_description,
                      user_id=usuario.user_id)
    db.session.add(new_event)
    db.session.commit()

    return redirect('/calendar')


@app.route("/editevent/<int:id>", methods=["GET", "POST"])
def editevent(id):
    if 'user' not in session or session['user'] is None:
        return redirect('/login')
    task = Tasks.query.filter_by(task_id=id).first()
    return render_template('editevent.html', task=task)


@app.route("/updateevent", methods=["GET", "POST"])
def updateevent():
    task = Tasks.query.filter_by(task_id=request.form['id']).first()
    task.task_name = request.form['nome']
    task.task_date = request.form['data']
    task.task_description = request.form['desc']

    db.session.add(task)
    db.session.commit()

    return redirect(url_for('calendar'))
