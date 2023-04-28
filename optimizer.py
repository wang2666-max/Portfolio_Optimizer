from stock import Stock


if __name__ == "__main__":

    stock = Stock("AAPL", "2023-04-27" ,1)
    stock.calculate_annualized_return()
    
    print(stock.annualized_return)




    # start_date = '1990-01-01'
    # end_date = '2021-07-12'

    # yahoo_financials = YahooFinancials('AAPL')
    # historical_data = yahoo_financials.get_historical_price_data('2022-04-27', '2023-04-27', 'daily')

    # adj_close_prices = [day['adjclose'] for day in historical_data['AAPL']['prices']]
    # print (adj_close_prices[0])
