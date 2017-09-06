a = raw_input("Enter a string: ")
print ''.join([x for x in a if x.isalnum() or x == ' '])