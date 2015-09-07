from flask import render_template, url_for, redirect, jsonify
from .. import db
from ..models import Suggestion
from . import api

@api.errorhandler(Exception)
def errors(error):
	return 'From API Blueprint :' + repr(error)
	

@api.route('/api/vote/put/<id>/<vote>')
def vote(id, vote):
	suggestion = Suggestion.query.filter_by(id = id).first()
	suggestion.votes += int(vote)
	db.session.commit()
	return redirect(url_for('main.index'))


@api.route('/api/vote/get/<id>', methods= ['GET'])
def getVotes(id):
	votes = Suggestion.query.filter_by(id = id).first()
	votes = votes.votes
	return jsonify(votes)


