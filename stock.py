import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib
import numpy as np


def graph_data(stock):
  print("Currently pulling: ", stock)
  # # url = "http://chartapi.finance.yahoo.com/instrument/1.0/"+stock+"/chartdata;type=quote;range=10y/csv"
  # url = 'https://finance.yahoo.com/quote/' + stock + '/history/csv'
  url = 'https://www.quandl.com/api/v3/datasets/WIKI/'+stock+'/data.csv'
  print(url)


stock = input("Stock to plot: ")
graph_data(stock)