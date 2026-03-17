#import sys

#filename = sys.argv[1]

##seq = ''
#seq =[]
#with open(filename) as fp:
#	for line in fp:
#		seq += 
#		seq.append(line.rstrip())
#seqline = ''.join(seq[1:])
#words = seq [0]
#uid = words.split()[0][1:]	##'>something out here
##print(seqline)
#print(uid, len(seqline))

##----------------------

#import sys
#import mcb185

#filename = sys.argv[1]

#def read_fasta(filename):
#	seq =[]
#	with open(filename) as fp:
#		for line in fp:
#			seq.append(line.rstrip())
#	seqline = ''.join(seq[1:])
#	words = seq [0]
#	uid = words.split()[0][1:]
#	return uid, seqline

#uid, seq = read_fasta(sys.argv[1])
#print(uid, seq)

##new------------

#import sys
#import mcb185

#for defline, seq in mcb185.read_fasta(sys.argv[1]):
#	print(defline, pro)
#	for frame in range(3):
#		pro = mcb185.translate(seq[frame:])
#		print('', pro)		#partial ones will translate into "X"


###-----------------------

#import random

#def random_word_list(n, k):
#	words = []
#	for i in range(n):
#		word = ''
#		for j in range(k):
#			letter = random.choice('ABCDEFGHIJ')
#			word += letter
#		words.append(word)
#	return words

#words = random_word_list(30, 5)
#print(words)

###--------------------------

#import random

#def random_word_list(n, k):
#	words = []
#	for i in range(n):
#		word = ''
#		for j in range(k):
#			letter = random.choice('ABCDEFGHIJ')
#			word += letter
#		words.append(word)
#	return words

#size = 10_000
#words1 = random_word_list(size, 5)
#words2 = random_word_list(size, 5)

#found = 0
#for word in words1:
#	if word in words2:
#		found += 1
#print('hooray, found', found)

###----------------------------

#import random						#O(n) = 'order n', introducing a binary search

#def random_word_list(n, k):			#dictionary works better than binary even. 
#	words = set()					#this unit is more about how to make a dictionary to make it more easier.
#	for i in range(n):
#		word = ''
#		for j in range(k):
#			letter = random.choice('ABCDEFGHIJ')
#			word += letter
#		words.append(word)
#	return words

#size = 10_000
#words1 = random_word_list(size, 5)
#words2 = random_word_list(size, 5)

#found = 0
#for word in words1:
#	if word in words2:
#		found += 1
#print('hooray, found', found)

###---------------------------------------

#def entropy(seq):
#	pa = seq.count('A') / len(seq)
#	pc = seq.count('C') / len(seq)
#	pg = seq.count('G') / len(seq)
#	pt = seq.count('T') / len(seq)
#	h = 0
#	if pa != 0: h -= pa * math.log2(pa)
#	if pc != 0: h -= pc * math.log2(pc)
#	if pg != 0: h -= pg * math.log2(pg)
#	if pt != 0: h -= pt * math.log2(pt)
#	return h

#seq = 'ACTATATATATCGAAAGGTCCAGA'
#w = 5
#t = 1.5
#for i in range(len(seq) -w +1):
#	win = seq[i:i+w]
#	h = entropy(win)
#	if h < t: print(i, win, h)

####-------------------------------------

#def entropy(seq):
#	pa = seq.count('A') / len(seq)
#	pc = seq.count('C') / len(seq)
#	pg = seq.count('G') / len(seq)
#	pt = seq.count('T') / len(seq)
#	h = 0
#	if pa != 0: h -= pa * math.log2(pa)
#	if pc != 0: h -= pc * math.log2(pc)
#	if pg != 0: h -= pg * math.log2(pg)
#	if pt != 0: h -= pt * math.log2(pt)
#	return h

#seq = 'ACTATATATATCGAAAGGTCCAGA'
#w = 5
#t = 1.5
#mask = list(seq)
#for i in range(len(seq) -w +1):
#	win = seq[i:i+w]
#	h = entropy(win)
#	if h < t:
#		for j in range(i, i+w):
#			mask[j] = 'N'
#print(''.join(mask))
			
###-------------------------------------

#42, helps with 43

#for a in range(1, 15):
#	for b in range(a+1, 15):
#		c = (a ** 2 + b ** 2) ** 0.5
#		if c % 1 != 0: continue
#		print(a, b, c)
		#seen.append((b, a)) introduce it makes things complicated
		
#stuff = ('A', 'B', 'C', 'D')		
#for i in range(len(stuff)):
#	for j in range(len(stuff)):
#		print(stuff[i], stuff[j])

#stuff = ('A', 'B', 'C', 'D')		
#for i in range(len(stuff)):
#	for j in range(i, len(stuff)):
#		print(stuff[i], stuff[j])

#######################################

#43

#import random
#import sys
#cal = int(sys.argv[1])
#num = int(sys.argv[2])

#birthdays = list()
#for _ in range(num):
#	birthdays.append(random.randint(0, cal-1))

#print(birthdays)


#import random
#import sys
#cal = int(sys.argv[1])
#num = int(sys.argv[2])

#shared_birthdays = 0#
#rounds = 50#
#for g in range(50):#
#	shared = False
#	birthdays = list()
#	for _ in range(num):
#		birthdays.append(random.randint(0, cal-1))
#	for i in range(num):
#		for j in range(i+1, num):
#			if birthdays[i] == birthdays [j]:
#				shared = True
#	#if shared: print('hooray')
#	#else:		print('not this time')
#	if shared: shared_birthdays += 1
#print(shared_birthdays/rounds)

##############################################################

#44 a calendar on the wall that won't use a list

#import random
#import sys
#cal = int(sys.argv[1]) #days in year
#num = int(sys.argv[2]) #people number

#shared = False	
#calendar = [0] * cal #before adding date, it will be 0s.
#for _ in range(num):
#	date = random.randint(0, cal-1)
#	calendar[date] += 1
#for date in range(cal):
#	if calendar[date] > 1: shared = True
#if shared: print('hooray')
#else:		print('not this time')

#################################################################

#46

#def char_count(s):
#	pass
#
#s = 'hello	this is fun!'
#characters = []
#char_count = []
#for c in s:
#	if c not in characters:
#		print('first time seeing', c)
#		characters.append(c)
#		char_count.append(1)
#	else:
#		print('seen', c, 'before, adding 1')
#		idx = characters.index(c)
#		char_count[idx] += 1

#for c, n in zip(characters, char_count):
#	if ord(c) <= 32: print(f'<{ord(c)}', n)
#	else:			print(c, n)
#_____

#def char_count(s):
#	pass
#
#s = 'hello	this is fun!'
#characters = []
#char_count = []
#for c in s:
#	if c not in characters:
#		print('first time seeing', c)
#		characters.append(c)
#		char_count.append(1)
#	else:
#		print('seen', c, 'before, adding 1')
#		idx = characters.index(c)
#		char_count[idx] += 1

#for i in range(len(characters)):
#	print()

####

#s = 'helllo	this is fun!'
#chars = [0] * 128
#for c in s:
#	#ascii_val = ord(c)
#	chars[ord(c)] += 1
#for i in range(len(chars)):
#	if chars[i] == 0: continue
#	print(ascii(i), chars[i])

###################################################

#49 VERY IMPORTANT!!!!!!!!!!!!!!!!!!

#seq = 'ACGTACGTAAAAAAAAAAACGTACGT'
#hard = 'ACGTACGTNNNNNNNNNNCGTACGT'
#soft = 'ACGTACGTaaaaaaaaaaCGTACGT'

#entropy function need:
#import math
#def entropy(seq):
	#pa = seq.count() --------
	#-----------
	#h = 0
	#if pa != 0: h -= pa * math.log2(pa)
	#if pc != 0: h -= pc * math.log2(pc)
	#if pg != 0: h -= pg * math.log2(pg)
	#if pt != 0: h -= pt * math.log2(pt)


#seq = 'ACGTACGTAAAAAAAAAAACGTACGT'
#hard = 'ACGTACGTNNNNNNNNNNCGTACGT'

#print(entropy('AC'))
#print(entropy('ACGT'))
#print(entropy('AAAT'))
#print(entropy('AAAA'))

#import argparse
#import math
#def entropy(seq): #-------

#seq = 'ACGTACGTAAAAAAAAAAACGTACGT'
#hard = 'ACGTACGTNNNNNNNNNNCGTACGT'
#k = 5 # of window size
#t = 1.0 #entropy threshold
#mask = list(seq)
#for i in range(len(seq) -k+1):
#	#win = i, seq[i:i+k]
#	if entropy(seq[i:i+k]) < t: continue
#	for j in range(i, i+k):
#		mask[j] = seq[j].lower()
#print(''.join(mask))

#import argparse
#import math
#import mcb185

#def entropy(seq): #-------

#parser = argparse.ArgumentParser()
#parser.add_argument('fasta')
#parser.add_argument('-window', type = int, default = 11)
#parser.add_argument('--threshold', type = float, default = 1.1)
#parser.add_argument('-wrap', )
#parser.add_argument('--hard', help = 'perform hard maskingg, soft is default')
#arg = parser.parse_args()


#k = arg.window # of window size
#t = arg.threshold #entropy threshold

#for defline, seq in mcb185.read_fasta(arg.fasta):

#	mask = list(seq)
#	for i in range(len(seq) -k+1):
#		if entropy(seq[i:i+k]) < t: continue
#		for j in range(i, i+k):
#			if arg.hard
#			mask[j] = seq[j].lower()
#	print('>', defline, sep='')
#	seq = ''.join(mask)

#######################################################
#5 questions in the exam, range from 41~49, except 47.

#import sys
#import random

#num_days = int(sys.argv[1])
#num_people = int(sys.argv[2])
#birthdays = list()
#found = False
#for i in range(num_people):
#	date = random.randint(0, num_days -1)
#	if date in birthdays:
#	#for prev_date in birthdays:
#	#	if date == prev_date: found = True
#		found = True
#		break
#	birthdays.append(date)
##print(birthdays)	#after looping
#	#print(birthdays)	#before looping
#print(found)

#- birthday by list
#import sys
#import random

#num_days = int(sys.argv[1])
#num_people = int(sys.argv[2])
## get all birthdays into a list
#birthdays = list()
#
#for i in range(num_people):
#	date = random.randint(0, num_days -1)
#	birthdays.append(date)

#found = False	
#for i in range(0, num_people):
#	#print('i=', i)
#	for j in range(i+1, num_people):
#		#print('	j=', j)
#		if birthdays[i] == birthdays[j]:
#			found = True
#			break
#	if found: break
#print(found)

#################################################
#- birthday by calendar

#import sys
#import random

#num_days = int(sys.argv[1])
#num_people = int(sys.argv[2])

##birthdays = list()
##birthdays.append(100)

###calendar 365 days in it
###calendar[100] += 1
###calendar[100] = 5
###calendar = list()
###for _ in range(num_days):
###	calendar.append(0)

#calendar = [0] * num_days
##fill calendar with dates
#found = False
#for i in range(num_people):	#for item in container:/for i in range(number): [i is an integer that creates range for intergers]
#	date = random.randint(0, num_days -1)						#Bad!!!: for i in dna: / for nt in range(number)
#	if calendar[date] != 0:
#		found = True
#		break
#	calendar[date] += 1
##check calendar for shared birthdays
#found = False
##for i in range(num_people):
##	if calendar[i] > 1:
##		found = True
##		break
#for birthday_count in calendar:
#	if birthday_count > 1: found = True
#print(found)

###############################################
#41
#import sys
#alph = sys.argv[1]
#mat = sys.argv[2]
#mis = sys.argv[3]

##print the header
#print('  ', end='')
#for nt in alph: print(nt, end='  ')
#print()

###print the side
##for i in range(len(alph)):
##	print(alph[i], end=' ')
##	for j in range(len(alph)):
##		if alph[i] == alph[j]: print(mat, end=' ')
##		else:				print(mis, end=' ')
##	print()

#for nt1 in alph:
#	print(nt1, end=' ')
#	for nt2 in alph:
#		if nt1 == nt2: print(mat, end=' ')
#		else:			print(mis, end=' ')
#	print()

#---------------------------------------------------
#49 write a function dust(seq, w, t) on the exam

#import math

#def entropy(seq):
#	pa = seq.count('A') / len(seq)
#	pc = seq.count('C') / len(seq)
#	pg = seq.count('G') / len(seq)
#	pt = seq.count('T') / len(seq)
#	h = 0
#	if pa != 0: h -= pa * math.log2(pa)
#	if pc != 0: h -= pc * math.log2(pc)
#	if pg != 0: h -= pg * math.log2(pg)
#	if pt != 0: h -= pt * math.log2(pt)
#	return h
	
#def dust(seq, w, t):
#	eseq = list(seq)
#	for i in range(len(seq) -w+1):
#		win = seq[i:i+w]
#		if entropy(win) < t:
#			for j in range(i, i+w): #eseq[j] = 'N' #change to N
#				eseq[j] = seq[j].lower() #change to lowercase
#	return ''.join(eseq)	
		
#print(dust('ACGTAAAAAAACGT', 6, 1.1))

#-----------------------------------------------------
#48 python3 gc_analysis ATATACAAATTACGAT 7

#import sys
#seq = sys.argv[1]
#k = int(sys.argv[2])
#for i in range(len(seq) -k +1):
#	win = seq[i:i+k]
#	g = win.count('G')
#	c = win.count('C')
#	gc_comp = (c+g)/k
#	#gc_skew = (g-c)/(g+c) if g+c != 0 else 0
#	##gc_skew = (g+c != 0) ? (g-c)/(g+c)
#	if g+c == 0: gc_skew = 0			#uniformly same for languages
#	else:		gc_skew = (g-c)/(g+c)
#	print(i, win, c, g, gc_comp, gc_skew)


#calendar = [0] * n #pythonism

#import sys
#seq = sys.argv[1]
#k = int(sys.argv[2])
#first = seq[0:k]
#gc = first.count('G') + first.count('C')
#for i in range(len(seq) -k +1):
#	#win = seq[i:i+k]
#	#c = seq[i:i+k].count('C')
#	#g = seq[i:i+k].count('G')
#	off = seq[i]
#	on = seq[i+k]
#	if off == 'C': gc -= 1
#	elif off == 'G': gc -= 1
	
#	if on == 'C': gc += 1
#	elif on == 'G': gc += 1
#	#if off == 'C' or off == 'G': gc -= 1
#	#if on == 'C' or on == 'G': gc += 1
#	print(i, off, seq[i:i+k], on, gc)

#45

#def polya(dna):
#    longest = 0
#    current = 0
    
#    for nt in dna:
#        if nt == 'A':
#            current += 1
#            if current > longest:
#                longest = current
#        else:
#            current = 0
            
#    return longest

#print(polya('ATCGGGCCATAAAAAAAACCTCTAGGGCT'))

#47

def read_fasta (file):
	defline = ''
	seq = ''
	
	with open(file) as fp:
		for line in fp:
			line = line.rstrip()
			if line [0] == '>'
				defline = line[1:]
			else:
				seq += line
				
	return defline, seq

























