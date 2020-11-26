from flask import Flask, request, render_template, url_for, flash, redirect
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from wtforms_sqlalchemy.fields import QuerySelectField
from stockticker.stock_form import StockForm
from stockticker.validate_and_update import validate_and_update
import requests as r
import pandas as pd


def createDatabaseEntries(db_engine, meta):
	# Creating DB entries for American stocks
	stocks = Table(
		'stocks', meta,
		Column('symbol', String, primary_key=True),
		Column('name', String),
		Column('country', String),
	)

	crypto = Table(
		'crypto', meta,
		Column('symbol', String, primary_key=True),
		Column('name', String),
	)
	meta.create_all(db_engine)

	try: 
		print("Reading American stock information from CSV files...")
		companylistNasdaq = pd.read_csv("/home/pi/flask_webserver/stockticker/companylistNasdaq.csv")
		companylistNyse = pd.read_csv("/home/pi/flask_webserver/stockticker/companylistNyse.csv")
		companylistAmex = pd.read_csv("/home/pi/flask_webserver/stockticker/companylistAmex.csv")
		conn = db_engine.connect()
		print("Creating DB entries for Nasdaq...")
		for x in range(len(companylistNasdaq)):
			symbol = companylistNasdaq['Symbol'][x]
			# Check if current symbol already exists in DB
			query = stocks.select().where(stocks.c.symbol == symbol)
			result = conn.execute(query)
			# If the symbol does not exists -> add it 
			if result.first() is None: 
				name = companylistNasdaq['Name'][x]
				ins = stocks.insert().values(symbol = symbol, name = name, country = "USA")
				result = conn.execute(ins)
			else:
				raise Exception("Tried to add duplicate entry for " + symbol + ". Aborting database creation.")
		print("Creating DB entries for NYSE...")
		for x in range(len(companylistNyse)):
			symbol = companylistNyse['Symbol'][x]
			# Check if current symbol already exists in DB
			query = stocks.select().where(stocks.c.symbol == symbol)
			result = conn.execute(query)
			# If the symbol does not exists -> add it 
			if result.first() is None: 
				name = companylistNyse['Name'][x]
				ins = stocks.insert().values(symbol = symbol, name = name, country = "USA")
				result = conn.execute(ins)
			else:
				raise Exception("Tried to add duplicate entry for " + symbol + ". Aborting database creation.")
		print("Creating DB entries for AMEX...")
		for x in range(len(companylistAmex)):
			symbol = companylistAmex['Symbol'][x]
			# Check if current symbol already exists in DB
			query = stocks.select().where(stocks.c.symbol == symbol)
			result = conn.execute(query)
			# If the symbol does not exists -> add it 
			if result.first() is None: 
				name = companylistAmex['Name'][x]
				ins = stocks.insert().values(symbol = symbol, name = name, country = "USA")
				result = conn.execute(ins)
			else:
				raise Exception("Tried to add duplicate entry for " + symbol + ". Aborting American database creation.")
	except Exception as error:
		print(error)

	# Creating DB entires for Swedish stocks
	try:
		print("Downloading Swedish stock information CSV file...")
		site_url="http://topforeignstocks.com/listed-companies-lists/the-complete-list-of-listed-companies-in-sweden/"
		response = r.get(site_url)
		print("Downloaded CSV file. Reading CSV file...")
		df = pd.read_html(response.text)
		company_list = df[0]
		conn = db_engine.connect()
		print("Creating DB entries for OMXS...")
		for x in range(len(company_list)):
			ticker = company_list.loc[x]['Ticker'] + ".ST"
			# Check if current symbol already exists in DB
			query = stocks.select() 
			query = query.where(stocks.c.symbol == symbol)
			result = conn.execute(query)
			# If the symbol does not exists -> add it 
			if result.first() is None: 
				name = company_list.loc[x]['Company Name']
				ins = stocks.insert().values(symbol = ticker, name = name, country = "Sweden")
				result = conn.execute(ins)
			else:
				raise Exception("Tried to add duplicate entry for " + symbol + ". Aborting Swedish database creation.")
	except Exception as error: 
		print(error)
		
	
def getTickerChoices(db_engine, country):
	query = stocks.select().where(stocks.c.country == country)
	conn = db_engine.connect()
	result = conn.execute(query)
	
	tickerList = []
	for row in result:
		tickerList.append(row)
		
	return tickerList
	
