from services.extension import db 
import datetime

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    dob = db.Column(db.Date)
    position = db.Column(db.String(50))
    salary = db.Column(db.Integer)
    works_from = db.Column(db.Date, default=datetime.date.today())
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id", use_alter=True), nullable=True)

    department = db.relationship('Department', back_populates='employees', foreign_keys=[department_id])
