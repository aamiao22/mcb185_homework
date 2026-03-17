import sys
import mcb185

# time python3 34skew.py ecoli.fa.gz 1000
w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):

    if len(seq) < w: continue

    window = seq[0:w]
    c = window.count('C')
    g = window.count('G')

    for i in range(0, len(seq) - w + 1):
        if i > 0:
            left = seq[i - 1]
            right = seq[i + w - 1]

            if left == 'C': c -= 1
            elif left == 'G': g -= 1

            if right == 'C': c += 1
            elif right == 'G': g += 1

        gccomp = (c + g) / w
        if c + g == 0:
            gcskew = 0
        else:
            gcskew = (g - c) / (g + c)

        #print(i, gccomp, gcskew)