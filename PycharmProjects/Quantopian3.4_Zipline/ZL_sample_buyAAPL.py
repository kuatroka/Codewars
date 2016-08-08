# import from zipine.api package. we bring functions order(), record(), symbol()
"""
- order() which takes two arguments: a security object, and a number specifying how many
stocks you would like to order (if negative, order() will sell/short stocks).
In this case we want to order 10 shares of Apple at each iteration.
-  record() function allows you to save the value of a variable at each iteration.
You provide it with a name for the variable together with the variable itself: varname=var.
After the algorithm finished running you will have access to each variable value you tracked with record()
under the name you provided
"""
from zipline.api import order, record, symbol
import pandas as pd
"""initialize(context)
Called once at the very beginning of a backtest. Your algorithm can use this method to set up any bookkeeping that
you'd like. The context object will be passed to all the other methods in your algorithm.
Parameters:
context: An initialized and empty Python dictionary. The dictionary has been augmented so that properties
can be accessed using dot notation as well as the traditional bracket notation.
Returns: None
"""
def initialize(context):
    context.security = [symbol("AAPL"), symbol("TSLA")]
    #for i in range(0, (len(context.security))):
        #print(context.security[i].asset_name)



def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), 'price'))

# read in pd dataframe from output pickle
perf = pd.read_pickle('buyapple_out.pickle')
perf.head()