# __str__ example

class Car:
    type = 'vehicle'   
    
    def __init__(self, color, price):
        self.color = color
        self.price = price
    def __str__(self):
        return(f"type={self.type}.")
		
my_car = Car('red',234343.33)
print(my_car)

my_car1 = Car('white',244343.33)
print(my_car1)