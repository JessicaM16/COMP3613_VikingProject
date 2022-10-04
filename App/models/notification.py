from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Notification(db.Model):                             
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200), nullable=False)

    def _init_(self, id, message, StudentID, StaffID):
        self.ID = ID
        self.message = message

    def toJSON(self):
        return{
            'id': self.id,
            'message': self.message
        }