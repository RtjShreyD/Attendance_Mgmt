import psycopg2
import os
from models import db, User

# Load database configurations from environment variables
db_name = os.getenv('DB_NAME', 'attendance_db')
db_user = os.getenv('DB_USER', 'postgres')
db_password = os.getenv('DB_PASS', 'password')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '5432')

db_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

def create_database_if_not_exists():
    """Creates the PostgreSQL database if it does not already exist."""
    db_name = os.getenv('DB_NAME', 'attendance_db')
    db_user = os.getenv('DB_USER', 'postgres')
    db_password = os.getenv('DB_PASS', 'password')
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = os.getenv('DB_PORT', '5432')

    try:
        # Connect to PostgreSQL without specifying a database
        connection = psycopg2.connect(
            dbname="postgres", user=db_user, password=db_password, host=db_host, port=db_port
        )
        connection.autocommit = True
        cursor = connection.cursor()

        # Check if the database exists
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
        if not cursor.fetchone():
            cursor.execute(f'CREATE DATABASE "{db_name}"')
            print(f"Database '{db_name}' created successfully.")
        else:
            print(f"Database '{db_name}' already exists.")

        cursor.close()
        connection.close()

    except psycopg2.Error as e:
        print(f"Error creating database: {e}")

def create_first_user():
    """
    Creates the first admin user if it does not exist.
    """
    try:
        existing_user = User.query.filter_by(username="admin").first()
        if existing_user:
            print("Admin user already exists.")
            return
        
        data = {
            "type": "admin",
            "full_name": "Admin User",
            "username": "admin",
            "email": "admin@example.com",
            "password": 'admin',  # Hash the password before saving
            "submitted_by": "system"
        }
        
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()

        print("Added 1st user : Username - admin, password - admin")
    
    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
