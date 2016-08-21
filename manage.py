#!/usr/bin/env python
import os
from app import create_app
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('APP_SETTINGS') or 'default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
