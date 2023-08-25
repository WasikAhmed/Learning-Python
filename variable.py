# Variables are containers for storing data values.
# Python has no command for declaring a variable.

## Declaring variable
a = 4 # int
print(a)
print(type(a)) # print the datatype of variable using type() function
b = 6.9 # decimal
c = True # boolean
d = "10" # string   single('') or double("") quotes both are same when declaring string


## Type Casting
a = float(a) # integer to float
print(a)
print(type(a))

b = int(b) # float to integer
print(b)
print(type(b))

d = int(d) # string to integer
print(d)
print(type(d))


# myVariable = "This" (Camel Case)
# MyVariable = "is" (Pascal Case)
# my_variable = "landladesh" (Snake Case)

m, n, o, p = 'here', 'we', 'go', 'again'
print(m, n, o, p)
print(m + n + o + p)

x = y = z = 'Hello, World!'
print(x, y, z)

## Global Variables : 
# Variables that are created outside of a function are known as global variables

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)

# use global keyword to change a global variable inside a function
def newfunc():
    global x
    x = "Hello"
    print(x)

newfunc()