def is_prime(n):
	for i in range(3, n, 2):
		print('checking', i)
		r = n % i
		if r == 0: return False
	return True

for i in range(1, 101,10):
	print(i, end=' ')
	if i % 15 == 0: print('fizzbuzz', end='')
	elif i % 3 == 0: print('fizz', end='')
	elif i % 5 == 0: print('buzz', end='')
	print()
