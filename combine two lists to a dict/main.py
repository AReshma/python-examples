'''
combine two lists to a dict, where items from one list will be the keys and
items from second list will become the values.
example,
list1 = [89, 23, 42, 1, 39, 29, 90]
list2 = ['jay', 'jack','ken','rose','diana','mary','paul']
expected dict : {89: 'jay', 23: 'jack', 42: 'ken', 1: 'rose', 39: 'diana', 29: 'mary', 90: 'paul'}
'''

list1 = [89, 23, 42, 1, 39, 29, 90]
list2 = ['jay', 'jack','ken','rose','diana','mary','paul']

# Using 'zip'
result = {}
for k, v in zip(list1, list2):
    result[k] = v

print(f"1. Using 'zip' : \n\t{result}")

# traditional 'for' loop
result = {}
for i in range(len(list1)):
    result[list1[i]] = list2[i]
print(f"2. using traditional 'for' loop :  \n\t{result}")

# using  'for' loop in single line
result = {}
result = { list1[i]: list2[i] for i in range(len(list1)) }
print(f"3. using  'for' loop in single line :  \n\t{result}")

# using 'dict' and 'zip'
result = {}
result = dict(zip(list1, list2))
print(f"4. using 'dict' and 'zip':  \n\t{result}")

# using fromkeys() method
result = {}
result = dict.fromkeys(list1)
for k, v in zip(result.keys(), list2):
    result[k] = v
print(f"5. using 'fromkeys()' method:  \n\t{result}")
