from datetime import datetime
from zipline import run_algorithm
from zipline.api import order, record, symbol, symbols, get_datetime
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from collections import Counter
import pytz
import pandas as pn
import numpy as np


def initialize(context):
    # create var in namespace context. this one will be the wide window of bars from within which I will be playing
    # with data. It's like extracting initial set of data. It will be used in handle_data in Zipline,
    # which means it will be working on a day by day basis. Each day I will be bringing this number of
    # wide net of bars/days
    context.historical_bars = 30
    # this var is a window of bars needed to form a feature/set based on which the learning will be done. For example,
    # the behaviour of prices during these 10 days will be analyzed and a label will be created for these 10 days.
    # More on this later...
    context.feature_window = 10
    # this is the var that contains the list of stocks manually selected. Hese in zipline I use other tickers than in
    # in the Sentdex video for lesson #14 because quantopian-quandl bundle doesn't have data for SPDR sectors.
    # it is supposed to be a list, but I'm not sure. I can access some elements through [i], but I still don't a
    # definitive way to logically understand
    context.stocks = symbols('AAPL',
                             'MSFT',
                             'FB',
                              'AMZN')
    # here I take len of stocks, which is 4, then I create range from 1 to 4 and loop over it.
    for i in context.stocks:
        # I print i-th element of the list?? "or something else"  stocks as I go through the loop
        print('context.stocks', i)

# this method in zipline supposedly only get called once a day, BUT in Quantopian it's different, it's minute based
def handle_data(context, data):

    """
    Execute orders according to our schedule_function() timing.
    """
    # here I create a var that collects dataframe from the stocks, for each stock and gets last known price for a period
    # indicated with hist.bars var and I indicate bar's window, which is 1 day ( it also can be 1m). SO it all means:
    # I bring: last price of all the 30 bars (in this case - days), for all the tickers.
    # It will start on the day that I choose in the backtester as the "From date" plus 29 days back.
    prices = data.history(context.stocks, 'price', context.historical_bars, '1d')
    # I print the len of prices, which is 30, the same as #bars
    print("\nhandle_data loop:> len of prices:", len(prices), get_datetime())
    # here I print prices and as I see they get printed for one day, then the code continues and prints the rest, then
    # and it gets repeated again. so only one day of data gets printed first
    #print(('prices', prices), end="\n\n")
    # create for lop to iterate through the list of stocks
    for stock in context.stocks:
        # check if the stock is tradable
        print("\nFirst for loop:>  Date and Time", get_datetime())
        if data.can_trade(stock):
            print("Now the value of iterator 'stock' is:", stock)
            # define var that contains average of last prices of last 50 days
            MA1 = data.history(stock, 'price', 50, '1d').mean()
            print("MA1 for stock:", stock.symbol, MA1)
            MA2 = data.history(stock, 'price', 200, '1d').mean()
            # define var that contains average of last prices of last 200 days
            print("MA2 for stock:", stock.symbol, MA2)
            # define var that contains average of last prices of last 30 days
            AVRG_30 = data.history(stock, 'price', 30, '1d').mean()
            print("Average for 30 days for stock:", stock.symbol, AVRG_30)
            # var to capture the current price for the current day, it should be the same as the 1st price in the
            # 'prices' list
            price = data.current(stock, "price")  # old way data[stock].price
            # prints current price of the run
            print(("current price for stock : ", price), end="\n\n")
            # creates another var to set up the starting bar for the feature window
            start_bar = context.feature_window
            # price_list var is assigned a list created with .tolist() for a current stock in "for loop"
            # from the dataframe - 'prices'
            price_list = prices[stock].tolist()
            print("len(price_list):..", len(price_list))
            print('price_list for stock.symbol', stock.symbol, np.around(price_list, 3))
            # creates two empty lists
            X = []
            y = []
            # new var bar that is the same as srart_bar the same as feature_window = 10
            bar = start_bar

            # feature creation
            while bar < len(price_list) - 1:
                try:
                    print("\nWhile loop:> the value of 'len(price_list) - 1' now is", len(price_list) - 1, "Date is:", get_datetime())
                    print("\nWhile loop:> The value of bar is:...", bar)
                    end_price = price_list[bar +1]
                    print("\nWhile loop:> end_price is:...", end_price)
                    print("\nWhile loop:> end_price is %d-tieth position in 'price_list'" % (bar + 1))
                    start_price = price_list[bar]
                    print("\nWhile loop:> start_price is:...", start_price)
                    print("\nWhile loop:> start_price is %d-tieth position in 'price_list'" % bar)
                    pricing_list = []
                    print("\nWhile loop:> pricing_list is:...", pricing_list)
                    xx = 0
                    for _ in range(context.feature_window):
                        print("\nInside the '_ for loop', the '_' is:...", _)
                        price = price_list[bar - (context.feature_window - xx)]
                        print("\nInside the '_ for loop', the 'price' is:...", price, "it's %d-ieth element of price_list" % (bar - (context.feature_window - xx)))
                        print("\nInside the '_ for loop', the 'bar' is:...", bar)
                        print("\nInside the '_ for loop', the 'context.feature_window' is:...", context.feature_window)
                        print("\nInside the '_ for loop', the 'xx' is:...", xx)



                        # appending price to a list 'pricing_list'
                        pricing_list.append(price)
                        print("\n'pricing_list' is...", pricing_list)
                        xx += 1
                        print("\n 'xx' is...", xx)
                    # np.diff checks the difference between two neighboring numbers.
                    print("\n'np.diff(pricing_list)' is:...", np.diff(pricing_list))
                    print("\n'pricing_list[:-1]' is:...", pricing_list[:-1])
                    print("\n'np.diff(pricing_list) / pricing_list[:-1] * 100.0' is ...,", np.diff(pricing_list) / pricing_list[:-1] * 100.0)
                    features = np.around(np.diff(pricing_list) / pricing_list[:-1] * 100.0, 1)
                    print("\nThe value of 'np.diff(pricing_list) / pricing_list[:-1]' is...", np.diff(pricing_list) / pricing_list[:-1])
                    print("\n Outside the '_ for loop', 'features is...'", features)
                    # here we compare the start_day price(one day after the last feature day)
                    # with end day price(two days later after the last feature), which means that with all the
                    # conditions that repeated itself in the pattern of the given features, in this case we could
                    # label it as '1' and it means to buy
                    if end_price > start_price:
                        label = 1
                    else:
                        label = -1
                    bar += 1
                    print("bar is...", bar)
                    print(features)
                    # appends to the list X the features that it works with, so it should get more and more populated
                    # with each for loop for individual stock
                    X.append(features)
                    print("list X is...", X)
                    # appends processed labels to the list y
                    y.append(label)
                    print("list y is:...", y)





                except Exception as e:
                    bar += 1
                    print(("Feature creation step", str(e))) # check if it works with one pair of parens less
            #  assigns to var clf value of the method/function of random forest classifier from scikit-learn
            clf = RandomForestClassifier()
            # takes the price_list for current stock and only takes values from -10th till the end. Last 10 values of
            # the price_list, which is in total 300 values.
            last_prices = price_list[-context.feature_window:]
            print("last_prices:...", last_prices, end='\n')
            # creates set of features based on these last 10 price values for the current stock of the loop
            current_features = np.around(np.diff(last_prices) / last_prices[:-1] * 100.0, 1)
            print("current_features:...", current_features, end='\n')








"""def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), 'price'))
    context.randomStuff += 1
"""

capital_base = 10000
start = datetime(2016, 1, 4, 0, 0, 0, 0, pytz.utc)
end = datetime(2016, 1, 6, 0, 0, 0, 0, pytz.utc)

run_algorithm(start=start, end=end, initialize=initialize,
              capital_base=capital_base, handle_data=handle_data,
              bundle='quantopian-quandl')