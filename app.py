from flask import Flask, render_template, request, flash
import models.department_class
from models.employee_class import Employee
from models.form_classes import NewEmployeeForm, NewDepartmentForm, UpdateEmployeeForm, DeleteEmployeeForm
from flask_migrate import Migrate
import services.employee_actions as ser_emp
import services.department_actions as ser_dep
from services.extension import db 

app = Flask(__name__, static_folder='statics')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:PhQfXWYyrjFIAZPyvwIKKIcQXaEyrmFA@ballast.proxy.rlwy.net:45738/railway'
app.config['SECRET_KEY'] = '123'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view():
    return render_template('view.html', employees=ser_emp.show_employees(), departments=ser_dep.show_departments())

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = NewEmployeeForm()
    if form.validate_on_submit():
        name = form.name.data
        last_name = form.last_name.data
        dob = form.dob.data
        position = form.position.data
        salary = form.salary.data
        department_id = form.department_id.data
        submit = form.submit

        ser_emp.create_employee(name, last_name, dob, position, salary, department_id)
        flash('New employee successfully created!', 'success')
        return render_template('view.html', employees=ser_emp.show_employees(), departments=ser_dep.show_departments())
    
    return render_template('create.html', form=form)

@app.route('/update/<int:employee_id>', methods=['GET', 'POST'])
def update(employee_id):
    form = UpdateEmployeeForm()
    if form.validate_on_submit():
        position = form.position.data
        salary = form.salary.data
        department_id = form.department_id.data
        submit = form.submit
        ser_emp.employee_update(employee_id, salary, position, department_id)
        flash('Employee successfully updated!', 'success')
        return render_template('view.html', employees=ser_emp.show_employees(), departments=ser_dep.show_departments())

    return render_template('update.html', form=form)

@app.route('/delete/<int:employee_id>', methods=['GET', 'POST'])
def delete_emp(employee_id):
    form = DeleteEmployeeForm()
    if form.validate_on_submit():
        ser_emp.delete_employee(employee_id)
        flash('Employee successfully deleted!', 'success')
        return render_template('view.html', employees=ser_emp.show_employees(), departments=ser_dep.show_departments())
    return render_template('delete.html', form=form, employee=db.session.execute(db.select(Employee).filter_by(id=employee_id)).scalar_one())


@app.route('/create_department', methods=['GET', 'POST'])
def create_department():
    form = NewDepartmentForm()
    if form.validate_on_submit():
        name = form.name.data
        submit = form.submit
        ser_dep.create_department(name)
        flash('New department successfully created!', 'success')
        return render_template('view.html', employees=ser_emp.show_employees(), departments=ser_dep.show_departments())
    return render_template('create_department.html', form=form)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)