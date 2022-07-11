from ast import Sub
from asyncore import file_dispatcher
from datetime import date
from distutils.command.upload import upload
from importlib.machinery import FileFinder
from click import File
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired


class UserDataForm(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                                choices=[('income', 'income'),
                                        ('expense', 'expense')])
    category = SelectField("Category", validators=[DataRequired()],
                                            choices =[('rent'),
                                            ('investment'),
                                            ('salary'),
                                            ('side_hustle'),
                                            ('travel'),
                                            ('eating out'),
                                            ('house'),
                                            ('Groceries'),
                                            ('charity'),
                                            ('education')
                                            ]
                            )
    amount = IntegerField('Amount', validators = [DataRequired()])                                   
    submit = SubmitField('Generate Report')   



class UploadForm(FlaskForm):
    file = FileField('file',validators = [DataRequired()])
   # date = FileField('date')
    #desc = FileField('desc')
    #amount = FileField('amount')
    #catagory = FileField('catagory')
    submit = SubmitField('Upload File')