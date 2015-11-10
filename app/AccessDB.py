'''Access Databases from within the app'''
from models import Suggestion, UserLog, Content, User


class AccessDb():
	correctContexts = ['first', 'all']
	def getDatafromDB(self, from, context = all):

		if from and _correctContext(context):
			data = from.query.context()

