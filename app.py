import os
import shutil

from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, login_manager

from werkzeug.utils import secure_filename

from classes import StudProjectGraded, Card, User

from data import user1, user2

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'png', 'jpg', 'jpeg', 'pdf', 'docx'}

app = Flask(__name__)
app.secret_key = '12345'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Пример данных пользователей
users = {
    user1.id: user1,
    user2.id: user2
}

logins_ids = {
    user1.login: user1.id,
    user2.login: user2.id
}

@login_manager.user_loader
def load_user(user_id):
    # print(f"Attempting to load user with ID: {user_id}")
    user = users.get(int(user_id))
    # print(f"Loading user: {user}")
    if user:
        return User(user.id, user.login, user.password, user.edu_info, user.projects)
    return None


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user = users.get(logins_ids.get(login))

        # print(f"Login attempt: {login}, {password}")

        if user and user.password == password:
            user_obj = User(user.id, user.login, user.password, user.edu_info, user.projects)
            login_user(user_obj)

            # print(f"User {user.login} logged in successfully")

            return redirect(url_for('index'))
        
        # print("Invalid login or password")
        return 'Invalid login or password'
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    # print(f"Current user: {current_user}")
    # print(f"Session: {session}")

    return render_template('index.html', projects = users.get(current_user.id).cards.values())

@app.route('/shared/<int:id>', methods=['GET'])
def shared_portfolio(id):
    if current_user.is_authenticated and current_user.id == id:
        return redirect(url_for('index'))

    user = users.get(id)
    if user:
        return render_template('outer_portfolio.html', user = user, projects = users.get(id).cards.values())
    else:
        return "Пользователь не найден", 404


@app.route('/add', methods=['GET', 'POST'])
def add_card():
    if request.method == 'GET':
        project_id = int(request.args.get('id'))
        
        project = users.get(current_user.id).available_projects[project_id]
        
        return render_template('add.html', project=project)
    
    if request.method == 'POST':
        id = int(request.form['id'])
        description = request.form['description']
        files = request.files.getlist('files')
        outer_link = request.form['outer_link']

        user_id = current_user.id
        user_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(user_id))
        project_folder = os.path.join(user_folder, str(id))

        # Создаем папки, если они не существуют
        os.makedirs(project_folder, exist_ok=True)

        file_paths = []
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(project_folder, filename)
                file.save(file_path)
                file_paths.append(file_path)

        card = Card(users.get(current_user.id).available_projects[id], description, file_paths, outer_link)
        
        users.get(current_user.id).cards[id] = card

        users.get(current_user.id).available_projects.pop(id) # надо будет добавить невозможность добавить, если все проекты закончились
        
        return redirect('/')
    
    return render_template('add.html', title=project)

@app.route('/select')
def select_project():
    return render_template('select.html', projects=users.get(current_user.id).available_projects)

@app.route('/description')
def get_description():
    card_id = int(request.args.get('id'))
    card = users.get(current_user.id).cards[card_id]
    
    return render_template('description.html', card=card)

@app.route('/shared/<int:id>/description')
def get_shared_description(id):
    card_id = int(request.args.get('card_id'))
    user = users.get(id)
    if user:
        card = user.cards.get(card_id)
        if card:
            return render_template('description.html', card=card)
    else:
        return "Пользователь не найден", 404


@app.route('/delete_project/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    deleted_card = users.get(current_user.id).cards.pop(project_id)
    users.get(current_user.id).available_projects[project_id] = deleted_card

    user_id = current_user.id
    project_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(user_id), str(project_id))

    # Удаляем папку проекта и все её содержимое
    if os.path.exists(project_folder):
        shutil.rmtree(project_folder)

    return '', 204

if __name__ == '__main__':
    app.run(debug=True)