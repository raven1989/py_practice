#!/usr/bin/python
def beatStock(stock):
  n=len(stock)
  buy=0
  sell=0
  max_dif=stock[sell]-stock[buy]
  for i in range(n):
    if(stock[buy]>stock[i]):
      buy=i
    if(stock[i]-stock[buy]>max_dif):
      max_dif=stock[i]-stock[buy]
      sell=i
  return (buy,sell)

s=[2,3,1,3,7,5,4]
time=beatStock(s)
print s
print 'best time to buy in @ day %d while to sell out day @ %d'%time
