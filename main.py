from flask import Flask, request, render_template, url_for, flash, redirect
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from wtforms_sqlalchemy.fields import QuerySelectField
from stockticker.stock_form import StockForm
from stockticker.validate_and_update import validate_and_update
from stockticker.databaseHelper import createDatabaseEntries, getTickerChoices
import requests as r
import pandas as pd

app = Flask(__name__)
api = Api(app)
	

#Setup database 

app.config['SECRET_KEY'] = 'ponja383' # Set up secret key so users cannot modify cookies n stuff
db_engine = create_engine('sqlite:///assets.db', echo=False)
meta = MetaData()

# ======== BUILDS DATABASE :::: ONLY RUN ONCE !!! ======== #
createDatabaseEntries(db_engine, meta)

@app.route("/")
def hello():
	return render_template("index.html", title="Home")


@app.route("/about")
def about():
	return render_template("about.html", title="About")
	

@app.route("/projects")
def projects():
	return render_template("projects.html", title="Projects")

@app.route("/projects/stockticker", methods=['GET', 'POST'])
def stockticker():
	form = StockForm()
	form.country.choices = ["Sweden", "USA"]
	form.ticker.choices = getTickerChoices(db_engine, form.country.data)
	if form.validate_on_submit():
		form_data = form.data
		if validate_and_update(form_data):
			flash("Added asset!")
		else:
			flash('Failed to add asset: ', 'success')
	return render_template("stockticker.html", title="Stockticker", form=form)

@app.route("/contact")
def contact():
	return render_template("contact.html", title="Contact")
	
	
if __name__ == '__main__':
	app.run(debug=True)
