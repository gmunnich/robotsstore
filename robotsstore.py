class Product(object):
 	price = 0 
 	count = 0
 	tax = 0

robot=Product()
robot.price = 900
robot.count = 2
robot.tax = 1.25

book=Product()
book.price = 100
book.count = 1
book.tax  = 1.06

print robot.price*robot.count*robot.tax+book.price*book.count*book.tax


 	

