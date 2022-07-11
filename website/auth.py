from distutils.log import error
from flask import Blueprint, flash, render_template, request, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user





auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.dashboard'))
            else:
                flash('password incorrect!')
        
    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/')
@auth.route('/sign-up', methods= ['GET','POST'])
def sign_up():
    if request.method =='POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        

     #add user to database
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        return redirect(url_for('views.dashboard'))
    return render_template("sign_up.html", user=current_user)

    