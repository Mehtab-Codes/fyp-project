from flask import Blueprint, request, jsonify
from app.models import User
from app import db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required
import json
from app.recommender import generate_recommendations

auth_routes = Blueprint('auth_routes', __name__)
main_routes = Blueprint('main_routes', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    courses = json.dumps(data.get('courses', []))
    skills = json.dumps(data.get('skills', []))
    interests = json.dumps(data.get('interests', []))

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists'}), 400

    user = User(
        username=username,
        email=email,
        courses=courses,
        skills=skills,
        interests=interests
    )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid username or password'}), 401

    login_user(user)
    return jsonify({
        'message': 'Logged in successfully',
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'courses': json.loads(user.courses),
            'skills': json.loads(user.skills),
            'interests': json.loads(user.interests)
        }
    })

@auth_routes.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})

@main_routes.route('/recommendations', methods=['GET'])
@login_required
def get_recommendations():
    recommendations = generate_recommendations(current_user)
    return jsonify(recommendations)
