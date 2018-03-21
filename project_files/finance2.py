import datetime as dt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
from bs4 import BeautifulSoup
import sklearn
style.use('ggplot')

start = dt.datetime(2017,1,1)
end = dt.datetime(2018, 2, 20)

df = web.DataReader('EXEL', 'yahoo', start, end)
df = df.round(2)
head = df.head()
print(head)
prices = df['Adj Close']
prices.to_csv('DVAX_prices.txt')

pct_returns = np.ones((len(prices)-1,1))
for i in range(len(pct_returns)):
	x = round(((prices[i+1] - prices[i]) / prices[i]),3)
	pct_returns[i] = x

cutoff_input = 2.5
cutoff = round(cutoff_input * pct_returns.std(),3)

pct_returns = pct_returns.tolist()
pct_returns = list([pct_returns[i][0] for i in  range(len(pct_returns))])

pct_returns_scrubbed = []
scrubbed_values = []
for i in pct_returns:
	if abs(i) <= cutoff:
		pct_returns_scrubbed.append(i)
	else:
		scrubbed_values.append(i)

#number of business days in the sample
days_raw_sample = len(pct_returns)
days_scrubbed_sample = len(pct_returns_scrubbed)

#scrubbing metrics
number_scrubbed = len(pct_returns) - len(pct_returns_scrubbed)
pct_days_scrubbed = round(number_scrubbed/days_raw_sample, 3)

#volatility calculations
volatility_raw = round(np.array(pct_returns).std()*16,3)
volatility_scrubbed = round(np.array(pct_returns_scrubbed).std()*16,3)

#print statements
print("Scrubbing Cutoff (abs pct move): " + 
	str(round(cutoff*100,3))
	)

print(str(number_scrubbed) + 
	" days were scrubbed; " + 
	str(round(pct_days_scrubbed, 3)*100) + 
	"% of days in the time period"
	)

print("historical volatility:: raw: " 
	+ str(round(volatility_raw*100,3)) + "; scrubbed:" +
	str(round(volatility_scrubbed*100, 3))
	)

print("scrubbed moves: ")
print(scrubbed_values)
	
min_return = min(pct_returns)
max_return = max(pct_returns)
min_return_index = np.argmin(pct_returns)+1
max_return_index = np.argmax(pct_returns)+1

#print(df.iloc[min_return_index])
#print(df.iloc[max_return_index])
#print(df)
#print(prices)
#print(pct_returns)

#text_file = open(r'output_file.txt', 'w')
#text_file.write(data)
#text_file.close()

