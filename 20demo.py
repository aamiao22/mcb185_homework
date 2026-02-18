s1 = 'hello'
s2 = 'world'
s = s1 + s2

#print(s1,s2,len(s))
#print(s.upper())
#print(s)
#print(s.replace('o',''))

nts = 'ACGT'
#for i in range(len(nts)):
	#print(i, nts[i])

#nts = 'ACGT'
#for i, nt in enumerate (nts):
#	print (i,nt)

#import sys

#nums = []
#for i in sys.argv[1:]:
#	nums.append(int(i))

#print('sum =', sum(nums))

#nts = ['A', 'G', 'T'] 
#nucleotides = nts
#nucleotides.append('C')
#nucleotides.sort()
#print(nts, nucleotides)

#birthday problem:
#ask everyone, do diagonal asking so people don't need to ask the same one again
#make a calendar for solving it, calendar with 365 values
#
#1st way:

#import sys
#import random

#people = int(sys.argv[1])
#calendar = int(sys.argv[2])
#iterations = int(sys.argv[3])

#people = 5 #23
#calendar = 50 #365

#sames = 0
#for _ in range(iterations): 
#	classroom = []
#	for i in range(people):
#		birthday = random.randint(0, calendar-1)
#		if birthday in classroom:
#			same_birthday = True
#			break
#		classroom.append(birthday)
	
#	same_birthday = False
#	for i in range(0, len(classroom)):
#		for j in range(i+1, len(classroom)):
#			if classroom[i] ==  classroom [j]: 
#			same_birthday = True
#			break
			
#	if same_birthday: sames += 1 
	
#print(sames/iterations)


#import sys
#import random

#people = int(sys.argv[1])
#calendar = int(sys.argv[2])
#iterations = int(sys.argv[3])

#sames = 0
#for _ in range(iterations):
#    calendar = [0] * days
#    same_birthday = False
#	for _ in range(people):
#		print(calendar)
#		bday = random.randint(0, days-1)
#		if calendar[bday] == 1:
#			same_birthday = True
#			break
	
#	same_birthday = False
#	for v in calendar:
#		if v > 1:
#			same_birthday = True
			
#	if same_birthday: sames += 1
		
#print(sames/iterations)

#import sys
#import random

#genome_size = int(sys.argv[1])
#coverage = int(sys.argv[2])
#iterations = int(sys.argv[3])

#genome = [0] * genome_size

#for i in range(genome_size * coverage):
#	pos = random.randint(0, genome_size-1)
#	genome[pos] += 1

##zeroes = 0
##for v in range genome:
##	if v < 10: zeroes += 1
##print(1 - zeroes/genome_size)

#print(genome)

#import sys

#vals = []
#for s in sys.argv[1:]:
#	vals.append(float(s))

#vals.sort()
#total = 0

#for val in vals: total += val
#mean = total/len(vals)

#m = len(vals) // 2
#if len(vals) % 2 == 1:
#	median = vals[m]
#else:
#	median = (vals[m] + vals[m-1]) / 2

#print('minimum', vals[0])
#print('maximum', vals[-1])
#print('range', vals[-1]-vals[0])
#print('average', mean)
#print('median', median)

#manhattan distance and dkl 

#import math
#def manhattan(X1, X2):
#	distance = 0
#	for x1,x2 in zip(X1, X2):
#		distance += abs(x1 - x2)
#	return distance

#def dkl(P, Q):
#	if not math.isclose(1.0, sum(P)): sys.exit('error')
#	if not math.isclose(1.0, sum(Q)): sys.exit('error')
#	distance = 0
#	for p, q in zip(P, Q):
#		if p == 0: continue  #telling it to skip
#		if q == 0: continue
#		distance = p * math.log2(p/q) #if either q,p is 0, it won't work
#	return -distance
	
#def pairwise_percent(s1, s2):
#	diff = 0
#	for c1, c2 in zip(s1, s2):
#		if c1 != c2: diff += 1
#	return 1 - diff / len(s1)

	
#a = [0.4, 0.3, 0.2, 0.1]
#b = [0.25, 0.25, 0.25, 0.25]

#s1 = 'ACGATATACAGTA'
#s2 = 'ACGATAGACAGTA'


#print(manhattan(a,b))
#print(dkl(a,b))
#print(pairwise_percent(s1,s2))

#import sys

#def get_list_from_file(filename):
#	strings = []
#	with open(filename) as fp:
#		for line in fp:
#			string.append(line.rstrip())
#	return strings

#def jaccard(f1, f2):
#	X1 = get_list_from_file(f1)
#	X2 = get_list_from_file(f2)
#	unique_a = []
#	unique_b = []
#	shared = []
#	for x1 in X1:
#		if x1 is X2: shared.append(x1)
#		else:		unique_a.append(x1)	
#	for x2 in X2:
#		if x2 not in X1: unique_b.append(x2)
#	print(unique_a)
#	print(unique_b)
#	print(shared)
#	return len(shared) / (len(shared) + len(unique_a) + len(unique_b))

#file1 = sys.argv[1] 
#file2 = sys.argv[2]

#print(jaccard(file1, file2)) #then put your file names up after your commands.

# what's dis and color name?
#2 40 81 (aggie blue)
#255 191 0 (aggie gold)

#import sys


#filename = sys.argv[1]
#target_r = int(sys.argv[2])
#target_g = int(sys.argv[3])
#target_b = int(sys.argv[4])

#min_distance = 1000
#min_color = None
#discrepancy = 0

#with open(filename) as fp:
#	for line in fp:
#		#parts = line.split()
#		#rgbs = parts[2].split(',')
#		#print(rgbs)
#		colorname, hexvalue, rgbs, = line.split()
#		r, g, b= parts[2].split(',')
#		distance = 0
#		distance += abs(target_r - int(r))
#		distance += abs(target_g - int(g))
#		distance += abs(target_b - int(b))
#		print(colorname, distance)
		
#		if distance < min_distance
#			discrepancy = abs(distance - min_distance)
#			min_distance = distance
#			min_color = colorname
				
#print(min_color, discrepancy)

#new problem following: hydropathy(pro)

#def hydropathy(seq):
#	aas = 'ACDEFGHIKLMNPQRSTVWY'
#	kdh = (1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6,
#	-3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3)
#
#	total = 0
#	for aa in seq:
#		idx = aas.index(aa)
#		total += kdh[idx]
		
#	return total / len(seq)

#print(hydropathy('MVPSSQLDRP'))

#def translate(seq):  #not done yet
#	codons = [''.join(t) for t in itertools.product('ACGT', repeat=3)]
#	trans = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'
#	print(codon)
#	print(trans)
#	return hello

#print(translate('ATGGTGTAA'))


##monty-pi-thon.py:

#import random

#inside = 1
#outside = 1
#total = 0

#for i in range(10000):
#	total += 1
#	x = random.random()
#	y = random.random()
#	d = (x ** 2 + y**2) ** 0.5
#	if d > 1: outside += 1
#	else:		inside += 1
#	print(4 * inside / (inside + outside), total)






























