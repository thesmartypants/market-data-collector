import urllib.request
import json
import time
import os
from datetime import date

hist = open('history.csv', 'a')
cur = input('enter crypto currency: ')
of_cur = input('official currency in your country ex: cad, usd, mxn: ')
url = f'https://api.coingecko.com/api/v3/simple/price?ids={cur}&vs_currencies={of_cur}'
while 1:
  req = urllib.request.urlopen(url).read().decode()
  d = json.loads(req)
  last_price = d[cur][of_cur]
  now = date.today()
  datetime=now.strftime('%b-%d-%Y-%H-%M-%S')
  hist.write(datetime+','+last_price+'\n')
  os.system('clear')
  print(hist.read())
  time.sleep(15)
hist.close()