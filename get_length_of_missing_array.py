def get_length_of_missing_array(array_of_arrays):
    if None in array_of_arrays or len(array_of_arrays) == 0:
        return 0
    res = sorted([len(array) for array in array_of_arrays])
    min_len = res[0]
    if res[0] == 0:
        return 0
    for element in res:
        if element - min_len > 0:
            return min_len
        min_len += 1
