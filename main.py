from flask import Flask
from models import db
from routes import user_routes, department_routes, student_routes, course_routes, attendance_routes
from utils import create_database_if_not_exists, create_first_user
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

create_database_if_not_exists()

# Fetch DB credentials from environment
db_name = os.getenv('DB_NAME', 'attendance_db')
db_user = os.getenv('DB_USER', 'postgres')
db_password = os.getenv('DB_PASS', 'password')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '5432')

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(user_routes)
app.register_blueprint(department_routes)
app.register_blueprint(student_routes)
app.register_blueprint(course_routes)
app.register_blueprint(attendance_routes)

if __name__ == '__main__':

    with app.app_context():
        db.create_all()  # Create tables if they don’t exist
        create_first_user()  # Ensure the first admin user exists

    app.run(debug=True)
