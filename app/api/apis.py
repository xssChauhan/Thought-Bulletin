from flask import render_template, url_for, redirect
from .. import db
from ..models import Suggestion
from . import api

@api.errorhandler(Exception)
def errors(error):
	return 'From API Blueprint :' + repr(error)
	

@api.route('/api/get/getThread/<id>')
def getThread(id):
	'''Return the thread from the ID'''

@api.route('/api/vote/<id>/<vote>')
def vote(id, vote):
	suggestion = Suggestion.query.filter_by(id = id).first()
	suggestion.votes += int(vote)
	db.session.commit()
	return redirect(url_for('main.index'))
