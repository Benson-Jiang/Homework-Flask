from app import myapp_obj
from flask import render_template
from app.forms import TopCities

@myapp_obj.route("/")
def home():
	title = 'Top Cities'
	name = 'Benson'
	form = TopCities()
	return render_template('home.html', title = title, name = name, form = form)

