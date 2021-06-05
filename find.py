def find(seq):
    seq.sort()
    diff = abs(seq[0] - seq[1])
    for i in range(len(seq)):
        if seq[i] + diff == seq[i + 1]:
            continue
        else:
            return seq[i] + diff
