import urllib.request
import json
import time
import os
from datetime import date

hist = open('history.csv', 'a')
cur = input('enter crypto currency: ')
of_cur = input('official currency in your country ex: cad, usd, mxn: ')
url = f'https://api.coingecko.com/api/v3/simple/price?ids={cur}&vs_currencies={of_cur}'

try:
  while 1:
    # get last price
    req = urllib.request.urlopen(url).read().decode()
    d = json.loads(req)
    last_price = d[cur][of_cur]

    #add to history file
    now = date.today()
    datetime=now.strftime('%b-%d-%Y-%H-%M-%S')
    hist.write(str(datetime)+','+str(last_price)+'\n')
    hist.flush()
    time.sleep(15)
except KeyboardInterrupt:
  hist.close()