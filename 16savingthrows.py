import random

def d20():
	return random.randint(1,21)
	
def roll(mode):
	r1 = d20()
	if mode == 'normal':
		return r1
	r2 = d20()
	if mode == 'advantage':
		if r1 > r2: return r1
		else: return r2
	else: 
		if r1 < r2: return r1
		else: return r2
		
def estimate(dc, mode, trials):
	wins = 0
	for i in range(trials):
		if roll(mode) >= dc:
			wins += 1
		return wins / trials
		
trials = 10000
for dc in (5, 10, 15):
	for mode in('normal', 'advantage', 'disadvantage'):
		print('DC', dc, mode, estimate(dc, mode, trials))
	print('---')