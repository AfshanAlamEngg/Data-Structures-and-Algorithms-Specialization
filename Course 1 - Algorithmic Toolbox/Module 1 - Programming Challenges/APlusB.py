# take input
a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))

# define a function
def APlusB(a, b):
    # do computation
    sum = a + b
    # return sum 
    return sum

# print sum
print(f"Sum of a and b is {APlusB(a,b)}")