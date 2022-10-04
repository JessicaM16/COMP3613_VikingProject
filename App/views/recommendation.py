from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from App.controllers import (
    create_recommendation, 
    get_all_recommendation,
    get_all_recommendation_json,
)

recommendation_views = Blueprint('recommendation_views', __name__, template_folder='../templates')  

@recommendation_views.route('/api/recommendation', methods=['POST'])
def create_recommendation_action():
    data = request.json # get data from request body
    recommendation = create_recommendation(data['letter'])
    return jsonify({"message":f" {data['letter']} created with id {recommendation.id}"})

@recommendation_views.route('/recommendation', methods=['GET'])
def get_recommendation_page():
    recommendations = get_all_recommendation()
    return render_template('recommendation.html', recommendations=recommendations)

@recommendation_views.route('/api/recommendation')
def client_app():
    recommendations = get_all_recommendation_json()
    return jsonify(recommendations)

