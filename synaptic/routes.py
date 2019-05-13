from flask import render_template, url_for, flash, redirect
from synaptic import app, db, bcrypt
from synaptic.forms import RegistrationForm, LoginForm
from synaptic.models import User

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

@app.route('/MedicalTerminology')
def medterms():
    return render_template('medicalterms.html')

@app.route('/Stroke')
def stroke():
    return render_template('stroke.html')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, age=form.age.data, diagnosis=form.diagnosis.data, dateofdiagnosis=form.dateofdiagnosis.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
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
