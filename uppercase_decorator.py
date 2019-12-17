# Uppercase decorator

def uppercase_decorator(function):
    def func_wrapper(x):
        res = function(x)
        return res.upper().center(len(res)*2,"_")
    return func_wrapper
    
@uppercase_decorator
def make_uppercase(x):
    return x
    
    
print(make_uppercase("hey"))
print(make_uppercase("hey this is a simple string"))

