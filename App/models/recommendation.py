from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Recommendation(db.Model):                              #check relationship !!!!!!!!!!!!!!!!!
    id = db.Column(db.Integer, primary_key=True)
    #studentID = db.Column(db.Integer, db.ForeignKey('Student.ID'), nullable=False)
    #staffID = db.Column(db.Integer, db.ForeignKey('Staff.ID'), nullable=False)
    letter = db.Column(db.String(200), nullable=False)

    def _init_(self, ID, Letter, StudentID, StaffID):
        self.ID = ID
        #self.StudentID = StudentID
       # self.StaffID = StaffID
        self.Letter = Letter

    def toJSON(self):
        return{
            'ID': self.ID,
            #'StudentID': self.StudentID,
           # 'StaffID': self.StaffID,
            'Letter': self.Letter
        }