f = open('BTC-USDT.csv')
ff = f.readlines()
of = open('BTC.txt','a')
for i in range(len(ff)):
  of.write(ff[-i-1])
of.close()
f.close()
