import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Player, Team


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True
                )
        return app
    
    def setUp(self):
        db.create_all()
        test_player=Player(name="test", position="top")
        test_team=Team(name="test")
        db.session.add(test_player)
        db.session.add(test_team)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_viewplayers_get(self):
        response = self.client.get(url_for('viewplayers'))
        self.assertEqual(response.status_code, 200)

    def test_updateplayer_get(self):
        response = self.client.get(url_for('updateplayer',playerid=1))
        self.assertEqual(response.status_code, 200)

    def test_addplayer_get(self):
        response = self.client.get(url_for('addplayer'))
        self.assertEqual(response.status_code, 200)

    def test_deleteplayer_get(self):
        response = self.client.get(url_for('deleteplayer',playerid=1))
        self.assertEqual(response.status_code,302)

    def test_viewteams_get(self):
        response = self.client.get(url_for('viewteams'))
        self.assertEqual(response.status_code, 200)

    def test_updateteam_get(self):
        response = self.client.get(url_for('updateteam',teamid=1))
        self.assertEqual(response.status_code, 200)

    def test_addteam_get(self):
        response = self.client.get(url_for('addteam'))
        self.assertEqual(response.status_code, 200)

    def test_deleteteam_get(self):
        response = self.client.get(url_for('deleteteam',teamid=1))
        self.assertEqual(response.status_code,302)
