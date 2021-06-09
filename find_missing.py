def find_missing(sequence):
    diff = min(sequence[1]- sequence[0], sequence[2]- sequence[1])
    for i in range(len(sequence)-1):
        if sequence[i] + diff != sequence[i+1]:
            return sequence[i] + diff
