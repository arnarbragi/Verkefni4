from flask import Flask, render_template
app = Flask(__name__)

listi=[
	["Arnar Bragi","1410022280"],
	["Guðjón Atli","2210022020"],
	["Ágúst Ingi","0205003280"]
]

@app.route('/')
def index():
	return render_template("index.tpl")

@app.route('/kt')
def kt():
	return render_template("kennitala.tpl", listi=listi)

@app.route('/kt/<kt1>')
def ktSumma(kt1):
	skref=kt1[1].split()
	thver=0
	for thing in kt1:
		thver=thver+int(thing)
	return render_template("ktThver.tpl", thver=thver, kt1=kt1)

@app.errorhandler(404)
def error404(error):
	return "Síða ekki fundin", 404

if __name__ == "__main__":
	app.run(debug=True)