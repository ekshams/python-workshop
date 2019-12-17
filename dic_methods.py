my_dic = {}

my_dic['name'] = 'Shams'
my_dic['age'] = 31
my_dic['place'] = 'Muthanur'

print(my_dic)
copy = my_dic.copy()
print(copy)

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

print(my_dic.get('name'))

print(my_dic.items())

my_dic.update({"pin":673641})
print(my_dic)


