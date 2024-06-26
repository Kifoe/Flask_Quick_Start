from flask import render_template, redirect, url_for, session, flash
from flask import Flask, request

from forms.login_form import LoginForm
from forms.registration_form import RegistrationForm
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/pisos")
def pisos():
    return render_template('hello_world.html')


@app.route("/posts")
def posts():
    return render_template('posts.html', posts=range(1, 11))


user_database = {
    "vasyl": "123456",
    "kifoe": "123",
    "oleksandr": "1234"
}

app.secret_key = 'PISOS'


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    return render_template('show_posts.html', post_id=post_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = request.form['username']
        password = request.form['password']
        if username in user_database and user_database[username] == password:
            session['username'] = username
            flash("You successfuly logged")
            return redirect(url_for('hello_user', username=request.form['username']))

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for register')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route("/user/<username>")
def hello_user(username):
    return render_template('hello_user.html', username=username)


@app.route('/users')
def show_users_profile():
    users = [
        'kyznetsov',
        'arsen',
        'Sovyak'
    ]
    return render_template('user_list.html', users=users)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)