#create a module

def mystring(str):
    print(str+"Hello")
person={"Name":"osama","Age":23}
List=['apple','banana','orange']
# use the module
# Naming a Module
import Module1
Module1.mystring("World")
b=Module1.person["Name"]
c=Module1.List[0]
print(b)
print(c)
# renaming a Module
import Module1 as mx
b=mx.person["Age"] 
print(b)
c=mx.List[1]
print(c)

# built in module platform
import platform
x=platform.system()
print(x)
# built in  module dir 
import platform
x=dir(platform)
print(x)
#from keyword
from Module1 import person
print(person["Age"])

