import sys
import mcb185

kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def avg_kd(peptide):
    kd = 0
    for aa in peptide:
        if aa not in kdtable:
            return None
        kd += kdtable[aa]
    return kd / len(peptide)

def has_region(seq, start, end, w, threshold):
    if end > len(seq): end = len(seq)
    if end - start < w: return False

    for i in range(start, end - w + 1):
        pep = seq[i:i+w]
        if 'P' in pep: continue         
        k = avg_kd(pep)
        if k is None: continue           
        if k >= threshold:
            return True
    return False

if len(sys.argv) < 2:
    print('usage: python3 35transmembrane.py <protein.faa>')
    sys.exit()

for defline, seq in mcb185.read_fasta(sys.argv[1]):

    # 1) signal peptide: w=8, avg KD >= 2.5, within first 30 aa
    signal = has_region(seq, 0, 30, 8, 2.5)

    # 2) transmembrane region: w=11, avg KD >= 2.0, after position 30
    tm = has_region(seq, 30, len(seq), 11, 2.0)

    if signal and tm:
        print(defline[1:60])