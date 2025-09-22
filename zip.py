letters = ['a','b','c']
numbers = [1,2,3]

# zip makes a tuple for each element in argument list.
# but it is a generator! ==> need to convert to list to see anything.
assert list(zip(letters , numbers)) == [('a', 1), ('b', 2), ('c', 3)]

# You can zip any number of lists like so:
zipped_things = [letters, numbers, reversed(letters)]
print(list(zip(
    *zipped_things
)))

# In this example we could just have provided zip arguments directly:
print(list(zip(
    letters, numbers, reversed(letters)
)))

# zip(*...) is useful when we don't have the whole list known at the time we write the program.
