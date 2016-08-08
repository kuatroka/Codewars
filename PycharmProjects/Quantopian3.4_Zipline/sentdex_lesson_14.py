import zipline
from zipline.api import order, record, symbols
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from collections import Counter
import numpy as np
import pandas as pd
#perf = pd.read_pickle('buyapple_out.pickle') # read in perf DataFrame
#perf.head()


def initialize(context):
    context.historical_bars = 30
    context.feature_window = 10
    context.stocks = symbols('XLY',  # XLY Consumer Discretionary SPDR Fund
                             'XLF',  # XLF Financial SPDR Fund
                             'XLK',  # XLK Technology SPDR Fund
                             'XLE',  # XLE Energy SPDR Fund
                             'XLV',  # XLV Health Care SPRD Fund
                             'XLI',  # XLI Industrial SPDR Fund
                             'XLP',  # XLP Consumer Staples SPDR Fund
                             'XLB',  # XLB Materials SPDR Fund
                             'XLU')  # XLU Utilities SPRD Fund

    """
    Called once at the start of the algorithm.
    """
    # Rebalance every day, 1 hour after market open.
    #schedule_function(my_rebalance, date_rules.every_day(), time_rules.market_open(hours=1))

    # Record tracking variables at the end of each day.
    #schedule_function(my_record_vars, date_rules.every_day(), time_rules.market_close())


def hande_data(context, data):
    """
    Execute orders according to our schedule_function() timing.
    """
    prices = data.history(context.stocks, 'price', context.historical_bars, '1d')
    print(prices)
    for stock in context.stocks:
        if data.can_trade(stock):
            MA1 = data.history(stock, 'price', 50, '1d').mean()
            MA2 = data.history(stock, 'price', 200, '1d').mean()
            price = data.current(stock, "price")  # old way data[stock].price
            start_bar = context.feature_window
            price_list = prices[stock].tolist()
            print('After tolist()', stock.symbol, np.around((price_list), 3))

"""            x = []
            y = []
            bar = start_bar
            print("Lengh of price_list", len(price_list) - 1)

            # feature creation
            while bar < len(price_list) - 1:
                try:
                    end_price = price_list[bar + 1]
                    print("bar and len", bar, len(price_list) - 1)
                    print("end_price", np.around(end_price, 3))
                    start_price = price_list[bar]
                    print("start_price", np.around(start_price, 3))

                    pricing_list = []
                    print("Pricing_list", pricing_list)
                    xx = 0
                    for _ in range(context.feature_window):
                        price = price_list[bar - (context.feature_window - xx)]
                        pricing_list.append(price)
                        xx += 1
                    features = np.around(np.diff(pricing_list) / pricing_list[:-1] * 100.0, 1)

                    print(features)
                    bar += 1


                except Exception as e:
                    print(("Feature Creation step", str(e)))


                    # if MA1 > MA2:
                    #   order_target_percent(stock, 0.11)
                    # elif MA1 < MA2:
                    #   order_target_percent(stock, -0.11)

            record(MA1=MA1, MA2=MA2, price=price)
            record("leverage", context.account.leverage)
"""

def my_record_vars(context, data):
    """
    Plot variables at the end of each day.
    """
    pass


def handle_data(context, data):
    """
    Called every minute.
    """
    pass

