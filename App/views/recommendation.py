from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from flask_jwt import current_identity

from App.controllers import (
    create_recommendation, 
    get_all_recommendation_for_user_json,
    create_notification
)

recommendation_views = Blueprint('recommendation_views', __name__, template_folder='../templates')  


#Creates a Recommendation - 
#   Teachers can create recommendations (entering the recommendation message and the reciever id).
#   This creates a recommendation object and links it to the recieving student
@recommendation_views.route('/api/recommendation', methods=['POST'])
@jwt_required()
def create_recommendation_action():
    if current_identity.role == 'teacher':          # checks that only teachers can create recommendations
        data = request.json         # get data from request body
        recommendation = create_recommendation(data['letter'], data['recipient_id'])
        return jsonify({"message":f" {data['letter']} created with id {recommendation.id} for user {current_identity.id}"})
    else:
        return jsonify({"message": f"Must be logged in as a teacher"})          #if user is not a teacher


#Request all recommendations a student has
@recommendation_views.route('/recommendation', methods=['GET'])
@jwt_required()
def get_all_recommendation_for_user():
    if current_identity.role == "student":          #user has to be a student to have recommendations
        recommendations = get_all_recommendation_for_user_json()
        if recommendations:         # if recommendations exist return the recommendations else error message
            return recommendations
        return jsonify({"message": f"No recommendations"})
    else:
        return jsonify({"message": f"Only students can have recommendations"})


# Request Recommendation - 
#   Students are allowed to request Recommendation(s) from a teacher. 
#   This sends the teacher a Notification that ask them to send a recommendation.
@recommendation_views.route('/request/recommendation', methods=['POST'])
@jwt_required()
def request_recommendation():
    data = request.json                                         # get data from request body
    if current_identity.role == "student":                      # teachers are not allowed to request recommendations
        notification = create_notification(data['message'], data['recipient_id'])
        return jsonify({"message":f" {data['message']} created with id {notification.id} for user {data['recipient_id']}"})
    else:
        return jsonify({"message":f" teachers can't request recommendations"})


#Reject Recommendation-
#   Teachers can reject a recommendation request from students.
#   This sends the user a notification informing them that the request was rejected
@recommendation_views.route('/reject/recommendation', methods=['POST'])
@jwt_required()
def reject_recommendation_action():
    if current_identity.role == "teacher":      #only teachers can reject an application
        data = request.json
        notification = create_notification(f"Your recommendation request from {current_identity.username} has been rejected", data['recipient_id'])
        return jsonify({"message":f" Your recommendation request was rejected by {current_identity.username}"})
    else:
        return jsonify({"message":f" Not Permitted to Reject Applications"})
        
