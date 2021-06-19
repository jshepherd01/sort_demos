def insertionSort(alist):
    i = 0
    while i < len(alist):
        j = i
        while j > 0: 
            if alist[j-1] > alist[j]:
                temp = alist[j]
                alist[j] = alist[j-1]
                alist[j-1] = temp
                j -= 1
            else:
                break
        i += 1
    return alist

print(insertionSort([10,5,37,1,6]))