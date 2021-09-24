
x = 100
y = 20
z = 30
w = 40

if x<y:
    print("x is less than y")
elif x==y:
    print("x is  than y")
else:
    print("x is greater than y")
    #short Hand if
if x>y:print("x is greater than y")
#short hand if else
print("x is less than y") if x<y else print("x is greater than y")
# And operator condition if both true
if x>y and z<w:
    print("less")
#or condition  if one true
if x<y or w>z:
    print("more")
#Nested if statements
#Pass statement
if x>y:
    pass