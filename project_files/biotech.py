import numpy as np
import pandas as pd
import datetime as dt
import pickle
from pprint import pprint

#Data Structure Outline for Stock as a Dict:
# <ticker>  
#   <company_name>  
#   <is_optionable>
#   <sector>
#   <subsector>
#   <industry>
#   <call_open_interest>
#   <put_open_interest>
#   <total_open_interest>
#   <best_index>
#
#
#
#
#   <drug>
#       <indication>
#           <market>
#               <US_market>
#                   <stage_of_development>
#                   <prob_success>
#                   <US_patient_population>
#                   <US_peak_penetration_est>
#                   <US_peak_penetration_year>
#                   <US_patent_expiration_year>
#                   <US_price_est>
#                   <US_gross_margin_est>
#               <Europe_market>
#           <competitor>
#               <name>
#               <market_share>
#               <price>
#               <efficacy
#               <safety>
#               <stage_of_development>
#               <prob_success>
#       <upcoming_catalyst>
#           <indication>
#           <catalyst_name>
#           <timing>
#           <probability_distribution>
#
#               
#               
#
#
#
#
#
#
#
#
#
#
#

class Stock():
        def __init__(self, ticker = 'ZTS'):  #set inital attributes, taken from external data sources
                self.ticker = ticker        #set ticker
                self.price = pickle.load(open('sp500_price_table.pkl', 'rb'))[self.ticker].tail(1).tolist()[0]      #retrieve last closing price from pickle file
                self.sector = 'Healthcare'      #default sector to Healtchare (for now)
                self.subsector = 'Biotech'
                self.company_name = 'Corbus Pharmaceuticals'
                self.isoptionable = True
                self.openinterest = 10000
                self.best_index = 'XBI'
                self.drugs = [Drug('Anabasum'), 'drug2']
                self.financials = []
                pprint(self.__dict__)

ZTS = Stock('ZTS')

class Drug():
        def __init__(self, name = 'Anabasum'):
            self.name = name
            self.indications = [Cystic_Fibrosis, 'Dermatomyositis', 'Scleroderma']
            self.competitors = ['drug1', 'drug2', 'drug3']
            pprint(self.__dict__)

class Indication():
        def __init__(self, name = 'Cystic_Fibrosis'):
            self.name = name
            self.size_general = 25000



#Cystic_Fibrosis = Indication('Cystic_Fibrosis')
#Anabasum = Drug('Anabasum')
#CRBP = Ticker('ZTS')
#print(CRBP.paul)
#CRBP.sector = 'Financials'
#print(CRBP.sector)
#x = CRBP.__init__()
#print(x)
#print(Anabasum.indications, Anabasum.competitors, Anabasum.name) 

class Company():
        def __init__(self):
                print("We are creating a new entry.")

        def newTicker(self):
                self._Ticker = input("Enter the stock ticker: ")
                self._CompanyName = input("Enter the company name: ")
                self._Sector = input("Enter the Sector: ")

        def setTicker(self):
                self._Ticker = input("Enter the stock ticker: ")
                print("You have entered:", self._Ticker)
                return self._Ticker
        
        def setCompanyName(self):
                self._CompanyName = input("Enter the company name: ")
                print("You have entered:", self._CompanyName)
                return self._CompanyName

        def Ticker(self):
                print(self._Ticker)
                print(self._CompanyName)
                return(self._Ticker)

        def CompanyName(self):
                print(self._CompanyName)
                return(self._CompanyName)
    
#CRBP = Company()
#CRBP.setTicker()
#CRBP.setCompanyName()
#print(type(CRBP))
#CRBP.Ticker()
#print(type(CRBP))
#CRBP.CompanyName()
##print(type(CRBP))
#print(CRBP._Ticker)
#print(CRBP._CompanyName)
#print(dir(CRBP))
#CRBP.__dict__
#print(CRBP.__dict__)
#pprint(CRBP.__dict__)
