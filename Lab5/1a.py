def f(a,b,c):
    return {'+': a+c, '-': a-c, '*': a*c, '/': a/c}.get(b)
a = input("Enter first number: ")
b = raw_input("Enter operator: ")
c = input("Enter second number: ")
print "Ans:",f(a,b,c)
