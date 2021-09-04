# RegEx Module to check if the searched pattern is string or not
import re
string = "Hello,World"
x = re.search("World", string)
# returns the start and End index of string
print(x.span())
# returns the string where there is a Match
print(x.group())
# print the string
print(x.string)
# if match found then return the whole string
x = re.findall("HelloWorld", string)
print(x)
# split a string into a List
x = re.split(string, "Hello")
print(x)
# replaces one or many matches with the string
x = re.sub("World", "OsamaAyub", string)
print(x)
