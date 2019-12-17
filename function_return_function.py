# function f is return the reference of function get  - nf1 = f(1)
# so, we can call function g with the reference - nf1(1)
def f(x):    
    def g(y):        
        return y + x + 3 
    return g

nf1 = f(1)
nf2 = f(3)
# nf2 = f(5)

print(nf1(1))
print(nf2(2))