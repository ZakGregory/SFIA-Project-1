from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField


class PlayerForm(FlaskForm):
    name= StringField('Player\'s In Game Name')
    position= StringField('Position')
    kills= IntegerField('Total Kills')
    deaths= IntegerField('Total Deaths')
    assists= IntegerField('Total Assists')
    dpm= IntegerField('Total Damage per Minute')
    gd10= IntegerField('Gold Differnce at 10 Min')
    submit= SubmitField('submit')

class TeamForm(FlaskForm):
    name= StringField("Team Name")
'''
class PickForm(FlaskForm):
    select=SelectField("", choices=playerlist)
'''

