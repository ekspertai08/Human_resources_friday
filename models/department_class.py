from services.extension import db 

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    employees = db.relationship('Employee', back_populates='department', foreign_keys='Employee.department_id')

