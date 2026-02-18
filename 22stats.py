import sys

vals = []
for s in sys.argv[1:]:
	vals.append(float(s))

vals.sort()
total = 0

for val in vals: total += val
mean = total/len(vals)

ss = 0
for val in vals:
	d = val - mean
	ss += d * d
sd = (ss / len(vals)) ** 0.5

m = len(vals) // 2
if len(vals) % 2 == 1:
	median = vals[m]
else:
	median = (vals[m] + vals[m-1]) / 2

print('minimum', vals[0])
print('maximum', vals[-1])
print('range', vals[-1]-vals[0])
print('average', mean)
print('standard deviation', sd)
print('median', median)

