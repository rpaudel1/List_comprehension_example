# List_comprehension_example
# This is a simple exmaple of list comprehension in python
#using list comprehension
x = [i for i in range(10)]
print('With List Comprehension:\n', x)

# using regular loop and append method
x = []
for i in range(10):
	x.append(i)
print('With append method:\n', x)
