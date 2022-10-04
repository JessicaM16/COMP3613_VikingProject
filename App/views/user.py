from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from App.models import User
from App.database import db

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    get_user_by_username
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')  
    
@user_views.route('/api/users', methods=['POST'])
def create_user_action():

    data = request.json # get data from request body
    user = User.query.filter_by(email=data['email']).first() # if this returns a user, then the email already exists in database

    if user:
        return jsonify({"message":f" Email Already Used"})
    newuser = User(username=data['username'], password=data['password'], email=data['email'], role= data['role'])
    db.session.add(newuser)
    db.session.commit()
    return jsonify({"message":f" Account Created"})

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')
