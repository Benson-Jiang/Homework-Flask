from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField

class TopCities(FlaskForm):
	city_name = StringField("City Name", validator = [DataRequired()])
	city_rank = IntegerField("City Rank", validator = [DataRequired()])
	is_visited = BooleanField("Visited")
	submit = SubmitField("Submit")

