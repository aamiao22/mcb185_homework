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
		
#		if distance < min_distance:
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


#import sys
#import itertools

#def translate(orf):  #36
#	codons = [''.join(t) for t in itertools.product('ACGT', repeat=3)]
#	trans = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'
#	prot = '' #prot = []
#	for i in range(0, len(orf), 3):
#		codon = orf[i:i+3]
#		idx = codons.index(codon)
#		aa = trans[idx]
#		prot += aa #prot.append(aa)
#		
#	return prot
#	
#protein = translate('ATAGCGAAT')
#print(protein)

#import random
#import sys

#def random_subseq(seq, n, k):
#	subs = []
#	for _ in range(n):
#		x = random.randint(0, len(seq) -k)
#		subseq = seq[x:x+k]
#		subs.append(subseq)
#	return subs

#seq = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 10 + 26 = 36
#subseqs = random_subseq(seq, 15, 7)
#print(subseqs)

#new
#import random
#import sys

#def anti(subseq):
#	rev = seq[::-1]
#	rc = ''
#	for nt in rev:
#		if nt == 'A': rc += 'T'
#		elif nt == 'C': rc += 'G'
#		elif nt == 'G': rc += 'C'
#		elif nt == 'T': rc += 'A'
#	return rc

#def shotgun_simu(seq, n, k):
#	subs = []
#	for _ in range(n):
#		x = random.randint(0, len(seq) -k)
#		subseq = seq[x:x+k]
#		if random.random() < 0.5: subseq = anti(subseq)
#		subs.append(subseq)
	
#	return subs

#seq = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#subseqs = shotgun_simu(seq, 15, 7)
#print(subseqs)

## 40 mutated dna:
#import random
#import sys

#def mutate(s, p):
#	seq = list(s)
#	for i in range(len(seq)):
#		if random.random() < p:
#			if seq[i] == 'A': seq[i] = random.choice('CGT')
#			elif seq[i] == 'C': seq[i] = random.choice('AGT')
#			elif seq[i] == 'G': seq[i] = random.choice('ACT')
#			elif seq[i] == 'T': seq[i] = random.choice('AGC')
#	return ''.join(seq)

#dna = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
#dna = mutate(dna, 0.2)
#print(dna)


#import random

#def random_dna(n):
#	seq = ''
#	for _ in range(n):
#		seq += random.choice('ACGT')
#	return seq

#for i in range(5):
#	print(i, random_dna(10))


##
#import random
##import math
#def random_dna(n, X=[0.25, 0.25, 0.25, 0.25]):
	##if not math.isclose(1.0, sum(X)): sys.exit('oops')
#	a = X[0]
#	c = X[0] + X[1]
#	g = X[0] + X[1] + X[2]
#	rseq = ''
	
#	for _ in range(n):
#		r = random.random()
#		if r < a: rseq += 'A'
#		elif r < c: rseq += 'C'
#		elif r < g: rseq += 'G'
#		else:		rseq += 'T'
#	return rseq

#for i in range(5):
#	print(i, random_dna(10, X=[0.7, 0.1, 0.1, 0.1]))


##weights:
#import random

#def random_dna(n, X=[0.25, 0.25, 0.25, 0.25]):
#	total = sum(X)
#	a = X[0]/total
#	c = (X[0] + X[1]) / total 
#	g = (X[0] + X[1] + X[2]) / total
#	rseq = ''
	
#	for _ in range(n):
#		r = random.random()
#		if r < a: rseq += 'A'
#		elif r < c: rseq += 'C'
#		elif r < g: rseq += 'G'
#		else:		rseq += 'T'
#	return rseq

#for i in range(5):
#	print(i, random_dna(10, X=[0.7, 0.1, 0.1, 0.1]))

##25scoringmatrix:

#import sys

#alph = sys.argv[1]
#mat = sys.argv[2]
#mis = sys.argv[3]

##print the header
#print('  ', end='')
#for _ in range(len(alph)):
#	print(alph[i], end=' ')
#print()

##print the side
#for i in range(len(alph)):
#	print(alph[i], end=' ') # print the rest
#	for j in range(len(alph)):
#		if i == j: print(mat, end='')
#		else:		print(mis, end='')
#	print('\n')

##same example:
#import sys

#alph = sys.argv[1]
#mat = sys.argv[2]
#mis = sys.argv[3]

##print the header
#print('  ', end='')
#for c in alph: print(c, end='  ')
#print()

##print the side
#for i in range(len(alph)):
#	print(alph[i], end=' ')
#	for j in range(len(alph)):
#		if i == j: print(mat, end=' ')
#		else:		print(mis, end=' ')
#	print()

#def minimum(vals):
#       mini = x[0]
#       for val in vals[1:]:
#           if val < mini: mini = val
#       return mini

#x = [3.14, 2.719, 1/7, 0, -2, 1]
#print(minimum(x))

#seq = input('Enter your sequence:')
#c = seq.count('C')
#g = seq.count('G')
#print(c, g, len(seq), (c+g) / len(seq))

#def crazy(s):
#	up = True
#	cl = []
#	for c in s:
#		if up: cl.append(c.upper())
#		else:	cl.append(c.lower())
#		up = not up
#	return ''.join(cl)
#
#filename = sys.argv[1]
#with open(filename) as fp:
#	for line in fp:
#		crazyline = crazy(line)
#		print(crazyline)


#def anti(dna):
#	rev = dna[::~1]
#	comp = ''
#	for nt in rev:
#		if nt == 'A': comp.append('T')
#		elif nt == 'C': comp.append('G')
#		elif nt == 'G': comp.append('C')
#		elif nt == 'T': comp.append('A')
#
#
#
#
#def longest_str(strings):
#	longest = s[0]
#	for s in strings[1:]:
#		if len(s) > len(longest):
#			longest = s 
#	return longest, len(longest)
#
#string = ['hello world', 'pi', '3.14159', 'mouserat']
#print(longest_str(strings))
#
#
#def highest_tm(oligns):
#	tm_max = tm(seqs[0])
#	save_seq = seqs[0]
#	
#	for seq inn seqs[1:]:
#		mytm = tm(seq)
#		if mytm > tm_max:
#			tm_max = mytm
#			save_seq = seq
#
#	return tm_max, save_seq
#
#oligos = ['ACGATTATT', 'CAATATCGATA', 'AAAAAAAAAAAAAAAA', 'ACG']
#print

#def minnmax(vals):
#	a = vals[0]
#	b = vals[0]
#	for val in vals[1:]:
#		if val < a: a = val
#		if val > b: b = val
#	return a,b

#def mymin(vals):
#	minval = vals[0]
#	for val in vals:
#		if val < minval: minval = val
#	return minval

#def minnmax2(vals):
#	myvals = vals.copy()
#	myvals.sort()
#	return myvals[0], myvals[-1]
#
#stuff = [3, -1, 0, 5, 21, 8]
#print(minmax(stuff))


#nucleotides = nts
#nucleotides.append('C')
#nucleotides.sort()
#print(nts, nucleotides)



































