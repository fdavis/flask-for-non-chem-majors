from app import *
from wtforms.validators import Required, Length
from wtforms import Form, TextField

class TrackingInfoForm(Form):
    user_ip = TextField('user_ip', validators=[Required(), Length(max=46, message='max 46 characters')])
    user_agent = TextField('user_agent', validators=[Length(max=46, message='max 46 characters')])