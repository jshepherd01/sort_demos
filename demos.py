from utilities import *

# start with the basics

def selectionSort(alist):
    for i in range(len(alist)):
        j = i
        for k in range(i, len(alist)):
            if alist[k] < alist[j]:
                j = k

        coloursList = ['c']*i + [None]*(len(alist)-i)
        coloursList[i] = 'r'
        coloursList[j] = 'g'

        print(prettyList(alist, coloursList))

        temp = alist[j]
        alist[j] = alist[i]
        alist[i] = temp
    return alist

print(selectionSort([5,2,3,4,1]))
