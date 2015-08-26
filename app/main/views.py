from . import main
from flask import render_template, redirect, url_for
from .. import db
from ..models import Suggestion
from .forms import FeatureForm


@main.route('/')
def index():
	s = Suggestion.query.all()
	return render_template('suggestions.html', suggestions = s)

@main.route('/featureRequest/',methods=['POST','GET'])
def addSuggestion():
	form = FeatureForm()
	if form.validate_on_submit():
		s = Suggestion(user = form.user.data, content = form.Suggestion.data)
		db.session.add(s)
		db.session.commit()
		return redirect(url_for('.index'))
	return render_template('addSuggestion.html', form = form)

@main.errorhandler(Exception)
def errors(error):
	return 'From main blueprint ' + repr(error)