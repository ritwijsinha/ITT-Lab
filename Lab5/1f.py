#DP FTW
def fib(n,l):
	if len(l) >= n:
		return l[n-1]
	else:
		l.append(fib(n-1,l)+fib(n-2,l))
		return l[n-1]
l = [0,1,1,2]
fib(input(),l)
print l