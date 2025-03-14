from models.department_class import Department
from services.extension import db

def create_department(name):
    new_department = Department(name=name)

    db.session.add(new_department)
    db.session.commit()

def show_departments():
    querry = db.select(Department)
    departments = db.session.execute(querry).scalars().all()
    return departments
