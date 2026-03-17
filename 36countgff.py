import sys
import gzip

counts = {}

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] == '#': 
            continue
        fields = line.split('\t')
        feature = fields[2]

        if feature not in counts:
            counts[feature] = 0
        counts[feature] += 1

for k, v in counts.items():
    print(k, v)