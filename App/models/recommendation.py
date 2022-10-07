from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Recommendation(db.Model):                             
    id = db.Column(db.Integer, primary_key=True)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sender = db.Column(db.Integer, nullable=False)                                      ##check if it needs to be forieggn
    letter = db.Column(db.String(200), nullable=False)

    def _init_(self, ID, Letter, recipient_id):
        self.id = ID                                # the recommendation ID
        self.letter = letter                        # recommendation message content
        self.recipient_id = recipient_id            # the student that recieves the recommendation (who it is for)
        self.sender                                 # the teacher that writes the recommendation (who it is from)

    def toJSON(self):
        return{
            'ID': self.id,
            'Letter': self.letter,
            'recipient_id': self.recipient_id,
            'sender': self.sender
        }