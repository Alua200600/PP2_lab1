x = 5
y = "John"
print(x)
print(y)
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
x = 5
y = "John"
print(type(x))
print(type(y))
x = "John"
# is the same as
x = 'John'
a = 4
A = "Sally"
#A will not overwrite a
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
#2myvar = "John"
#my-var = "John"
#my var = "John"
#This example will produce an error in the result
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

