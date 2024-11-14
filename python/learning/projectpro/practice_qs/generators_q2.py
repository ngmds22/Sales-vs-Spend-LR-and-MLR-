# Generator functions use the yield keyword instead of return
# return will return a value and exit the function
# yield will return a value and pause the function, allowing it to be resumed later
def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30

# This creates a generator object but does not execute the function immediately
# The function will only start when you explicitly ask for the next value
g = mygenerator()
# First next(g) will execute all code before the first yield statement in the generator
# it will print "First item", returns 10 and pauses the function
# a = 10
a = next(g)
b = next(g)
c = next(g)
print(a,b,c)

# If you try to iterate further, you will recieve a StopIteration exception