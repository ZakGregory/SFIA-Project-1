from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField

class PlayerForm(FlaskForm):
    name= StringField('Player\'s in game name')
    position= StringField('Role')
    kills= IntegerField('Total kills')
    deaths= IntegerField('Total deaths')
    assists= IntegerField('Total assists')
    dpm= IntegerField('Total damage per minute')
    gd10= IntegerField('Gold differnce at 10 min')
    submit= SubmitField('submit')
