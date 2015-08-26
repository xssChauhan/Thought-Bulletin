import os
from app import create_app, db
from app.models import Suggestion
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
	manager.run()