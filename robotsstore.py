class Product(object):
 
  price = 0 
  count = 0
  tax = 0

  def price_with_tax(self):
  	return self.price * self.count * self.tax 

robot=Product()
robot.price = 900
robot.count = 2
robot.tax = 1.25

book=Product()
book.price = 100
book.count = 1
book.tax  = 1.06

print robot.price_with_tax()+book.price_with_tax()


		






 	



print robot.price*robot.count*robot.tax+book.price*book.count*book.tax


 	

