import pandas_datareader.data as web
import datetime as dt
import matplotlib.dates as mdates
from datetime import timedelta
from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np
#from pandas_datareader._utils import RemoteDataError
#from datetime import datetime


STOCKS = {
    "INVE-B.ST": 0,
    "KINV-B.ST": 0,
    "CLA-B.ST": 0,
    "LATO-B.ST": 0,
    "LUNE.ST": 0,
    "MEKO.ST": 0,
    "TIGO-SDB.ST": 0,
    "RROS.ST": 0,
    "STWK.ST": 0,
    "BLK": 0,
    "MSFT": 0,
    "OHI": 0,
    "NDA-FI.HE": 0
}

#
#def update_price_info():
#    for ticker in STOCKS:
#        try:
#            STOCKS[ticker] = web.DataReader(ticker, 'yahoo', start, end)
#            filename = ticker
#            filename += '.csv'
#            my_file = open(filename, "w")
#            with my_file:
#                writer = csv.writer(my_file, delimiter="\t")
#                my_data = STOCKS[ticker]
#                writer.writerow(my_data['Adj Close'].astype(float))
#        except:
#            print("Failed to update values for " + ticker)


#def fetch_price_info():

#    for ticker in STOCKS:
#        filename = ticker
#        filename += '.csv'
#        try:
#            with open(filename) as my_file:
#                results = []
#                reader = csv.reader(my_file, delimiter="\t")
#                for line in reader:
#                    results.append(line)
#
#        except:
#            print("Failed to fetch info for " + ticker)


#def update_total():
#    totals = {
#        "INVE-B.ST": [],
#        "KINV-B.ST": [],
#        "CLA-B.ST": [],
#        "LATO-B.ST": [],
#        "LUNE.ST": [],
#        "MEKO.ST": [],
#        "TIGO-SDB.ST": [],
#        "RROS.ST": [],
#        "STWK.ST": [],
#        "BLK": [],
#        "MSFT": [],
#        "OHI": [],
#        "NDA-FI.HE": []
#    }
#    with open("C:/Users/p0nt/PycharmProjects/stockticker/pos.csv", "r") as quant_file:
#        quant_reader = csv.reader(quant_file, delimiter="\t")
#        quant = []
#        for line in quant_reader:
#            quant.append(line)
#        curr = 0
#        for ticker in STOCKS:
#            filename = ticker
#            filename += '.csv'
#            with open(filename) as ticker_file:
#                ticker_reader = csv.reader(ticker_file, delimiter="\t")

#                for line in ticker_reader:
#                    for i in line:
#                        total = float(i) * int(quant[0][curr])
#                        totals[ticker].append(total)

#            curr += 1
#    return totals


#def plot_graphs(totals):
#    total_for_each = [0 for i in range(len(totals["INVE-B.ST"]))]

#    for curr in totals:
        total_index = 0
#        try:
#            for daily_price in totals[curr]:
#                total_for_each[total_index] += daily_price
#                total_index += 1
#        except:
#            print(total_index)

#    end = date.today()
#    start = end - timedelta(days=len(total_for_each))
#    days = mdates.drange(start, end, dt.timedelta(days=1))
#    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
#    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=int((len(total_for_each)/5))))
#    plt.plot(days, total_for_each)
#    plt.gcf().autofmt_xdate()
#    plt.show()

#end = date.today()
#start = end - timedelta(days=365)
#update_price_info()
#fetch_price_info()
#totals = update_total()
#plot_graphs(totals)
