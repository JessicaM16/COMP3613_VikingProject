from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Notification(db.Model):                      
    id = db.Column(db.Integer, primary_key=True)                                        # the notification ID
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)      # the user that recieves the notification (who it is for)
    sender = db.Column(db.Integer, nullable=False)                                      # the user that writes the notification (who it is from)
    message = db.Column(db.String(200), nullable=False)                                 # notification message content

    def _init_(self, ID, message, recipient_id):
        self.id = ID                                
        self.message = message 
        self.recipient_id = recipient_id
        self.sender  

    def toJSON(self):
        return{
            'ID': self.id,
            'message': self.message,
            'recipient_id': self.recipient_id,
            'sender': self.sender
        }