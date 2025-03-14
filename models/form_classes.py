from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Optional
from models.department_class import Department
from services.extension import db
from flask import current_app

class NewEmployeeForm(FlaskForm):
    name = StringField('Employee Name', validators=[DataRequired()])
    last_name = StringField('Employee last name', validators=[DataRequired()])
    dob = DateField('Employee date of birth', validators=[DataRequired()])
    position = StringField('Employee position', validators=[DataRequired()])
    salary = IntegerField('Employee Salary', validators=[DataRequired()])

    def int_or_non(value):
        if value == '':
            return None
        else:
            return int(value)

    @staticmethod
    def get_departments():
        with current_app.app_context():
            return [(dep.id, dep.name) for dep in db.session.execute(db.select(Department)).scalars().all()]

    department_id = SelectField('Department', choices=[], coerce=int_or_non, validators=[Optional()])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(NewEmployeeForm, self).__init__(*args, **kwargs)
        self.department_id.choices = [('', 'None')] + self.get_departments()
    
class UpdateEmployeeForm(FlaskForm):
    def int_or_non(value):
        if value == '':
            return None
        else:
            return int(value)
            
    position = StringField('Employee position', validators=[Optional()])
    salary = IntegerField('Employee Salary', validators=[Optional()])

    @staticmethod
    def get_departments():
        with current_app.app_context():
            return [(dep.id, dep.name) for dep in db.session.execute(db.select(Department)).scalars().all()]

    department_id = SelectField('Department', choices=[], coerce=int_or_non, validators=[Optional()])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(UpdateEmployeeForm, self).__init__(*args, **kwargs)
        self.department_id.choices = [('', 'None')] + self.get_departments()

class DeleteEmployeeForm(FlaskForm):
    submit = SubmitField('Delete')

class NewDepartmentForm(FlaskForm):
    name = StringField('Employee Name', validators=[DataRequired()])
    submit = SubmitField('Submit')