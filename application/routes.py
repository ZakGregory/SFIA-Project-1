from flask import render_template, redirect, request, url_for
from application import app, db
from application.models import Team, Player, Picks
from application.forms import PlayerForm
#from sqlalchemy import asc, desc

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


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
    all_players=Player.query.all()
    return render_template('viewplayers.html', all_players=all_players)

@app.route('/add-player', methods=['GET','POST'])
def addplayer():
    form=PlayerForm()
    
    if form.validate_on_submit():
        new_player=Player(name=form.name.data, position=form.position.data, kills=form.kills.data, deaths=form.deaths.data, assists=form.assists.data, dpm=form.dpm.data, gd10=form.gd10.data)
        db.session.add(new_player)
        db.session.commit()
        return redirect(url_for('viewplayers'))
    return render_template('addplayer.html', form=form)

@app.route('/update-player/<playerid>', methods=['GET','POST'])
def updateplayer(playerid):
    form = PlayerForm()
    player_to_update = Player.query.get(playerid)

    if form.validate_on_submit():
        player_to_update.name=form.name.data
        player_to_update.position=form.position.data
        player_to_update.kills=form.kills.data
        player_to_update.deaths=form.deaths.data
        player_to_update.assists=form.assists.data
        player_to_update.dpm=form.dpm.data
        player_to_update.gd10=form.gd10.data
        db.session.commit()
        return redirect(url_for('viewplayers'))
    return render_template('addplayer.html', form=form)

    return render_template('main.html')

@app.route('/delete-player/<playerid>')
def deleteplayer(playerid):
    player_to_delete = Player.query.get(playerid)
    db.session.delete(player_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
