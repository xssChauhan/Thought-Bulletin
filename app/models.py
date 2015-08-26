from . import db


class Suggestion(db.Model):
	__tablename__ = 'suggestions'
	id = db.Column(db.Integer, primary_key = True)
	content = db.Column(db.String(300), nullable = False)
	user = db.Column(db.String(25), nullable = False)
	votes = db.Column(db.Integer, default=0)

	def __repr__(self):
		return '<Suggestion %r>' % self.content

class UserLog(db.Model):
	__tablename__ = 'userlog'
	id = db.Column(db.Integer, primary_key = True)
	dateTime = db.Column(db.DateTime, nullable = False)
	remote = db.Column(db.UnicodeText, nullable = False)
	agent = db.Column(db.String, nullable = False)
	url = db.Column(db.String, nullable = False)

	def __repr__(self):
		return '<UserLog %r>' % self.remote
