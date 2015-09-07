from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required, Length

class FeatureForm(Form):
	user = StringField('What is your name?', validators = [Required(), Length(1,25)])
	Suggestion = TextAreaField('Suggestion', validators = [Length(1,300)])
	submit = SubmitField('Submit')

class ContentForm(Form):
	link = StringField('Enter the link here', validators = [Required()])
	user = StringField('What is your username', validators = [Required(), Length(1,25)])
	submit = SubmitField('Submit')