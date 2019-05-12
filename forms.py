from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateField


class RegistrationForm(FlaskForm):
    name = StringField('Full Name',
                           validators=[DataRequired(), Length(min=2, max=30)])
    age = IntegerField('Age',
                           validators=[DataRequired()])
    diagnosis = StringField('What is your diagnosis (i.e stroke etc.)?',
                         validators=[DataRequired(), Length(min=2, max=20)])
    dateofdiagnosis = DateField('What was the date of your diagnosis?' ,
                         validators=[DataRequired()], format='%d/%m/%y')
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
