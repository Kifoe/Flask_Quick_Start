from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/posts")
def posts():
    return render_template('posts.html', posts=range(1, 11))


@app.route("/bye")
def bye():
    return f"<h1>Bye, world </h1>"


@app.route("/hello/<username>")
def hello_user(username):
    return render_template('hello_user.html',username=username)


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    return render_template('show_posts.html', post_id=post_id)


@app.route('/login')
def login():
    return f"Login"