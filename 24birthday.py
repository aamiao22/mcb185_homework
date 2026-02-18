import sys
import random

people = int(sys.argv[1])
days = int(sys.argv[2])
iterations = int(sys.argv[3])

sames = 0
for _ in range(iterations):
	calendar = [0] * days
	same_birthday = False
	for _ in range(people):
		print(calendar)
		bday = random.randint(0, days-1)
		calendar[bday] += 1
		if calendar[bday] == 2:
			same_birthday = True
			break
	
	same_birthday = False
	for v in calendar:
		if v > 1:
			same_birthday = True
			
	if same_birthday: sames += 1
		
print(sames/iterations)