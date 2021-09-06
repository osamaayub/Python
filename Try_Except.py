# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exeption Handling
from os import write


try:
    print("x")
except:
    print("eror occured")
finally:
    print("code executed")
# Many Exeptions

try:
    print(NameError)
except NameError:
    print("error Handle")
except:
    print("code executed")
# else
try:
    print("Hello")
except:
    print("World")
else:
    print("code Executed")
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")
