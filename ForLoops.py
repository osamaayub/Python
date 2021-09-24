List=["may","june"]
for i in List:
    print(i)

# print a tuple

tuple=("may","june")
for i in tuple:
    print(i)
# print a string:
x=["banana","Grape"]
for i in "x":
    print(i)
# break statement

for i in "x":
    if i=="x":
     break
     print(i)
# continue statement
for i in "x":
    if i=="x":
     continue
     print(i)
# Range function
for i in range(5):
    print(i)
# two ranges in for loop
for i in range(2,5):
    print(i)
# 3 ranges in for loop
for i in range(1,2,6):
    print(i)
# else in for loop

for i in range(3):
    print(i)
else:
    print("loop finished")
# Nested for Loops
number=1
for i in range(1,10):

    for j in range(0,i+1):
        print(number,end=" ")
        number=number+1
    print("\r")