from App.models import Notification
from App.database import db 
from flask_jwt import current_identity
import json 

# creates a notification given the notification letter and the person to recieve
def create_notification(message, recipient_id):
    newnotification = Notification(message=message, recipient_id=recipient_id, sender = current_identity.id)
    db.session.add(newnotification)
    db.session.commit()
    return newnotification

#Viewing Notifications of the current user
def get_all_notifications_for_user_json():

    notifications = Notification.query.filter_by(recipient_id=current_identity.id).all()    #get notifications for the current user
    if notifications:       # if the user has notifications
        notifications = [notification.toJSON() for notification in notifications]
        return json.dumps(notifications)

    return []