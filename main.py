from flask import Flask, request, url_for , render_template, redirect
from googleurl import genlinks
import pyjokes
app = Flask(__name__)


@app.route("/search/<query>")
def GetQuery(query=None):
	q = request.args.get('q')
	links = genlinks(query)
	return render_template('search.html', query=query, links=links)
@app.route("/custom")
@app.route("/custom/<instruction>")
def GenQuote():
	myjoke = pyjokes.get_joke(language="en", category="neutral")
	return render_template("custom.html", myjoke=myjoke)

@app.route("/" , methods = ["GET","POST"])
def main():
	if request.method == "POST":
		query = request.form["query"]
		if "!g" in query:
			return redirect(url_for("GenQuote"))
		return redirect(url_for("GetQuery", query=query))

	else:
		return render_template("index.html")