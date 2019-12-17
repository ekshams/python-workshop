# simple decorator

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling "+ func.__name__)
        res = func(x)
        print(res)
        print("After calling "+ func.__name__)
    return function_wrapper
    

# @our_decorator   # succ = our_decorator(succ)    
def succ(n):
    return n
    
succ1 = our_decorator(succ)    
succ1(10)

