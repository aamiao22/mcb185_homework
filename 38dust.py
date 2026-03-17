import argparse
import math
import mcb185

def entropy(seq): #-------

parser = argparse.ArgumentParser()
parser.add_argument('fasta')
parser.add_argument('-window', type = int, default = 11)
parser.add_argument('--threshold', type = float, default = 1.1)
parser.add_argument('-wrap', )
parser.add_argument('--hard', help = 'perform hard maskingg, soft is default')
arg = parser.parse_args()


k = arg.window # of window size
t = arg.threshold #entropy threshold

for defline, seq in mcb185.read_fasta(arg.fasta):

	mask = list(seq)
	for i in range(len(seq) -k+1):
		if entropy(seq[i:i+k]) < t: continue
		for j in range(i, i+k):
			if arg.hard
			mask[j] = seq[j].lower()
	print('>', defline, sep='')
	seq = ''.join(mask)
