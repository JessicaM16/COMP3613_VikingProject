from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Notification(db.Model):                      
    id = db.Column(db.Integer, primary_key=True)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sender = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(200), nullable=False)

    def _init_(self, ID, message, recipient_id):
        self.id = ID                                #for the rec
        self.message = message                        #message itself
        self.recipient_id = recipient_id            #who it is for
        self.sender

    def toJSON(self):
        return{
            'ID': self.id,
            'message': self.message,
            'recipient_id': self.recipient_id,
            'sender': self.sender
        }