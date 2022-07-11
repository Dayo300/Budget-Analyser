from flask import Blueprint, app, flash, redirect, render_template, request, jsonify, url_for, send_from_directory
from flask_login import login_required, current_user
from numpy import insert
from website.form import  UserDataForm, UploadForm
from .models import User, IncomeExpenses, UploadFiles
from . import DB_NAME, db
import json
import pandas as pd









views = Blueprint('views',__name__)


@views.route("/upload", methods = ["POST", "GET"])
@login_required
def upload():
    form = UploadForm()
    if request.method == "POST":
      if form.validate_on_submit():
         csvfile = form.file.data
         csvdata = pd.read_csv(csvfile)
         csvdata.to_html()

         
         #csvdata.to_sql(name='UploadFiles', con=db.engine, if_exists='append', dtype= dict(), method=None, index= True)
         #uploadfile = list(csvdata.values)
         #for row in df:
            # results.append(df(row))
        # entry = UploadFiles(csv_file, columns=['date','desc','amount','catagory'])
         print(csvdata)
         return render_template("upload.html", user=current_user, form=form, tables=[csvdata.to_html()])
    return render_template("upload.html",title="Uploads", user=current_user, form=form)



@views.route("/index")
@login_required
def index():
    entries = IncomeExpenses.query.order_by(IncomeExpenses.date.desc()).all()
    return render_template('index.html', title="Transaction History", entries = entries, user=current_user)
    
    
    
    
    


@views.route("/add", methods = ["POST", "GET"])
@login_required
def add_expenses():
    form = UserDataForm()
    if form.validate_on_submit():
        entry = IncomeExpenses(type=form.type.data, category=form.category.data, amount=form.amount.data)
        db.session.add(entry)
        db.session.commit()
        flash(f"{form.type.data} has been added to {form.type.data}s", "success")
        return redirect('index')
    return render_template('add.html', title="Add expenses",user=current_user, form=form)


@views.route('/delete/<int:entry_id>')
@login_required
def delete(entry_id):
    entry = IncomeExpenses.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('views.index', user=current_user))


@views.route('/dashboard')
@login_required
def dashboard():
    income_vs_expense = db.session.query(db.func.sum(IncomeExpenses.amount), IncomeExpenses.type).group_by(IncomeExpenses.type).order_by(IncomeExpenses.type).all()

    category_comparison = db.session.query(db.func.sum(IncomeExpenses.amount), IncomeExpenses.category).group_by(IncomeExpenses.category).order_by(IncomeExpenses.category).all()

    dates = db.session.query(db.func.sum(IncomeExpenses.amount), IncomeExpenses.date).group_by(IncomeExpenses.date).order_by(IncomeExpenses.date).all()

    income_category = []
    for amounts, _ in category_comparison:
        income_category.append(amounts)

    income_expense = []
    for total_amount, _ in income_vs_expense:
        income_expense.append(total_amount)

    over_time_expenditure = []
    dates_label = []
    for amount, date in dates:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_expenditure.append(amount)

    return render_template('dashboard.html', title="Dashboard",
                            income_vs_expense=json.dumps(income_expense),
                            income_category=json.dumps(income_category),
                            over_time_expenditure=json.dumps(over_time_expenditure),
                            dates_label =json.dumps(dates_label),user=current_user
                        )
 


