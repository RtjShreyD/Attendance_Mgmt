# routes.py
from flask import Blueprint, request, jsonify
from models import db, User, Department, Student, Course, AttendanceLog

user_routes = Blueprint('user_routes', __name__)
department_routes = Blueprint('department_routes', __name__)
student_routes = Blueprint('student_routes', __name__)
course_routes = Blueprint('course_routes', __name__)
attendance_routes = Blueprint('attendance_routes', __name__)

@user_routes.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@user_routes.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([user.__dict__ for user in users if '_sa_instance_state' not in user.__dict__])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            return jsonify({k: v for k, v in user.__dict__.items() if k != '_sa_instance_state'})
        return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404
        data = request.get_json()
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@department_routes.route('/departments', methods=['POST'])
def create_department():
    try:
        data = request.get_json()
        new_department = Department(**data)
        db.session.add(new_department)
        db.session.commit()
        return jsonify({'message': 'Department created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@department_routes.route('/departments', methods=['GET'])
def get_departments():
    try:
        departments = Department.query.all()
        return jsonify([{k: v for k, v in dept.__dict__.items() if k != '_sa_instance_state'} for dept in departments])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@student_routes.route('/students', methods=['POST'])
def create_student():
    try:
        data = request.get_json()
        new_student = Student(**data)
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'message': 'Student created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@student_routes.route('/students', methods=['GET'])
def get_students():
    try:
        students = Student.query.all()
        return jsonify([{k: v for k, v in student.__dict__.items() if k != '_sa_instance_state'} for student in students])
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@course_routes.route('/courses', methods=['POST'])
def create_course():
    try:
        data = request.get_json()
        new_course = Course(**data)
        db.session.add(new_course)
        db.session.commit()
        return jsonify({'message': 'Course created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@course_routes.route('/courses', methods=['GET'])
def get_courses():
    try:
        courses = Course.query.all()
        return jsonify([{k: v for k, v in course.__dict__.items() if k != '_sa_instance_state'} for course in courses])
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@attendance_routes.route('/attendance', methods=['POST'])
def create_attendance_log():
    try:
        data = request.get_json()
        new_attendance_log = AttendanceLog(**data)
        db.session.add(new_attendance_log)
        db.session.commit()
        return jsonify({'message': 'Attendance log created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Get attendance logs route
@attendance_routes.route('/attendance', methods=['GET'])
def get_attendance_logs():
    try:
        attendance_logs = AttendanceLog.query.all()
        return jsonify([{
            'id': log.id,
            'student_id': log.student_id,
            'course_id': log.course_id,
            'present': log.present,
            'submitted_by': log.submitted_by,
            'updated_at': log.updated_at
        } for log in attendance_logs])
    except Exception as e:
        return jsonify({'error': str(e)}), 500