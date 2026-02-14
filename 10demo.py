import math

print('hello, again')
print(1.5e-2)
print(1 + 1)
print(2**3)
print(pow(2, 3))
print(math.pow(2, 3))
print(2**0.5)
print(math.sqrt(2))
print(math.log(2))

#print('a', 'ace', 'hello', 5, 3.1415926, 2.8, sep='\t')

def is_prime(n):
	for i in range(3, n, 2):
		#print('checking', i)
		r = n % i
		if r == 0: return False
	return True

#for i in range(1, 101,10):
	print(i, end=' ')
	if i % 15 == 0: print('fizzbuzz', end='')
	elif i % 3 == 0: print('fizz', end='')
	elif i % 5 == 0: print('buzz', end='')
	print()

def inch_to_cm(x):
	inches = x * 2.54
	return inches

for inch in range(20):
	cm = inch_to_cm(inch)
	#print(inch, cm)

def is_prob(x):
	if x >= 0 and x <= 1: return True
	return False

	#example
#print (is_prob(0.5))
#print (is_prob(2.5))

import math

def distance(x1,y1,x2,y2):
	i = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	return i

	#example
#print(distance(3,4,5,6))

# 1 1 2 3 5 8 13 21 (fibonacci):

a = 1
b = 1
fib = 0
#print(fib)

while True:
	a = b
	b = fib
	fib = a + b
	#print(fib)
	if fib > 100: break


def min4(a, b, c, d):
	if a <= b and a <= c and a <= d: return a
	if b <= c and b <= d: return b
	if c <= d: return c
	return d

#print(min4(5, 3, -1, 0))

import math

a = round (math.log2 (math.pi), 5)
b = round (math.log2 (math.e), 5)
#print (a,b, sep = ",")

def ftoc (x):
	c = (x - 32) * 5 / 9
	return c
#print(ftoc(32))
#print(ftoc(212))

def mph_to_kph (x):
	kph = x / 0.62137
	return kph
#print(mph_to_kph(5))

def is_int(x):
	return x % 1 == 0
#print(is_int(2.10))

def complement (nt):
	if nt == "A": return "T"
	if nt == "T": return "A"
	if nt == "C": return "G"
	if nt == "G": return "C"
#print(complement("T"))
#print(complement("f"))

def phred_to_prob (c):
	Q = ord(c) - 33
	return 10 ** (-Q / 10)
#print (phred_to_prob("A"))

def factorial (n):
	if n == 0: return 1
	fac = 1
	for i in range (1, n+1):
		fac = fac * i
	return fac
#print(factorial(5))

import math

pi = 3.0
sign = 1
n = 2

upper = math.inf
lower = -math.inf

while True:
	term = 4 / (n * (n + 1) * (n + 2))
	pi += sign * term
	#print(pi)

	if pi < math.pi: lower = pi
	else:		upper = pi

	if upper - math.pi < 1e-6 and math.pi - lower < 1e-6: break

	#if abs(pi - math.pi) < 1e-6:
		#break

	sign *= -1
	n += 2


a, b = 0, 1
for i in range(101):
	#print(a)
	a, b = b, a + b
	if a > 100: break
