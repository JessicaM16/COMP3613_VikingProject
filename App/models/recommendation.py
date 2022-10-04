from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Recommendation(db.Model):                              #check relationship !!!!!!!!!!!!!!!!!
    id = db.Column(db.Integer, primary_key=True)
    letter = db.Column(db.String(200), nullable=False)

    def _init_(self, ID, Letter, StudentID, StaffID):
        self.ID = ID
        self.Letter = Letter

    def toJSON(self):
        return{
            'ID': self.ID,
            'Letter': self.Letter
        }