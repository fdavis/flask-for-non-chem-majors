from flask import render_template, request
from models import *
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
from app import *
import logging

@app.before_first_request
def before_first_request():
	logging.info("------------initializing everything ----------------")
	db.create_all()

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page=1):
	Tracking(request.remote_addr, request.headers.get('User-Agent')).save()
	list_records = Tracking.list_all_users(page, app.config['LISTINGS_PER_PAGE'])
	# for record in list_records:
	# 	logging.info(record.user_ip + " " + record.user_agent)
	return render_template("index.html", list_records=list_records, page=page, num_paginated=app.config['LISTINGS_PER_PAGE'])

@app.route('/track/<user_ip>')
@app.route('/track/<user_ip>/<int:page>')
def track_user_ip(user_ip="", page = 1):
	Tracking(request.remote_addr, request.headers.get('User-Agent')).save()
	list_records = Tracking.track_user_ip(user_ip, page, app.config['LISTINGS_PER_PAGE'])
	return render_template("track.html", user_ip=user_ip, list_records=list_records, page=page, num_paginated=app.config['LISTINGS_PER_PAGE'])