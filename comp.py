def comp(array1, array2):
    if (array1 is None or array2 is None): 
        return False
    array1.sort(key=lambda x:abs(x))
    array2.sort()
    print(array1)
    print(array2)
    count = 0
    if len(array1) != len(array2):
        return False
    try:
        for i in range(len(array1)):            
            print(abs(array1[i]))
            print(array2[i]**0.5)
            if (array2[i])**0.5 == abs(array1[i]):
                count += 1
    except:
        pass
    return count == len(array1)
