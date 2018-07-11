__author__ = 'xianda'

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from xianda import app
from extends import db
from models import User, Article, Message

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
