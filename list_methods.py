list = [1,3,5,4,3,2]
list_one = ['a','d','c','b']

print("Original List:",list)

# List sorting
print("sorted list", sorted(list))

# Return the index of first occurrence of given items
print("index:", list.index(5))
print("Current List:",list)

# List reverse
print("reversed list:", list.reverse())

# List length
print("Length of list:",len(list))

# Min element of list
print("Min:", min(list))
print("Current List:",list)

# Max element of list
print("Max:", max(list))

# Returns the number of elements with the specified value
print("Count:", list.count(3))

# POP from list
print("POP:", list.pop())
print("Current List:",list)

# Adds an element at the specified position
list.insert(0,10)
print("Inserted list:", list)

# Sorts the list
list.sort()
print("sorted", list)


# Add the elements of a list (or any iterable), to the end of the current list
list.extend(list_one);
print(list)



