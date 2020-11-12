from flask import render_template, redirect, request, url_for
from application import app, db
from application.models import Team, Player, Picks
from application.forms import PlayerForm
#from sqlalchemy import asc, desc

@app.route('/')
@app.route('/home')
def home():
    return render_template('main.html')


@app.route('/view-teams')
def viewteams():
    return render_template('main.html')

@app.route('/add-team')
def addteam():
    return render_template('main.html')

@app.route('/update-team')
def updateteam():
    return render_template('main.html')

@app.route('/delete-team')
def deleteteam():
    return render_template('main.html')

@app.route('/view-players')
def viewplayers():
    return render_template('main.html')

@app.route('/add-player', methods=['GET','POST'])
def addplayers():
    form=PlayerForm()
    
    if form.validate_on_submit():
        new_player=Player(name=form.name.data, position=form.position.data, kills=form.kills.data, deaths=form.kills.data, assists=form.assists.data, dpm=form.dpm.data, gd10=form.gd10.data)
        db.session.add(new_player)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('addplayer.html', form=form)

@app.route('/update-player')
def updateplayer():
    return render_template('main.html')

@app.route('/delete-player')
def deleteplayer():
    return render_template('main.html')
