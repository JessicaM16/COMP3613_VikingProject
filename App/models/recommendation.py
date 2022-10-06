from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Recommendation(db.Model):                              #check relationship !!!!!!!!!!!!!!!!!
    id = db.Column(db.Integer, primary_key=True)
    recipient_id = db.Column(db.Integer,nullable=False)
    letter = db.Column(db.String(200), nullable=False)

    def _init_(self, ID, Letter, recipient_id):
        self.ID = ID
        self.Letter = Letter
        self.recipient_id = recipient_id

    def toJSON(self):
        return{
            'ID': self.ID,
            'Letter': self.Letter,
            'recipient_id': self.recipient_id
        }