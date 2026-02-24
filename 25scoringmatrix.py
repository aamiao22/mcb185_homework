import sys

alph = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]

#print the header
print('  ', end='')
for c in alph: print(c, end='  ')
print()

#print the side
for i in range(len(alph)):
	print(alph[i], end=' ')
	for j in range(len(alph)):
		if i == j: print(mat, end=' ')
		else:		print(mis, end=' ')
	print()
