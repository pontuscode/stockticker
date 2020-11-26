import numpy as np
import pandas_datareader.data as web
import datetime as dt
#import matplotlib.dates as mdates
from datetime import timedelta
from datetime import date
#import matplotlib.pyplot as plt
#import pandas as pd
#import csv
#import numpy as np

def validate_and_update(form):
	
	# Determine deltatime
	end = date.today()
	#print(end)
	#print(form['datePurchased'])

	delta = end - form['datePurchased']
	start = end - timedelta(delta.days)
	#print(start)
	
	# We need to know what type of asset the user added:
	if(form['assetType'] == 'stock'):
		ticker = form['ticker']
		if(form['country'] == "Sweden"):
			ticker = ticker + ".ST"
		assetInfo = web.DataReader(ticker, 'yahoo', start, end)
		print(assetInfo['Adj Close'])
	elif(form['assetType'] == 'crypto'):
		print("crypto")
	elif(form['assetType'] == 'bond'):
		print("bond")
	elif(form['assetType'] == 'material'):
		print("material")
	else:
		print("Something went wrong when determining asset type")
		return False
	
	return True
