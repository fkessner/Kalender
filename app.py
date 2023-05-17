from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar.db'
db = SQLAlchemy(app)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-DD

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        new_appointment = Appointment(title=title, date=date)
        db.session.add(new_appointment)
        db.session.commit()
        return 'Appointment added!'
    else:
        appointments = Appointment.query.all()
        return render_template('index.html', appointments=appointments)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
