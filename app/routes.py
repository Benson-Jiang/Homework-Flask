from app import myapp_obj
from flask import render_template, redirect, flash
from app.forms import TopCities
from app.models import city
from app import db

@myapp_obj.route("/", methods = ['GET', 'POST'])
def home():
	title = 'Top Cities'
	name = 'Benson'
	form = TopCities()
	list = city.query.order_by(city.rank).all()
	if form.validate_on_submit():
		flash(f'City name: {form.city_name.data} has been added')
		c = city(city = form.city_name.data, rank = form.city_rank.data, visit = form.is_visited.data)
		db.session.add(c)
		db.session.commit()
		list = city.query.order_by(city.rank).all()
		return redirect("/")
	return render_template('home.html', title = title, name = name, form = form, list = list)
