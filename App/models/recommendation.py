from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Recommendation(db.Model):                              #check relationship !!!!!!!!!!!!!!!!!
    id = db.Column(db.Integer, primary_key=True)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    letter = db.Column(db.String(200), nullable=False)

    def _init_(self, ID, Letter, recipient_id):
        self.id = ID                                #for the rec
        self.letter = Letter                        #message itself
        self.recipient_id = recipient_id            #who it is for

    def toJSON(self):
        return{
            'ID': self.id,
            'Letter': self.letter,
            'recipient_id': self.recipient_id
        }