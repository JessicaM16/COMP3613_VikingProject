from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    create_notification,
    get_all_notifications_for_user_json
)


# request recommendation calls the create notification function asking the staff
# reject recommendation calls the create notification function saying rejected to the student
# and create the views for each user to view notifications 


notification_views = Blueprint('notification_views', __name__, template_folder='../templates')  

@notification_views.route('/api/notification', methods=['POST'])
@jwt_required()
def create_recommendation_action():
    if current_identity.role == 'teacher':                          # checks that only teachers can create recommendations
        data = request.json                                         # get data from request body
        recommendation = create_recommendation(data['letter'], data['recipient_id'])
        return jsonify({"message":f" {data['letter']} created with id {recommendation.id} for user {current_identity.id}"})
    else:
        return jsonify({"message": f"Must be logged in as a teacher"})          #if user is not a teacher

@notification_views.route('/recommendation', methods=['GET'])
@jwt_required()
def get_all_recommendation_for_user():
    recommendations = get_all_recommendation_for_user_json()
    if recommendations:         # if recommendations exist return the recommendations else error message
        return recommendations
    return jsonify({"message": f"No recommendations"})

