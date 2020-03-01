from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from database.models import db_drop_and_create_all, setup_db, Movie, Actor, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
