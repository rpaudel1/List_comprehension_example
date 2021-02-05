#using list comprehension
list_comp = [i for i in range(10)]
print('With List Comprehension:\n', list_comp)

# using regular loop and append method
list_append = []
for i in range(10):
	list_append.append(i)
print('With Append method:\n', list_append)
