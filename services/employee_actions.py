from models.employee_class import Employee
from services.extension import db 

def create_employee(name, last_name, dob, position, salary, department_id):
    new_employee = Employee(name=name, last_name=last_name, dob=dob, position=position, salary=salary, department_id=department_id)

    db.session.add(new_employee)
    db.session.commit()

def show_employees():
    querry = db.select(Employee)
    employees = db.session.execute(querry).scalars().all()
    return employees

def employee_update(id, salary, position, department_id):
    querry = db.select(Employee).filter_by(id=id)
    emp = db.session.execute(querry).scalar_one_or_none()
    if salary != None:
        emp.salary = int(salary)
    if position != '':
        emp.position = position
    if department_id != None:
        emp.department_id = department_id
    db.session.commit()

def delete_employee(id):
    querry = db.select(Employee).filter_by(id=id)
    delete_emp = db.session.execute(querry).scalar_one_or_none()
    db.session.delete(delete_emp)
    db.session.commit()

