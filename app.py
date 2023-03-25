from flask import render_template, redirect, request, url_for, session, flash
import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

flask_app = app.app
flask_app.secret_key = 'mps'




class Task:
    def __init__(self, task_name, task_date, task_description):
        self.task_name = task_name
        self.task_date = task_date
        self.task_description = task_description


user_dict = {}
task_list = []

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        user_dict[usuario] = senha
        return redirect(url_for('login'))
    else:
        return render_template('cadastro.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario in user_dict and user_dict[usuario] == senha:
            session['user'] = usuario
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
    task = Task(task_name, task_date, task_description)
    task_list.append(task)
    return redirect('/calendar')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
