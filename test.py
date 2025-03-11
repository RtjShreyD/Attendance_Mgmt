import requests
import json

BASE_URL = "http://127.0.0.1:5000"  # Change this to your Flask app's URL

# Test Create User
def test_create_user():
    print("Testing create user...")
    data = {
        "type": "admin",
        "full_name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com",
        "password": "password123",
        "submitted_by": "admin"
    }
    response = requests.post(f"{BASE_URL}/users", json=data)
    print("Create User Response:", response.json())

# Test Get Users
def test_get_users():
    print("Testing get users...")
    response = requests.get(f"{BASE_URL}/users")
    print("Get Users Response:", response.json())

# Test Create Department
def test_create_department():
    print("Testing create department...")
    data = {
        "department_name": "Computer Science",
        "submitted_by": "admin"
    }
    response = requests.post(f"{BASE_URL}/departments", json=data)
    print("Create Department Response:", response.json())

# Test Get Departments
def test_get_departments():
    print("Testing get departments...")
    response = requests.get(f"{BASE_URL}/departments")
    print("Get Departments Response:", response.json())

# Test Create Student
def test_create_student():
    print("Testing create student...")
    data = {
        "full_name": "Alice Smith",
        "department_id": 1,
        "class_name": "CS101",
        "submitted_by": "admin"
    }
    response = requests.post(f"{BASE_URL}/students", json=data)
    print("Create Student Response:", response.json())

# Test Get Students
def test_get_students():
    print("Testing get students...")
    response = requests.get(f"{BASE_URL}/students")
    print("Get Students Response:", response.json())

# Test Create Course
def test_create_course():
    print("Testing create course...")
    data = {
        "course_name": "Introduction to Programming",
        "department_id": 1,
        "semester": 1,
        "class_name": "CS101",
        "lecture_hours": 40,
        "submitted_by": "admin"
    }
    response = requests.post(f"{BASE_URL}/courses", json=data)
    print("Create Course Response:", response.json())

# Test Get Courses
def test_get_courses():
    print("Testing get courses...")
    response = requests.get(f"{BASE_URL}/courses")
    print("Get Courses Response:", response.json())

# Test Create Attendance Log
def test_create_attendance_log():
    print("Testing create attendance log...")
    data = {
        "student_id": 1,
        "course_id": 1,
        "present": True,
        "submitted_by": "admin"
    }
    response = requests.post(f"{BASE_URL}/attendance", json=data)
    print("Create Attendance Log Response:", response.json())

# Test Get Attendance Logs
def test_get_attendance_logs():
    print("Testing get attendance logs...")
    response = requests.get(f"{BASE_URL}/attendance")
    print("Get Attendance Logs Response:", response.json())

# Run all tests
if __name__ == "__main__":
    test_create_user()
    test_get_users()
    test_create_department()
    test_get_departments()
    test_create_student()
    test_get_students()
    test_create_course()
    test_get_courses()
    test_create_attendance_log()
    test_get_attendance_logs()
