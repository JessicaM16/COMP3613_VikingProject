from App.models import Recommendation
from App.database import db 
from flask_jwt import current_identity
import json 

def get_all_recommendation_for_user_json():
    if current_identity.role == "student":
        recommendations = Recommendation.query.filter_by(recipient_id=current_identity.id).all()                        # student can only see its own recommendations
    else:    
        recommendations = Recommendation.query.filter_by(sender=current_identity.id).all()                              # teacher can see all the recommendations created

    recommendations = [recommendation.toJSON() for recommendation in recommendations]
    return json.dumps(recommendations)

# creates a recommendation given the recommendation letter and the person to recieve
def create_recommendation(recommendation, recipient_id):
    newrecommendation = Recommendation(letter=recommendation, recipient_id=recipient_id, sender = current_identity.id)
    db.session.add(newrecommendation)
    db.session.commit()
    return newrecommendation




def get_recommendation(ID):
    return Recommendation.query.get(ID)

def get_all_recommendation():
    return Recommendation.query.all()

def get_all_recommendation_json():
    recommendations = Recommendation.query.all()
    if not recommendations:
        return []
    recommendations = [recommendation.toJSON() for recommendation in recommendations]
    return recommendations

def update_recommendation(ID, recommendation):
    recommendation = get_recommendation(ID)
    if recommendation:
        recommendation.recommendation = recommendation
        db.session.add(recommendation)
        return db.session.commit()
    return None
    