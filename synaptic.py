#!/usr/bin/python3

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
#from flask import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']= '50eb51cfa4098f26588f83086fa28229'



#app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://localhost/synaptic_db'
#db = SQLAlchemy(app)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/Home')
def index():
    return render_template('index.html')

@app.route('/CommunityServices')
def community():
    return render_template('communityservices.html')

@app.route('/WheelchairVendors')
def wheelchair():
    return render_template('wheelchairvendors.html')

@app.route('/MedicalVendors')
def medical():
    return render_template('medicalvendors.html')

@app.route('/HomeCareServices')
def homeservices():
    return render_template('homeservices.html')

@app.route('/Research')
def research():
    return render_template('research.html')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run()