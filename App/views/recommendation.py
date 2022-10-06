from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    create_recommendation, 
    get_all_recommendation,
    get_all_recommendation_json,
    get_all_recommendation_for_user_json
)

recommendation_views = Blueprint('recommendation_views', __name__, template_folder='../templates')  

@recommendation_views.route('/api/recommendation', methods=['POST'])
@jwt_required()
def create_recommendation_action():
    #if user is a teacher how to do that
    if current_identity.role == 'teacher':
        data = request.json # get data from request body
        recommendation = create_recommendation(data['letter'], data['recipient_id'])
        return jsonify({"message":f" {data['letter']} created with id {recommendation.id} for user {current_identity.id}"})
    else:
        return jsonify({"message": f"Must be logged in as a teacher"})

@recommendation_views.route('/recommendation', methods=['GET'])
@jwt_required()
def get_all_recommendation_for_user():
    return get_all_recommendation_for_user_json(current_identity.id)

