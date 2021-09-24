import os

if os.path.exists("input.txt"):
    os.remove("input.txt")
elif not os.path.exists("input.txt"):
    print("file  does not exits")
