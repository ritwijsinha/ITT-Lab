import re
a = raw_input("Enter a string: ")
b = raw_input("Enter the string to search: ")
c = raw_input("Enter the string to replace: ")
a = re.sub(b,c,a)
print a