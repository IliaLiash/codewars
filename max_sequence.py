def max_sequence(arr):
    max_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if sum(arr[i:j+1]) >= max_sum:
                max_sum = sum(arr[i:j+1])
    return max_sum
