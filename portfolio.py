from yahoofinancials import YahooFinancials
import numpy as np
import pandas as pd
from datetime import datetime
from QuantLib import *


# image
import seaborn as sns
import matplotlib.pyplot as plt

from stock import Stock

# Takes a list of stocks, returning stock correlation matrix
class Portfolio():
    def __init__(self, name, tickers, mkt_date, time_frame):
        self.name = name
        self.tickers = tickers
        self.mkt_date = mkt_date
        self.time_frame = time_frame

        self.stocks = [Stock(ticker, mkt_date, time_frame) for ticker in tickers]
    def calculate_correlation_matrix(self, image: bool = False):
        if len(self.stocks) <= 1:
            print("ERROR: Not enough stocks in the portfolio")
        else:
            # self.df_returns = pd.DataFrame()
            returns = [stock.df['daily_return'] for stock in self.stocks]
            self.df_returns = pd.DataFrame(returns).transpose()
            self.df_returns.columns = self.tickers
            self.corr_matrix = self.df_returns.corr()

            if (image):
                sns.heatmap(self.corr_matrix, annot = True, cmap = 'coolwarm')
                # Set the title of the heatmap
                plt.title('Correlation Matrix of Portfolio: ' + self.name)
                # Display the heatmap
                plt.show()


