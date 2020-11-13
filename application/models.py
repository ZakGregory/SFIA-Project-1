from application import db

class Team(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    score=db.Column(db.Integer, default=0)

class Player(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    position=db.Column(db.String(7), nullable=False)
    kills=db.Column(db.Integer, default=0)
    deaths=db.Column(db.Integer, default=0)
    assists=db.Column(db.Integer, default=0)
    dpm=db.Column(db.Integer, default=0)
    gd10=db.Column(db.Integer, default=0)
    score=db.Column(db.Integer, default=0)

class Picks(db.Model):
    pick_id=db.Column(db.Integer, primary_key=True)
    team_id=db.Column('team_id',db.Integer, db.ForeignKey('team.id'))
    player_id=db.Column('player_id',db.Integer, db.ForeignKey('player.id'))

