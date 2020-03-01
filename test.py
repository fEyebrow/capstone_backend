import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from database.models import db_drop_and_create_all, setup_db, Movie, Actor


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        self.new_movie = {
            'title': '1919',
            'date': 1582988568437
        }

        self.new_actor = {
            'name': 'lj',
            'age': 24,
            'gender': 1
        }

        self.ExecutiveProducer = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlEwVTBOVVEzTlRjM1FrSkROVVZDUmpKQk1VSkNNekkyT0RReFFqa3dPVFJDT1RVME1UbEVSUSJ9.eyJpc3MiOiJodHRwczovL2Rldi1seGYuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlMTA3OGUwYjk3ZTI2MGU5OTlmY2JhNSIsImF1ZCI6Im1vdmllIiwiaWF0IjoxNTgzMDUzOTM2LCJleHAiOjE1ODMxNDAzMzYsImF6cCI6Ikhzb05CeDR0a0kycjBDOEk2QmVyRXg3UXY1eWJOQzdvIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSIsInB1dDphY3RvciIsInB1dDptb3ZpZSJdfQ.gbkksdS_zdwQKAKnDOKyHoYi4l7ozvcCHx5C_u9Cj9C6bw6nDLx0S1g984MIzWTASjyrEyzAlX5uO2_g74TBS-IF3RO1aXBHQxIFtFzetF04qM59copyOLqQGnKmKGZAlZaYDEjbgbIAnSSpMG9MClcKzOWHFD5sQMNin1L4kimM5U2ub2-uOP1t2OTVEfXMrRLCvnOnQrbu79c4KfcDt112D93BRv8b3kXvpgjeICAdPQmvic5TdoQthY8sFQMpbQSRX8JScbUvimIN_-SH0sekJ40zfKr3oYpmW8QXi5N5o0O_CXFZk7slN_zpYw4EqBSivrvVRIxXwK0Y-igzqw'
        self.CastingDirector = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlEwVTBOVVEzTlRjM1FrSkROVVZDUmpKQk1VSkNNekkyT0RReFFqa3dPVFJDT1RVME1UbEVSUSJ9'

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)

    def test_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)

    def test_add_movie(self):
        res = self.client().post('/movie',
                                 json=self.new_movie,
                                 headers={'Authorization': self.ExecutiveProducer})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)

    def test_add_actor(self):
        res = self.client().post('/actor',
                                 json=self.new_actor,
                                 headers={'Authorization': self.CastingDirector})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
    
    def test_put_actor(self):
        res = self.client().put('/actor/2',
                                 json=self.new_actor,
                                 headers={'Authorization': self.ExecutiveProducer})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
    
    def test_put_movie(self):
        res = self.client().put('/movie/2',
                                 json=self.new_movie,
                                 headers={'Authorization': self.ExecutiveProducer})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)

    def test_delete_actor(self):
        res = self.client().delete('/actor/1',
                                   json={},
                                   headers={'Authorization': self.ExecutiveProducer})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)

    def test_delete_movie(self):
        res = self.client().delete('/movie/1',
                                   json={},
                                   headers={'Authorization': self.ExecutiveProducer})
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)


# self.assertEqual(data['message'], 'Authorization header must start with "Bearer".')
# self.assertEqual(len(data['questions']), 10)
# self.assertIsNotNone(data['categories'])
# self.assertIsNotNone(data['currentCategory'])
# self.assertIsNotNone(data['total_questions'])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
