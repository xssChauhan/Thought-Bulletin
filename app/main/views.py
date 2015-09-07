from . import main
from flask import render_template, redirect, url_for, request
from .. import db
from ..models import Suggestion, UserLog, Content
from .forms import FeatureForm, ContentForm
from datetime import datetime






@main.route('/')
def index():
	s = Suggestion.query.all()
	cacheUser()
	return render_template('suggestions.html', suggestions = s)

@main.route('/featureRequest/',methods=['POST','GET'])
def addSuggestion():
	form = FeatureForm()
	cacheUser()
	if form.validate_on_submit():
		s = Suggestion(user = form.user.data, content = form.Suggestion.data)
		db.session.add(s)
		db.session.commit()
		return redirect(url_for('.index'))
	return render_template('addSuggestion.html', form = form)


	

@main.route('/content', methods = ['POST', 'GET'])
def content():
	form = ContentForm()
	cacheUser()
	if form.validate_on_submit():
		c = Content(url = form.link.data, user = form.user.data )
		db.session.add(c)
		db.session.commit()
		return redirect(url_for('.content'))
	c = Content.query.all()
	return render_template('content.html', content = c,form = form)

@main.errorhandler(Exception)
def errors(error):
	return 'From main blueprint ' + repr(error)


def cacheUser():
	u = UserLog(dateTime = datetime.now(),remote = request.remote_addr, agent = request.headers.get('User-Agent'), url = request.url)
	db.session.add(u)
	db.session.commit()
	return