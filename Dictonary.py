# create a  Dictonary
thisdic = {'Name' : 'osama' , 'Age' : 23 , 'year' : 1999}
# print a Dictonary
print(thisdic)

# access the information in the Dictonary  with the help of the key
print(thisdic['Name'])
print(thisdic['year'])
#acesskeynamethroughget()functionsDictonary
y=thisdic.get("Name")
print(y)

#keys()function in the Dictonary
x=thisdic.keys()
print(x)
#Values() function in the Dictonary
y=thisdic.values()
print(y)
#items() function in the Dictonary
x=thisdic.items()
print(x)
#check if the key is present or not in the Dictonary

if "Name" in thisdic:
    print("key is present in the Dictonary")
if "color" not in thisdic:
    print("key is not present in the Dictionary")
#Add New item in the Dictionary
thisdic["School"]="BeaconHouseSchoolSystem"
print(thisdic)
# duplicates are not allowed in  Dictonary   it will overwrite it
thisdic['year'] = '2000'
print(thisdic)
#length of Dictionary
print(len(thisdic))

#TypeoftheDictonary
print(type(thisdic))
thisdic2={"Name": "osama" , "Age": 34 , "complex": 23j}
print(thisdic2)
# change the particular key's value
thisdic['Name']='Hamza'
print(thisdic)
#update() the Dictionary items
thisdic.update({"School": "CitySchool"})
print(thisdic)
thisdic.update({"Age" : 25})
print(thisdic)
#Add items in the Dictionary
thisdic["Education"]="Bachelor of Computer Science"
print(thisdic)
thisdic["CourseName"]="Artificial_Intelligence"
print(thisdic)
thisdic.update({"color" : "blue"})
print(thisdic)
#Remove items from the Dictionary
# pop() function
thisdic.pop("CourseName")
print(thisdic)
# popitem()function
thisdic.popitem()
print(thisdic)
# del function in dictionary
del thisdic['year']
del thisdic

#clear() function in Dictionary
thisdic2.clear()
print(thisdic2)

thisdic2={"Name": "osama" , "Age": 34 , "complex": 23j}
for i in thisdic2:
    print(i)
for i in thisdic2:
    print(thisdic2[i])
for i in thisdic2.values():
    print(i)


for i in thisdic2.items():
    print(i)
for i in thisdic2.keys():
    print(i)
#copy Dictionary in python
thisdic=thisdic2.copy()
print(thisdic)

#dict() for copying in the Dictionary
thisdic=dict(thisdic2)
print(thisdic)

# Nested Dictionary in python
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)