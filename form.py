from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired("can't put nothin"), Email("enter a valid email address")])
    password = PasswordField(label='Password', validators=[DataRequired(message="can't put nuthin"), Length(min=8, message="password must be 8 or more characters")])
    submit = SubmitField(label="Kenny Logins")
