from app import myapp_obj

@myapp_obj.route("/")
def hello():
	user = {'username': 'Ben'}
	return render_template('hello.html', title = 'Home', user = user)

