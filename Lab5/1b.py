matrix=[[int(x) for x in raw_input().split()] for x in range(3)]
t_matrix = map(list,zip(*matrix))
for i in t_matrix:
	print i