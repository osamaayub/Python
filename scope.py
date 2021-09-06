# python scope 
#Local Scope
def mysum():
    sum=767
    print(sum)
mysum()
#global scope
sum=756
def mysum():
    sum=767
    print(sum)
mysum()
print(sum)