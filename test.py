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

        self.ExecutiveProducer = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlEwVTBOVVEzTlRjM1FrSkROVVZDUmpKQk1VSkNNekkyT0RReFFqa3dPVFJDT1RVME1UbEVSUSJ9.eyJpc3MiOiJodHRwczovL2Rldi1seGYuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlMTA3OGUwYjk3ZTI2MGU5OTlmY2JhNSIsImF1ZCI6Im1vdmllIiwiaWF0IjoxNTgyOTg5MTA1LCJleHAiOjE1ODMwNzU1MDUsImF6cCI6Ikhzb05CeDR0a0kycjBDOEk2QmVyRXg3UXY1eWJOQzdvIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSIsInB1dDphY3RvciIsInB1dDptb3ZpZSJdfQ.j4TWOrfE0tstmlAfi2XYsv7y00Cdv09u4VU7cP_ZAu6nUeEY3c73EyGtgonNjDkKFJHkAUnfAOMrU9Jd9UnO43-u8OasTqVPuNQwlhM1awOn_Xqc9nzSX6XcCjeORhyPVUQR0s21miio-V7uKQAOxOZQkmyXHc8gEft2zoTV8W98J7gKdMnpEWzetx2YMlFzHtjU1SQPQR0kSdR_A_CGOa9ck91BjkWFl5EApSDzW1dnxvM1dDXcNEba1sAUC7A6ubbqcS3Z_Nm17c58iE3E2SoMEzUYlz97boG0d_1EHcsP4Wdh0CKjxac0afff_mGqTDV3iC6oEyDUjvMhKksDLw'

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
                                 headers={'Authorization': self.ExecutiveProducer})
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
