from . import db


class Suggestion(db.Model):
	__tablename__ = 'suggestions'
	id = db.Column(db.Integer, primary_key = True)
	content = db.Column(db.String(300), nullable = False)
	user = db.Column(db.String(25), nullable = False)
	votes = db.Column(db.Integer, default=0)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

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

class Content(db.Model):
	__tablename__ = 'content'
	id = db.Column(db.Integer, primary_key= True)
	url = db.Column(db.String , nullable = False)
	user = db.Column(db.String, default = '')
	def __repr__(self):
		return '<content %r>' % self.url

	'''To-do
	1. Add a content field where the content of the url can be cached'''

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String, nullable= False)
	polls = db.relationship('Suggestion', backref ='poll' )