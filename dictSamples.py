#!/usr/bin/python
ab={'Swaroop':'swaroopch@byteofpython.info',
'Larry':'larry@wall.org',
'Matsumoto':'matz@ruby-lang.org',
'Spammer':'spammer@hotmail.com'
}
for t,k in ab.items():
  print 'Contact %s at %s' %(t,k)

a=[0,1,2,3,4,5]
print '-3~2',a[-3:2]
print '2~-3',a[2:-3]
