from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Notification(db.Model):                             
    id = db.Column(db.Integer, primary_key=True)
    #studentID = db.Column(db.Integer, db.ForeignKey('Student.ID'), nullable=False)
    #staffID = db.Column(db.Integer, db.ForeignKey('Staff.ID'), nullable=False)
    message = db.Column(db.String(200), nullable=False)

    def _init_(self, id, message, StudentID, StaffID):
        self.ID = ID
        self.StudentID = StudentID
        self.StaffID = StaffID
        self.message = message

    def toJSON(self):
        return{
            'id': self.id,
            'studentID': self.studentID,
            'staffID': self.staffID,
            'message': self.message
        }