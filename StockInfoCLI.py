import itertools
import threading
import time
import sys
import argparse
from termcolor import colored
import yfinance as yf

# Initialize parser
msg = "Adding description"
parser = argparse.ArgumentParser(description = msg)
parser.add_argument("-t", "--Ticker", help = "Enter Stock Ticker")
# parser.parse_args()
args = parser.parse_args()

# Loader Animation
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading please wait ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!                           \n')


if args.Ticker:
  try:
    getTicker = args.Ticker
    print("Entered Ticker is: % s" % getTicker)
    # Start Loader
    t = threading.Thread(target=animate)
    t.start()
    # Get Ticker Info
    tickerInfo = yf.Ticker(getTicker)
    # Stop Loader
    time.sleep(10)
    done = True
    # Print Stock Info
    print(colored("\rName: ", attrs=['bold']) + colored(str(tickerInfo.info['shortName']),'blue'))
    print(colored("Currency: ", attrs=['bold']) + colored(str(tickerInfo.info['currency']),'blue'))
    print(colored("Current Price: ", attrs=['bold']) + colored(str(tickerInfo.info['regularMarketPrice']),'blue'))
    print(colored("Exchange Timezone: ", attrs=['bold']) + colored(str(tickerInfo.info['exchangeTimezoneName']),'blue'))
  except:
    print('Invalid ticker')
else:
  print("Please enter a Ticker")