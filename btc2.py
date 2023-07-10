import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def sim(history_price,ema12,ema26,buy,sold,info=False):
  ema12i=ema12.iloc
  ema26i=ema26.iloc
  hpi=history_price.iloc
  usd=100
  btc=0
  end=0
  for i in range(len(history_price)):
    if ema12i[i][0]>ema26i[i][0] and ema12i[i-1][0]<=ema26i[i-1][0]:
      btc+=usd*buy/hpi[i][0]
      usd*=1-buy
    elif ema12i[i][0]<ema26i[i][0] and ema12i[i-1][0]>=ema26i[i-1][0]:
      usd+=btc*sold\hpi[i][0]
      btc*=1-sold
    if not info:
      print(usd,btc*hpi[i][0],i)
  return usd+btc*hpi[-1][0]
 
def draw(history_price, ema12, ema26):
  plt.plot(history_price, label="Close Prices")
  plt.plot(ema12, label="EMA12 Values")
  plt.plot(ema26, label="EMA26 Values")
  plt.xlabel("Days")
  plt.ylabel("Price")
  plt.legend()
  plt.show()
period = ['2023-01-01','2023-02-01','2023-03-01','2023-04-01','2023-05-01','2023-06-01','2023-07-01']

for ii in range(1):
  #coin = yf.Ticker('BTC-USD')
  #history_data = coin.history(start=period[ii],end=period[ii+1],interval='1d')
  #history_price = history_data['Close']
  df_csv = pd.read_csv('BTC-USD.csv')
  history_price = pd.DataFrame({'Close':np.array(df_csv['Close'])}, index=np.array(df_csv['Start']))
  history_price = history_price['2022-01-01':'2023-01-01']
  print(history_price)
  ema12 = history_price.ewm(alpha=2/13).mean()
  ema26 = history_price.ewm(alpha=2/27).mean()
  for i in range(1,11):
      for j in range(1,11):
          print(i/10,j/10,sim(history_price,ema12,ema26,i/10, j/10,info=True))
  draw(history_price, ema12, ema26)
