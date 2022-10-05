from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity
from App.models import User
from App.database import db

from flask_login import login_required

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    get_user_by_username,
    authenticate,
    login_user,
    logout_user
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')  
    


    ##Sign-up route!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@user_views.route('/api/users', methods=['POST'])
def create_user_action():
    data = request.json # get data from request body
    user = User.query.filter_by(email=data['email']).first() # if this returns a user, then the email already exists in database
    if user:
        return jsonify({"message":f" Email Already Used"})
    create_user(data['username'], data['email'], data['password'], data['role'])
    return jsonify({"message":f" Account Created"})

@user_views.route('/login', methods=['POST'])
def login_user_action():
    data = request.json
    user = authenticate(data['username'], data['password'])
    if user:
        login_user(user, True)
        return jsonify({"message": f"Login Successful "})
    return jsonify({"message": f"Login Fail"})

@user_views.route('/logout')
def logout_user_action():
    logout_user()
    return jsonify({"message": f"Logout Successfully"})


@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/identify', methods=['GET'])
@jwt_required()
def identify_user_action():
    return jsonify({'message': f"user: {current_identity.username}"})

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')
