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
        
        self.time_frame = Period(-1*time_frame,Years)

        self.term_dates = None
        self.term_price = None
        self.annualized_return = None
        self.annualized_vol = None
        self._fetch_data()

    def _fetch_data(self):
        yahoo_financials = YahooFinancials(self.ticker)
        start=UnitedStates(UnitedStates.NYSE).advance(Date(27,4,2023),Period("-1Y"))
        data = yahoo_financials.get_historical_price_data(start_date=start.to_date().strftime('%Y-%m-%d'), end_date=self.mkt_date.to_date().strftime('%Y-%m-%d'), time_interval='daily')
        prices = [day['adjclose'] for day in data[self.ticker]['prices']]
        dates = [x['formatted_date'] for x in data[self.ticker]['prices']]
        self.term_price = np.array(prices)
        self.term_dates = pd.to_datetime(dates)

    def calculate_annualized_return(self):
        daily_returns = (self.term_price[1:] / self.term_price[:-1]) - 1
        total_return = np.prod(daily_returns + 1) - 1
        num_years = len(self.term_dates) / 365
        self.annualized_return = (1 + total_return) ** (1 / num_years) - 1

    def calculate_annualized_vol(self):
        daily_returns = (self.term_price[1:] / self.term_price[:-1]) - 1
        self.annualized_vol = np.std(daily_returns) * np.sqrt(252)

