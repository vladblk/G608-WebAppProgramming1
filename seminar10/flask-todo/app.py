from logging import debug
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    todo_list = Todo.query.all()

    return render_template('base.html', all_todos=todo_list)


@app.route('/add', methods=["POST"])
def add():
    todo_title = request.form.get('todo')

    new_todo = Todo(
        title=todo_title,
        complete=False
    )

    db.session.add(new_todo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete

    db.session.commit()

    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()

    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()

    # new_todo = Todo(title='Todo 1', complete=False)
    # db.session.add(new_todo)
    # db.session.commit()

    app.run(debug=True)