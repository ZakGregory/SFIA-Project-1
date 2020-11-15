import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Player


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
        db.session.add(test_player)
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

    def test_deleteplayer_get(self):
        response = self.client.get(url_for('deleteplayer',playerid=1))
        self.assertEqual(response.status_code,405)

