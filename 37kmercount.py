import sys
import mcb185

k = int(sys.argv[2])
counts = {}

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    # sliding window of length k
    for i in range(0, len(seq) - k + 1):
        kmer = seq[i:i+k]
        if kmer not in counts:
            counts[kmer] = 0
        counts[kmer] += 1

for kmer, n in counts.items():
    print(kmer, n)