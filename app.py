import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from database.models import db_drop_and_create_all, setup_db, Movie, Actor, db
from auth.auth import AuthError, requires_auth
from datetime import datetime


def create_app():
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # ROUTES

    @app.route('/movies', methods=['GET'])
    def drinks():
        movies = Movie.query.all()
        longMovies = [movie.long() for movie in movies]

        return jsonify({
            'success': True,
            'data': longMovies
        })

    @app.route('/actors', methods=['GET'])
    def actors():
        actors = Actor.query.all()
        longActors = [actor.long() for actor in actors]

        return jsonify({
            'success': True,
            'data': longActors
        })

    @app.route('/movie', methods=['POST'])
    @requires_auth('post:movie')
    def create_movie(payload):
        print('payload', payload)

        body = request.get_json()
        req_title = body.get('title')
        req_date = datetime.fromtimestamp(body.get('date')/1000.0)
        movie = Movie(title=req_title, date=req_date)
        movie.insert()

        return jsonify({
            'success': True,
            'movie': movie.long()
        })

    @app.route('/actor', methods=['POST'])
    @requires_auth('post:actor')
    def create_actor(payload):
        print('payload', payload)

        body = request.get_json()
        req_name = body.get('name')
        req_age = body.get('age')
        req_gender = body.get('gender')

        actor = Actor(name=req_name, age=req_age, gender=req_gender)
        actor.insert()

        return jsonify({
            'success': True,
            'movie': actor.long()
        })

    @app.route('/movie/<int:movie_id>', methods=['PUT'])
    @requires_auth('put:movie')
    def put_movie(payload, movie_id):
        if not movie_id:
            abort(404)

        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)

        body = request.get_json()
        req_title = body.get('title')
        req_date = datetime.fromtimestamp(body.get('date')/1000.0)

        movie.title = req_title
        movie.date = req_date
        movie.update()

        return jsonify({
            'success': True,
            'movie': movie.long()
        })

    @app.route('/actor/<int:actor_id>', methods=['PUT'])
    @requires_auth('put:actor')
    def put_actor(payload, actor_id):
        if not actor_id:
            abort(404)

        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)

        body = request.get_json()
        req_name = body.get('name')
        req_age = body.get('age')
        req_gender = body.get('gender')

        actor.name = req_name
        actor.age = req_age
        actor.gender = req_gender
        actor.update()

        return jsonify({
            'success': True,
            'movie': actor.long()
        })

    @app.route('/movie/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(payload, movie_id):
        if not movie_id:
            abort(404)

        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)

        movie.delete()

        return jsonify({
            'success': True,
            'movie': movie.long()
        })

    @app.route('/actor/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload, actor_id):
        if not actor_id:
            abort(404)

        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)

        actor.delete()
        return jsonify({
            'success': True,
            'actor': actor.long()
        })

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_find(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(401)
    def not_auth(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": error.description
        }), 401

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": 'bad request.'
        }), 400

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": 'Forbidden.'
        }), 403

    @app.errorhandler(AuthError)
    def autherror_handler(e):
        return jsonify({
            "message": e.error['description']
        }), e.status_code

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
