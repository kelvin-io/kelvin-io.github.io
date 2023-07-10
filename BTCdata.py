f = open('BTC-USD.csv')
ff = f.readlines()
of = open('BTC.txt','a')
for i in range(len(ff)):
  of.write(ff[-i-1])
of.close()
f.close()
