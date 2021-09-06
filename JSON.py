import json
# convert json string to python dictionary json.loads()
x='{"Name":"osama","Age":23,"Year":1999}'
y=json.loads(x)
print(y["Name"])

# convert python dictionary to json string json.dumps()
x={
    "Name":"osama",
    "Age":23,
    "Year":1999
   }
y=json.dumps(x)
print(x)
import json
#convert the python objects into json strings
x=["apple","banana","Mango"]
print(json.dumps(x))