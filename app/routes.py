from app import myapp_obj
from flask import render_template

@myapp_obj.route("/")
def home():
	title = 'Top Cities'
	name = 'Benson'
	return render_template('home.html', title = title, name = name)

