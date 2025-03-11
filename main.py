# main.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from routes import user_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rtjadmin@localhost:5432/attendance_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(user_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)