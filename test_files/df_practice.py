import pandas as pd

dict1 = {'paul' : [1, 2, 3, 4],
	'billy' : [5, 6, 7, 8]
	}

df = pd.DataFrame()
print(df)
df2 = pd.DataFrame(dict1)
print(df2) 
df.join(df2)
print(df)
