# example of map(), reduce(), and filter()
from functools import reduce
my_list = list(range(1,11))
print(my_list)

# Use lambda function with filter
filterd_list = list(filter(lambda x: x%2==0, my_list))

print(filterd_list)

# use with map

map_list = list(map(lambda x: x*x, my_list))
print(map_list)

# with reduce
reduced_list = reduce(lambda x,y: x+y, my_list)
print(reduced_list)