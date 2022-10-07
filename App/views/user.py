from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.models import User#

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

#Sign-up/Create user route -
#   Creates a new User(role: staff  or  student).
#   Checks that the user does not already exist by checking its email.
#   Creates new User if email not found 
@user_views.route('/api/users', methods=['POST'])#
def create_user_action():
    data = request.json 
    user = User.query.filter_by(email=data['email']).first() # if this returns a user, then the email already exists in database
    if user:
        return jsonify({"message":f" Email Already Used"})
    create_user(data['username'], data['email'], data['password'], data['role'])
    return jsonify({"message":f" Account Created"})


#displays a html page containing all user info
@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users_json()
    if users:
        return users
    return jsonify({"message": f"No Users"})





@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/identify', methods=['GET'])
@jwt_required()
def identify_user_action():
    return jsonify({'message': f"username: {current_identity.username}, id : {current_identity.id}"})

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')


