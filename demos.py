# start with the basics

def selectionSort(alist):
    for i in range(len(alist)):
        j = i
        for k in range(i, len(alist)):
            if alist[k] < alist[j]:
                j = k
        temp = alist[j]
        alist[j] = alist[i]
        alist[i] = temp
    return alist

print(selectionSort([5,2,3,4,1]))