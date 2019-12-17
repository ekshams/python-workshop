# first min, first max, second min, secon max etc

lst = [6,8,9,10,7,15,14,13,11]


# out put should be
[6,15,7,9]

print(lst)
print(sorted(lst))  
print("---------")

# lst.sort(key=lambda x: (len(x.split())>1, x if len(x.split())==1 else int(x.split()[-1]) ) )
lst.sort()

i=0
j=-1
new_lst = []
half_length = len(lst)/2
while i < half_length:
    # print(i,j)    
    new_lst.append(lst[j])
    if lst[i] != lst[j]:
        new_lst.append(lst[i])
        
    i = i + 1
    j = j - 1
    
    
print(new_lst)

# n_lst = [x for x in lst[0:]]

# print(n_lst)