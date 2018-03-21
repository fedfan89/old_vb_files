import pandas as pd
import pickle
import numpy as np
import datetime as dt

price_table = pickle.load(open('sp500_price_table.pkl','rb'))
price_table = price_table[['ZBH', 'ZTS', 'PFE']].tail(10)
corr_table = price_table.corr().round(2)
class Df_Ops():
        def __init__(self, df):
            self.df = df
            self.columns = self.df.columns.values.tolist()
            self.rows = self.df.index.tolist()  #is there a better name than rows for elements of the index?

        def df_to_dict(self):
            self.df_dict = {}
            for column in self.columns:
                    self.df_dict[column] = self.df[column].tolist()
            return(self.df_dict)

        def scalar_mult(self, scalar=2):
                return(self.df*scalar)

        def cc_moves_df(self): # for first row, the cc_move defaults to 0.0%
            self.df_dict = Df_Ops(self.df).df_to_dict()
            self.cc_moves_dict = {}
            for column in self.columns:
                cc_moves_row_values = [0]  #default first row to 0.0%
                for i in range(1, len(self.rows)):
                    cc_moves_row_values += [(self.df_dict[column][i] / self.df_dict[column][i-1]) - 1]
                self.cc_moves_dict[column] = cc_moves_row_values
            self.cc_moves = pd.DataFrame(self.cc_moves_dict)
            print(self.cc_moves)
            return(self.cc_moves_dict)

        def hist_vol(self):
            self.df_dict = Df_Ops(self.df).df_to_dict()
            hist_vol_dict = {}
            for column in self.columns:
                hist_vol_dict[column] = pd.Series(self.df_dict[column]).std
            self.hist_vols = pd.DataFrame(hist_vol_dict, index=[0])
            print(self.hist_vols)
            return(self.hist_vols)

Df_Ops(price_table).hist_vol()

class PT_Operations():	
        def __init__(self, df):
            print('Your table is created')
            self.df = df
            self.columns = self.df.columns.values.tolist()
            self.rows = self.df.index.tolist()

        def mult_by_2(self):
            self.mult_by_2 = self.df*2
            return(self.mult_by_2)
    
        def cc_moves_function(self):
            self.prices_as_dict = {}
            for column in self.columns:
                    values = []
                    for row in self.rows:
                            values = values + [(self.df[column][row])]
                    self.prices_as_dict[column] = values
           
            self.prices_as_dict = Df_Ops(self.df).to_dict()
            dict2 = {}
            for symbol in self.prices_as_dict:
                    new_symbol = [0.00001]
                    for i in range(1,len(self.prices_as_dict[symbol])):
                            try:
                                    cc_change = (self.prices_as_dict[symbol][i] - self.prices_as_dict[symbol][i-1]) / self.prices_as_dict[symbol][i]
                                    new_symbol = new_symbol + [cc_change]
                            except Exception:
                                    print("There was an error when calculating cc_moves")
                                    cc_change = 0
                                    new_symbol = new_symbol + [cc_change]
                            else:
                                    pass
                    dict2[symbol] = new_symbol

            df = pd.DataFrame(dict2).round(3)
            return(df)

        def cc_moves_scrubbed(self):
            self.cc_moves_scrubbed_as_dict = {}
            for column in self.columns:
                    for i in range(len(self.columns)):
                            cc_moves_after_scrubbing = []
                            if abs((self.cc_moves)[column][i]) < ((self.cc_moves)[column]).std():
                                cc_moves_after_scrubbing += (self.cc_moves)[column][i]
                            else:
                                    print("We scrubbed a move", column, self.cc_moves[column][i])
                            self.cc_moves_scrubbed_as_dict[column] = cc_moves_after_scrubbing
            df = pd.DataFrame(self.cc_moves_scrubbed_as_dict).round(3)
            print(df)
            return(df)

        def hist_vol(self):
            dict1 = {}
            i = 0
            for symbol in self.columns:
                dict1[symbol] = (cc_moves[symbol]).std()*16
            my_list = dict1.items()
            my_list = [list(x) for x in my_list]
            df = (pd.DataFrame(my_list, columns=['Symbols', 'HVs'])).sort_values('HVs', ascending =False)
            print(df)
            return(dict1)
        
#cc_moves = PT_Operations(price_table).cc_moves_function()		
#volatility = (cc_moves['ZTS']).std()
#hist_vol = PT_Operations(price_table).hist_vol()
#PT_Operations(price_table).cc_moves_scrubbed()
#
#		self.cc_moves = self.df
#		for row in self.rows[1:]:
#			print(self.df['ZBH'][row+dt.timedelta(days=-1)])
#			
#
#		for column in self.df.columns.values.tolist():
#			for row in self.df.index.tolist():
#				try:
#					self.cc_moves[column][row] = ((self.df[column][row] - self.df[column][(row+dt.timedelta(days=-1))]) / self.df[column][(row+dt.timedelta(days=-1))])
#					print(self.df[column][row])
#					#print(self.df[column][(row+dt.timedelta(days=-1))])
#				except Exception:
#					100
#
#				else:
#					pass
#		self.df['ZTS'][dt.datetime(2018,2,26)] = 100
#		return(self.cc_moves)	
#
#
#price_table = PT_Operations(price_table).cc_moves()
#print(price_table)
#print(type(price_table))

#
#	def cc_pct_move(day1, day2):
#		try:
#			pct_move = round(((day2 - day1) / day1),2)
#		except Exception:
#			return(float('nan'))
#		else:
#			return(pct_move)
#
#def apply_cc_pt_move(df):
#	zipped = [zip(
#
#for (i, j) in (range(df.shape[0]), range(df.shape[1])):
#		try:
#			value = (df[i,j] - df[i-1, j] / df[i-1, j]) 
#		except Exception:
#			return float('nan')
#		else:
#			return(value)
#
#pct_moves = apply_cc_pt_move(price_table)
#print(pct_moves)
#
##print(price_table.size)
##print(price_table.shape)
##print(type(price_table.shape))
##print(price_table.shape[0])
##print(price_table.shape[1])
#
#
#print(cc_pct_move(2, 1.8))
#print(cc_pct_move(0,0))
#print(cc_pct_move(2,0))
#print(cc_pct_move(0,2))
#print(cc_pct_move('lsf','dfdf'))
#	
#print(price_table)
#print(corr_table)
#print(corr_table.describe())
