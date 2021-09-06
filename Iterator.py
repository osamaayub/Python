mytupple=('apple','Mango','banana')
myit=iter(mytupple)
print(next(myit))
print(next(myit))
print(next(myit))

string='HelloWorld!'
myit=iter(string)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
""""
# iterate the tupple objects through for loop
for x in mytupple:
    print(x)

# iterate the string through for loop
for x in string:
    print(x)
    
# create an iterator
class student:
    def __iter__(self):
       self.a = "osama"
       return self
    def __next__(self):
        x=self.a
        return x
    
        
myclass = student()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
"""

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
       if self.a <= 20:
           x = self.a
           self.a += 1
           return x
       else:
          raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)