
import config
import pandas as pd

import robin_stocks.robinhood as rh
import datetime as dt
import time


def login(days):
    time_logged_in = 60*60*24*days
    rh.authentication.login(username=config.USERNAME,
                            password=config.PASSWORD,
                            expiresIn=time_logged_in,
                            scope='internal',
                            by_sms=True,
                            store_session=True)

def logout():
    rh.authentication.logout()

#def get_stocks():
    # add your stocks here
    #stocks = list()
    #stocks.append('AMZN')
    #return(stocks)
def current_time():
    time = dt.datetime.now().time()
    return(time)
def open_market():
    market = False
    time_now = dt.datetime.now().time()

    market_open = dt.time(9,30,0) # 9:30AM
    market_close = dt.time(15,59,0) # 3:59PM
    

    if time_now > market_open and time_now < market_close:
        market = True
    else:
         print('market is closed')
         pass

    return(market)


#def get_cash():
 #   rh_cash = rh.account.build_user_profile()
 #   print(rh_cash)

   # cash = float(rh_cash['cash'])
    #equity = float(rh_cash['equity'])
    #return(cash, equity)

#def view_profile():
  #  profile_basics = rh.account.build_user_profile()
  #  return(profile_basics)

def get_info(ticker, info):
    price_action_data = rh.stocks.get_fundamentals(ticker)[0][info]
    return(price_action_data)

def get_moving_average(ticker, option='close_price', interval='5minute', span='day'):
    history = rh.stocks.get_stock_historicals(ticker, interval, span)
    
    count = 0
    total = 0
    
    for time_frame in history:
        total += float(time_frame[option])
        count += 1
        
    return total/count    

login(days=1)

'''
ticker: any stock symbol
info: open, high, low, volume,
{'market_date': '2022-09-14', 'average_volume_2_weeks': '10767995.200000', 'average_volume': '10767995.200000', 'high_52_weeks': '2.140000', 'dividend_yield': None, 'float': '812844421.750000', 'low_52_weeks': '0.910000', 'market_cap': '1158000625.000000', 'pb_ratio': '3.378130', 'pe_ratio': '25.000000', 'shares_outstanding': '818375000.000000', 'description': 'Denison Mines Corp. engages in the exploration and development of uranium. The firm has interest in the McClean Lake and Mill, Wheeler River, Waterbury, Midwest, and Hook-Carter projects. It operates through the following segments: Mining, Closed Mines, and Corporate and Other. The company was founded on May 9, 1997 and is headquartered in Toronto, Canada.', 'instrument': 'https://api.robinhood.com/instruments/258d54d0-8a95-4059-a8ac-29dca732e9fb/', 'ceo': 'David D. Cates', 'headquarters_city': 'Toronto', 'headquarters_state': 'Ontario', 'sector': 'Non-Energy Minerals', 'industry': 'Other Metals/Minerals', 'num_employees': None, 'year_founded': 1997, 'symbol': 'DNN'}
'''

'''
print(rh.stocks.get_fundamentals("DNN")[0])
vol=get_info("DNN", 'volume')
print(vol)

while between 9:30am and 4:00 do
    if(volume>10000000 & 5day> 1.20)
    buy(DNN, 100)
'''

#history = get_history("DNN")

#print(get_moving_average(history))

#avg = get_moving_average("DNN", option='close_price', interval='day', span='week')

#print(avg)

'''
PARAMETERS
'''
STOCK = "FFIE"
INTERVAL = "5minute"
SPAN = "day"
OPTION = "close_price"
UPDATE_TIME = 20 # seconds
INFO_CRITERIA = "volume"
VOLUME_TRIGGER = float(45000000)
MOVING_AVG_TRIGGER = float(.50)
BUY_QUANTITY =1000


while(True):
    criteria1 = get_moving_average(STOCK, option=OPTION, interval=INTERVAL, span=SPAN)
    criteria2 = get_info(STOCK, INFO_CRITERIA)
    
    print()
    print(dt.datetime.now())
    print("Price Moving Average: ", criteria1)
    print(INFO_CRITERIA, ": ", criteria2)
    
    if(float(criteria1) > MOVING_AVG_TRIGGER and float(criteria2) > VOLUME_TRIGGER):
        print("Buying ", BUY_QUANTITY, " shares of ", STOCK)
        rh.orders.order_buy_market(STOCK,BUY_QUANTITY)
        
    time.sleep(UPDATE_TIME)