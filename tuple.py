mytuple = ("may" , "June" , "july")
print(mytuple)

mytuple2 = ("may" , "june" , "july" , "may")
print(mytuple2)

mytuple3 = (1 , 2 , 4 , 5)
print(mytuple3)
print(len(mytuple))
mytuple4 = (True , True , False)
print(mytuple4)
print(type(mytuple4))

mytuple5 =tuple(("osama" , "Abeera" , "hamza"))
print(mytuple5)

print(mytuple5[0:2])

y = list(mytuple)
print(y)
y.append("August")
mytuple = tuple(y)
print(mytuple)
# join two tuples
mytuple6=mytuple4+mytuple5
print(mytuple6)



y = list(mytuple2)
y.remove("may")
mytuple4 =tuple(y)
print(mytuple4)

del mytuple3

# unpacking of a tuple
mytuple6 = ("apple" , "mango" , "grape")
(green , *red, blue) = mytuple6
print(green)
print(blue)
print(red)
# iterate tuple  through  for loop

mytuple3 = ("may" , "june" , "july" , "August" , "September")
for i in range(len(mytuple3)):
    print(mytuple3[i])
    # iterate through while loop
i = 0
while i < len(mytuple3):
    print(mytuple3[i])
    i+=1

# join two tuples
mytuple7=mytuple3+mytuple
print(mytuple7)
