from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Recommendation(db.Model):                             
    id = db.Column(db.Integer, primary_key=True)                                        # the recommendation ID
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)      # the student that recieves the recommendation (who it is for)
    sender = db.Column(db.Integer, nullable=False)                                      # the teacher that writes the recommendation (who it is from)                                      
    letter = db.Column(db.String(200), nullable=False)                                  # recommendation message content

    def _init_(self, ID, Letter, recipient_id):
        self.id = ID                            
        self.letter = letter                        
        self.recipient_id = recipient_id            
        self.sender                                 

    def toJSON(self):
        return{
            'ID': self.id,
            'Letter': self.letter,
            'recipient_id': self.recipient_id,
            'sender': self.sender
        }