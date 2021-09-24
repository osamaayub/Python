
# open a file in python using open() function
import os
f = open("input.txt")
# read a text file
f = open("input.txt", "rt")
# read data from a file
f = open("input.txt", "rt")
print(f.read())
# read  data into file up to 6 characters
f = open("input.txt", "rt")
print(f.read(6))
# read one line from the file
f = open("input.txt", "rt")
print(f.readline())
# Loop through the contents of a file
for x in f:
    print(x)
# closing the files
f = open("input.txt", "rt")
print(f.read())
f.close()
# writing to an existing file using append
f = open("input.txt", "a")
f.write("Welcome To Python Programming Language")
f.close()
# overwrite the contents of a file using write
f = open("input.txt", "w")
f.write("Welcome to Python Programming Tutorial")
f.close()
# create a New file in python
f = open("test.txt", "x")
f.close()
