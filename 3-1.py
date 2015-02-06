#width = input ('Please enter width : ')
#Write in 6/2/2015 for calculate the friut price

print "Welcome to my Fruit Store, What kind of Fruit you want?"

buy_Apple = input ('How many Apples you want to buy?')
buy_Pears = input ('How many Pears you want to buy?')
buy_Cantaloupes = input ('How many Cantaloupes you want to buy?')
buy_DriedApricots = input ('How many DriedApricots you want to buy?')
buy_Prunes = input ('How many Prunes you want to buy?')

width = 30
price_width = 20
item_width = 10
total_width = 20
header_format = '%-*s%*s%*s'
format        = '%-*s%*.2f%*.2f'

bottom_format = '%-*s%*s'


aa = 0.4*buy_Apple
bb = 0.5*buy_Pears
cc = 1.92*buy_Cantaloupes
dd = 8*buy_DriedApricots
ff = 12*buy_Prunes
buy_num = buy_Apple+buy_Pears+buy_Cantaloupes+buy_DriedApricots+buy_Prunes
tot = aa+bb+cc+dd+ff

print '=' * width *2

print header_format % (item_width,'item',price_width,'Price',total_width,'Total Price')

print '-' *width*2

print format % (item_width, 'Apples' , price_width,0.4, total_width, aa)
print format % (item_width, 'Pears' , price_width,0.5, total_width, bb)
print format % (item_width, 'Cantaloupes' , price_width,1.92, total_width, cc)
print format % (item_width, 'Dried Apricots(16 oz)' , price_width,8, total_width, dd)
print format % (item_width, 'Prunes (4 lbs)' , price_width,12, total_width, ff)
print '=' * width * 2

ccu = input ('Import Money:')
cco = ccu-tot
if ccu>0:
      print bottom_format % (price_width, 'Numbers',total_width,'Total Price')
      print format % (item_width,'Items',price_width,buy_num,total_width,cco)
elif ccu<tot:
      print "Error"
      print "Please input Received money again:"
else:
      print bottom_format % (price_width, 'Numbers',total_width,'Total Price')
      print format % (item_width,'Changes',price_width,buy_num,total_width,tot)
