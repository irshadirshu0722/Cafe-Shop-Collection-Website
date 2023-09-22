from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,BooleanField
from wtforms.validators import  DataRequired
class AddCaffe(FlaskForm):
    name =StringField("name",[DataRequired()])
    map_url = StringField("map_url", validators=[DataRequired()])
    img_url = StringField("img_url", validators=[DataRequired()])
    place = StringField("place/Location", validators=[DataRequired()])
    seats = StringField("no.of seats", validators=[DataRequired()])
    has_toilet = BooleanField("has_toilet(True/False",[DataRequired()])
    has_wifi =BooleanField("has_toilet(True/False",[DataRequired()])
    has_sockets =BooleanField("has_toilet(True/False",[DataRequired()])
    can_take_calls =BooleanField("has_toilet(True/False",[DataRequired()])
    coffee_price =  StringField("Coffe price", validators=[DataRequired()])
    submit = SubmitField("Add Coffee")