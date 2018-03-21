import pandas as pd

sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S&P_500_companies')[0][0]
print(type(sp500))

sp500 = sp500[1:]
print(type(sp500))

sp500 = sp500.sort_values(inplace=True)
print(type(sp500))

sp500 = sp500.tolist()
print(type(sp500))
