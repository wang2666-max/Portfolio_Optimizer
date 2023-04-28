from yahoofinancials import YahooFinancials
import numpy as np
import pandas as pd
from datetime import datetime


from QuantLib import *

class Stock:
    def __init__(self, ticker, mkt_date,time_frame):

        self.ticker = ticker
        
        mkt_date = datetime.strptime(mkt_date, '%Y-%m-%d')
        self.mkt_date= Date(mkt_date.day, mkt_date.month, mkt_date.year)

        self.years=time_frame
        
        self.time_frame = Period(-1*time_frame,Years)

        self.term_dates = None
        self.term_price = None
        self.df=None
        
    
        self._fetch_data()

    def _fetch_data(self):
        yahoo_financials = YahooFinancials(self.ticker)
        start=UnitedStates(UnitedStates.NYSE).advance(Date(27,4,2023),Period("-1Y"))
        data = yahoo_financials.get_historical_price_data(start_date=start.to_date().strftime('%Y-%m-%d'), end_date=self.mkt_date.to_date().strftime('%Y-%m-%d'), time_interval='daily')
        prices = [day['adjclose'] for day in data[self.ticker]['prices']]
        dates = [x['formatted_date'] for x in data[self.ticker]['prices']]
        print(dates[0])
        df1=pd.DataFrame()
        df1["dates"]=dates
        df1["price"]=prices
        df1["daily_return"]=np.log(df1["price"]/df1["price"].shift())

        print(df1.head())
        self.df=df1
        self.term_price = np.array(prices)
        self.term_dates = pd.to_datetime(dates)

    def calculate_annualized_return(self):
        
        total_return = np.log(list(self.df["price"])[-1] / list(self.df["price"])[0]) 
        
        self.annualized_return = total_return / self.years

    def calculate_annualized_vol(self):
        total_vol=self.df["daily_return"].std()
        
        self.annualized_vol = total_vol * np.sqrt(252)

