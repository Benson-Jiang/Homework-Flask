from app import myapp_obj
from flask import render_template, redirect, flash
from app.forms import TopCities

@myapp_obj.route("/", methods = ['GET', 'POST'])
def home():
	title = 'Top Cities'
	name = 'Benson'
	form = TopCities()
	if form.validate_on_submit():
		flash(f'City name: {form.city_name.data} has been added')
		return redirect("/")
	return render_template('home.html', title = title, name = name, form = form)

