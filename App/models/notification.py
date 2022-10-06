from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Notification(db.Model):                             
    id = db.Column(db.Integer, primary_key=True)
    reciever_id = db.Column(db.Integer, nullable=False)
    sender_id = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(200), nullable=False)

    def _init_(self, id, message, reciever_id, sender_id):
        self.ID = ID
        self.message = message
        self.reciever_id = reciever_id
        self.sender_id = sender_id

    def toJSON(self):
        return{
            'id': self.id,
            'message': self.message,
            'reciever_id': self.reciever_id,
            'sender_id': self.sender_id
        }