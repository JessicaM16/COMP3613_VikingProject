from App.models import Recommendation
from App.database import db

def create_recommendation(recommendation):
    newrecommendation = Recommendation(letter=recommendation)
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
    return recommendation

def update_recommendation(ID, recommendation):
    recommendation = get_recommendation(ID)
    if recommendation:
        recommendation.recommendation = recommendation
        db.session.add(recommendation)
        return db.session.commit()
    return None
    