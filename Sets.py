myset = {"May" , "June" , "July" , "August"}
print(myset)

print(len(myset))

print(type(myset))

for i in myset :
    print(i)
print("june" in myset)

myset.add("September")
print(myset)
myset2 = {"osama" , " Abeera" , "Autumn"}
# update items in set2 will be entered into set1
myset.update(myset2)
print(myset)

list = [1 , 2 , 3 , 4 , 5]
myset.update(list)
print(myset)
mytuple =("a" , "b" , "c" , "d")
myset.update(mytuple)
print(myset)
myset.remove("May")
print(myset)

# remove selected element from the set
myset.discard("a")
print(myset)

# pop out element out of the set
myset.pop()
print(myset)

#clear the set elements
myset.clear()
print(myset)

del myset

#print a set through Loop
for x in myset2:
    print(x)

# join two set union()
myset={'summer' , 'winter' , 'Autumn', 'summer'}
myset.union(myset2)
print(myset)

# it will only print duplicates
myset.intersection(myset2)
print(myset)
# it will only print the duplicate items in the set
myset.intersection_update(myset2)
print(myset)
# keep all the items and duplicates
myset.symmetric_difference(myset2)
print(myset)
# keep all the items but not duplicates or not same
myset.symmetric_difference_update(myset2)
print(myset)
myset.difference(myset2)
print(myset)
myset.difference_update(myset2)
print(myset)
myset={'osama'  , 'Autumn'  , 'Abeera'}
myset.issubset(myset2)
print(myset)
myset.isdisjoint(myset2)
print(myset)

myset.issuperset(myset2)
print(myset)