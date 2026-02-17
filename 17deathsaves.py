import random
print('start')

def one_game():
	successes = 0
	failures = 0
	while successes < 3 and failures < 3:
		r = random.randint(1, 20)
	
	if r == 20:
		return 'revive'
	elif r == 1:
		failures += 2
	elif r < 10:
		failures += 1
	else:
		successes += 1
		
	if failures >= 3:
		return 'die'
	else:
		return 'stable'
		
N = 10000
die = 0
stable = 0
revive = 0

for i in range(N):
	result = one_game()
	if result == 'die':
		die += 1
	elif result == 'stable':
		stable += 1
	else:
		revive += 1
		
print('die', die / N)
print('stable', stable / N)
print('revive', revive / N)