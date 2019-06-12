#!/usr/bin/env python3
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app.database import db

app = create_app()
#db.create_all()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()