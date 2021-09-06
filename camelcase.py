# pip install camelcase
import camelcase

c = camelcase.CamelCase()
string = "welcome to python programming"
code = c.hump(string)
print(code)
