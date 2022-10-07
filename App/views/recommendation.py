from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    create_recommendation, 
    get_all_recommendation_for_user_json,
    create_notification
)

recommendation_views = Blueprint('recommendation_views', __name__, template_folder='../templates')  

@recommendation_views.route('/api/recommendation', methods=['POST'])
@jwt_required()
def create_recommendation_action():
    if current_identity.role == 'teacher':                          # checks that only teachers can create recommendations
        data = request.json                                         # get data from request body
        recommendation = create_recommendation(data['letter'], data['recipient_id'])
        return jsonify({"message":f" {data['letter']} created with id {recommendation.id} for user {current_identity.id}"})
    else:
        return jsonify({"message": f"Must be logged in as a teacher"})          #if user is not a teacher

@recommendation_views.route('/recommendation', methods=['GET'])
@jwt_required()
def get_all_recommendation_for_user():
    recommendations = get_all_recommendation_for_user_json()
    if recommendations:         # if recommendations exist return the recommendations else error message
        return recommendations
    return jsonify({"message": f"No recommendations"})

@recommendation_views.route('/request/recommendation', methods=['POST'])
@jwt_required()
def request_recommendation():
    data = request.json                                         # get data from request body
    notification = create_notification(data['message'], data['recipient_id'])
    return jsonify({"message":f" {data['message']} created with id {notification.id} for user {data['recipient_id']}"})

