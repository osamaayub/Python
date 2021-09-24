# string Formating in python

# format()

string = "Hello Guys "
text = " {} This is Python Programming"
print(text.format(string))
# format the price as Two decimals
price = 49
text = "The price is {:.2f} dollars"
print(text.format(price))
# Multiple Values format
item = 43
count = 10
Number = 32
text = " Count is {} and Item is {} and the Number is {}"
print(text.format(item, count, Number))

# format Index Numbers
item = 34
count = 23
Number = 12
text = "Count is {0} and Item is {1} and the Number is {2}"
print(text.format(item, count, Number))
# Index Number
age = 24
Name = "Osama"
text = " His name is {1}. {1}  is {0} years old"
print(text.format(age, Name))
# Name Indexes
myorder = "I have a car {carname},  and its  Model is {carmodel}."
print(myorder.format(carname="Mustang GT ", carmodel=" 2019"))
