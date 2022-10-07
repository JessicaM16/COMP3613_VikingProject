from App.models import Notification
from App.database import db 
from flask_jwt import current_identity
import json 

#

# creates a notification given the notification letter and the person to recieve
def create_notification(message, recipient_id):
    newnotification = Notification(message=message, recipient_id=recipient_id, sender = current_identity.id)
    db.session.add(newnotification)
    db.session.commit()
    return newnotification

#Viewing Notifications of the current user
def get_all_notifications_for_user_json():
    if current_identity.role == "student":
        notifications = Notification.query.filter_by(recipient_id=current_identity.id).all()                        # student can only see its own notifications
    else:    
        notifications = Notification.query.filter_by(sender=current_identity.id).all()                               # teacher can see all the notifications they created

    notifications = [notification.toJSON() for Notification in notifications]
    return json.dumps(notifications)
