def max_and_min(arr1,arr2):
    big_diff = 0
    small_diff = max(max(arr1), max(arr2))
    big = []
    small = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if abs(arr1[i] - arr2[j]) > big_diff:
                big_diff = abs(arr1[i] - arr2[j])
            if abs(arr1[i] - arr2[j]) < small_diff:
                small_diff = abs(arr1[i] - arr2[j])
    return [big_diff, small_diff]
