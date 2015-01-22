import datetime
from app import db
from sqlalchemy import asc, desc

class Tracking(db.Model):
	__tablename__ = "tracking"

	id = db.Column(db.Integer, primary_key=True)
	user_ip = db.Column(db.String(46))
	user_agent = db.Column(db.String(100))
	at_time = db.Column(db.DateTime,default=datetime.datetime.now)

	def __init__(self, user_ip, user_agent):
		self.user_ip = user_ip
		self.user_agent = user_agent

	def save(self):
		# new_user = Tracking(user_ip, user_agent=user_agent)
		db.session.add(self)
		db.session.commit()

	@staticmethod
	def list_all_users(page, LISTINGS_PER_PAGE=10):
		return Tracking.query.order_by(desc(Tracking.at_time)).paginate(page, LISTINGS_PER_PAGE, False)

	@staticmethod
	def track_user_ip(user_ip, page, LISTINGS_PER_PAGE):
		return Tracking.query.filter(Tracking.user_ip == user_ip).order_by(desc(Tracking.at_time)).paginate(page, LISTINGS_PER_PAGE,False)

	def __repr__(self):
		return '<Tracking %r>' % (self.id)