def phred_to_prob(c):
    Q = ord(c) - 33
    return 10 ** (-Q / 10)

import math

def prob_to_phred(p):
    a = -10 * (math.log10(p))
    a = int(p + 0.5)
    return chr(a + 33)

print(phred_to_prob('A'))
print(prob_to_phred(0.001))

