from flask import render_template, request, flash, redirect, url_for
from models import *
from forms import *
from app import *
import logging

# from flask.ext.admin import Admin, BaseView, expose
# from flask.ext.admin.contrib.sqla import ModelView

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

@app.route('/track', methods=['GET', 'POST'])
@app.route('/track/<user_ip>', methods=['GET', 'POST'])
@app.route('/track/<user_ip>/<int:page>', methods=['GET', 'POST'])
def track_user_ip(user_ip="", page = 1):
	Tracking(request.remote_addr, request.headers.get('User-Agent')).save()

	form = TrackingForm(request.form)
	if request.method == 'POST':
		if form.validate():
			user_ip = form.user_ip.data

	list_records = Tracking.track_user_ip(user_ip, page, app.config['LISTINGS_PER_PAGE'])
	return render_template("track.html", form=form, user_ip=user_ip, list_records=list_records, page=page, num_paginated=app.config['LISTINGS_PER_PAGE'])

@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
	form = TrackingInfoForm(request.form)
	if request.method == 'POST':
		if form.validate():
			new_tracking = Tracking()
			user_ip = form.user_ip.data
			user_agent = form.user_agent.data
			logging.info("adding " + user_ip + " " + user_agent)
			new_tracking.set_data(user_ip, user_agent)
			flash("added successfully", category = "succses")
	return render_template("add_record.html", form = form)
