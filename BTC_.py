import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
     

def sim(history_price,ema_12,ema_26,buy,sold,info=False):
  usd=100
  btc=0
  end=0
  for i in range(len(history_price)):
    if ema_1[i]>ema_2[i] and ema_1[i-1]<=ema_2[i-1] and ema_1[i-2]<=ema_2[i-2]:
      btc+=usd*buy/history_price[i]
      usd*=1-buy
      if info:
        print(usd+btc*history_price[i],i)
      elif ema_1[i]==ema_2[i-1] and ema_1[i-2]>=ema_2[i-2]:
        usd+=btc*sold*history_price[i]
        btc*=1-sold
      if info:
        print(usd+btc*history_price[i],i)
  return usd+btc*history_price[-1]
 
def draw(history_price, ema12, ema26):
  plt.plot(history_price, label="Close Prices")
  plt.plot(ema12, label="EMA12 Values")
  plt.plot(ema26, label="EMA26 Values")
  plt.xlabel("Days")
  plt.ylabel("Price")
  plt.legend()
  plt.show()
unix,date,symbol,open,high,low,close,Volume BTC,Volume EUR
period = ['2023-01-01','2023-02-01','2023-03-01','2023-04-01','2023-05-01','2023-06-01','2023-07-01']

for ii in range(1):
  #coin = yf.Ticker('BTC-USD')
  #history_data = coin.history(start=period[ii],end=period[ii+1],interval='1d')
  #history_price = history_data['Close']
  df = pd.read_csv('BTC-USDT.csv')
  df_date = df['close']
  
  print(df)
  #ema12 = history_price.ewm(alpha=2/13).mean()
  #ema26 = history_price.ewm(alpha=2/27).mean()
  #draw(history_price=history_price, ema12=ema12, ema26=ema26)
  #sim(history_price=history_price,ema_12=ema12,ema_26=ema26,buy=1.0, sold=1.0,info=True)
