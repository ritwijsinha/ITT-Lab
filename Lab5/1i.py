a = raw_input("Enter list elements: ").split()
print ("Palindrome" if a==a[::-1] else "Not a Palindrome")