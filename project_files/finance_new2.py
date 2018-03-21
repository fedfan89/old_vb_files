import datetime as dt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import pickle
from bs4 import BeautifulSoup
import sklearn
style.use('ggplot')

#--------------------------------------------------------------------#
# the functions in this module are web scraping functions
#	pull S&P 500 symbols from Wikipedia
#		get_sp500_symbols_from_wiki()	

#	get historical data for a single stock from Yahoo Finance
#		get_prices(symbol, start, end)

#	get historical data for multiple stocks from Yahoo Finance
#		make_price_table(symbols,start,end)

#	make pickle file for stock prices for a single symbol
#		pickle_prices(symbol, start, end)
#--------------------------------------------------------------------#

#pull S&P 500 symbols from Wikipedia
def get_sp500_symbols_from_wiki():
	#pull symbols from Wikipedia table
	sp500_symbols = pd.read_html('https://en.wikipedia.org/wiki/List_of_S&P_500_companies')[0][0][1:].reset_index(drop=True)

	#save to csv
	sp500_symbols.to_csv('sp500_symbols.csv')

	#save to pickle
	pickle_file = open('sp500_symbols.pkl', 'wb')
	pickle.dump(sp500_symbols, pickle_file, pickle.HIGHEST_PROTOCOL)
	pickle_file.close()

	return sp500_symbols
	

#function to get prices from Yahoo's website for one symbol
def get_prices(symbol, start, end):
	count = 1
	while count < 10:
		try:
			df = web.DataReader(symbol, 'yahoo', start, end).round(2)
		except Exception:
			count = count + 1
			if count == 9:
				print(str(symbol) + ' failed the query')
				failed_symbols.append(symbol)
			else:
				pass
			continue
		else:
			break
	
	print(count)
	yahoo_query_count.append(count)

	if count < 10:
		prices = pd.DataFrame(df['Adj Close'])
		prices = prices.rename(columns = {'Adj Close' : symbol})
		return(prices)
	else:
		return

#function to get prices from Yahoo's website for multiple symbols
def make_price_table(symbols, start = dt.datetime(2016,1,1), end = dt.datetime.today(), name = 'default_price_table'):
	yahoo_query_count = []
	failed_symbols = []
	price_table = get_prices(symbols[0], start, end)
	for symbol in symbols[1:]:
		try:
			price_table = price_table.join(get_prices(symbol, start, end))
		except Exception:
			pass
		else:
			pass
	print(price_table)
	print(yahoo_query_count)
	print(failed_symbols)
	
	#save price table and query details to csv file
	price_table.to_csv(name)
	yahoo_query_count.to_csv(str(name) + '_query_count.csv')
	failed_symbols.to_csv(str(name) + '_failed_symbols.csv')

	#save price table to pickle file
	pickle_file = open(str(name) + '_price_table.pkl', 'wb')
	pickle.dump(price_table, pickle_file, pickle.HIGHEST_PROTOCOL)
	pickle_file.close()

	return(price_table)

#function to download stock prices to pickle file using Yahoo's website
def pickle_prices(symbol, start, end):
	df = web.DataReader(symbol, 'yahoo', start, end).round(2)
	prices = df['Adj Close']
	pickle_file = open(str(symbol) + '_pickle_file.pkl', 'wb')
	pickle.dump(prices, pickle_file, pickle.HIGHEST_PROTOCOL)
	pickle_file.close()

#--------------------------------------------#
#This is code to execute queries using the functions above

#we can make a new price table using a (list of symbols, start, end) or we can use a previously downloaded pickle file

#symbols= ['ALNY', 'SRPT', 'EXEL', 'MRNS', 'CRBP', 'BMRN', 'NBIX']
#get_sp500_symbols_from_wiki()
#symbols = pickle.load(open('sp500_symbols.pkl', 'rb'))
#start = dt.datetime(2016,2,1)
#end = dt.datetime.today()

make_price_table(symbols, start, end)

historical_price_table = pickle.load(open('sp500_price_table.pkl', 'rb'))
print(historical_price_table)

#Code to get prices for individual symbols
#alny = get_prices('ALNY', start, end)
#srpt = get_prices('SRPT', start, end)
#combined = alny.join(srpt)
#print(combined)

#pickle stock prices
#pickle_prices(symbol, start, end)

#get stock prices from pickle file
#pickle_file = open(str(symbol) + '_pickle_file.pkl', 'rb')
#prices = pickle.load(pickle_file)

#get stock prices from Yahoo website	
#get_prices(symbol, start, end)
#prices = get_prices(symbol, start, end)
#
#pct_returns = np.ones((len(prices)-1,1))
#for i in range(len(pct_returns)):
#	x = round(((prices[i+1] - prices[i]) / prices[i]),3)
#	pct_returns[i] = x
#
#cutoff_input = 2.5
#cutoff = round(cutoff_input * pct_returns.std(),3)
#
#pct_returns = pct_returns.tolist()
#pct_returns = list([pct_returns[i][0] for i in  range(len(pct_returns))])
#
#pct_returns_scrubbed = []
#scrubbed_values = []
#for i in pct_returns:
#	if abs(i) <= cutoff:
#		pct_returns_scrubbed.append(i)
#	else:
#		scrubbed_values.append(i)
#
##number of business days in the sample
#days_raw_sample = len(pct_returns)
#days_scrubbed_sample = len(pct_returns_scrubbed)
#
##scrubbing metrics
#number_scrubbed = len(pct_returns) - len(pct_returns_scrubbed)
#pct_days_scrubbed = round(number_scrubbed/days_raw_sample, 3)
#
##volatility calculations
#volatility_raw = round(np.array(pct_returns).std()*16,3)
#volatility_scrubbed = round(np.array(pct_returns_scrubbed).std()*16,3)
#
##print statements
#print("Scrubbing Cutoff (abs pct move): " + 
#	str(round(cutoff*100,3))
#	)
#
#print(str(number_scrubbed) + 
#	" days were scrubbed; " + 
#	str(round(pct_days_scrubbed, 3)*100) + 
#	"% of days in the time period"
#	)
#
#print("historical volatility:: raw: " 
#	+ str(round(volatility_raw*100,3)) + "; scrubbed:" +
#	str(round(volatility_scrubbed*100, 3))
#	)
#
#print("scrubbed moves: ")
#print(scrubbed_values)
#	
#min_return = min(pct_returns)
#max_return = max(pct_returns)
#min_return_index = np.argmin(pct_returns)+1
#max_return_index = np.argmax(pct_returns)+1
#
##print(df.iloc[min_return_index])
##print(df.iloc[max_return_index])
##print(df)
##print(prices)
##print(pct_returns)
#
##text_file = open(r'output_file.txt', 'w')
##text_file.write(data)
##text_file.close()
#
