# Basic "TO DO app" created using Python and Flask technologies

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# creating models for our app
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_text = db.Column(db.String(300), nullable=False)
    task_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Todo %r>' % self.id


# creating adding task view logic
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        add_task = request.form['add-task']
        adding_task = Todo(task_text=add_task)

        try:
            db.session.add(adding_task)
            db.session.commit()
            return redirect('/')

        except:
            return "Something went wrong. Seems that no task has been added"

    else:
        add_task_list = Todo.query.order_by(Todo.task_date).all()
        return render_template('index.html', add_task_list=add_task_list)


# creating update view logic
@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    update_task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        update_task.task_text = request.form['add-task']

        try:
            db.session.commit()
            return redirect('/')

        except:
            return "Something went wrong. Seems that we cannot update the task"

    else:
        return render_template('update.html', update_task=update_task)


# creating the delete view logic
@app.route('/delete/<int:id>')
def delete(id):
    delete_task = Todo.query.get_or_404(id)

    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect('/')

    except:
        return 'We could not manage this operation'


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)