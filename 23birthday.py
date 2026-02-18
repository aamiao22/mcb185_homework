import sys
import random

people = int(sys.argv[1])
calendar = int(sys.argv[2])
iterations = int(sys.argv[3])

sames = 0
for _ in range(iterations): 
	classroom = []
	same_birthday = False
	
	for i in range(people):
		birthday = random.randint(0, calendar-1)
		if birthday in classroom:
			same_birthday = True
			break
		classroom.append(birthday)
	
	if same_birthday: sames += 1 
	
print(sames/iterations)