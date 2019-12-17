# simple decorator

def square_decorator(func):
    def function_wrapper(x):        
        res = func(x)
        return res * res             
    return function_wrapper
    

@square_decorator
def square(n):
    return n
    
# square1 = square_decorator(square)    
print(square(10))

