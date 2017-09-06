print "Enter Matrix 1:"
m1 = [[int(x) for x in raw_input().split()] for x in range(3)]
print "Enter Matrix 2:"
m2 = [[int(x) for x in raw_input().split()] for x in range(3)]
m3 = [[a+b for a,b in zip(i,j)] for i,j in zip(m1,m2)]
for i in m3:
	print i