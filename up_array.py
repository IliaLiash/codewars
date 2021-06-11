def up_array(arr):
    try:
        for element in arr:
            if element < 0 or element > 9:
                return None
        arr = list(map(str,arr))
        res = int(''.join(arr)) + 1
        res = [int(i) for i in str(res)]
        return res
    except:
        return None
