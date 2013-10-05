f = open('x-acc.csv')
for line in f:
	cols = line.split(',')
	print cols[1]
