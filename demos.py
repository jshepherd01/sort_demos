from utilities import *
from random import shuffle, randint

# sorting algorithms

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

# data functions

def dataShuffle(n):
    out = list(range(1,n+1))
    shuffle(out)
    return out

def dataRand(n):
    out = [randint(1,100) for i in range(n)]
    return out

def dataOrder(n):
    out = list(range(1,n+1))
    return out

def dataReverse(n):
    out = list(range(1,n+1))
    return out[::-1]

def dataLit(alist):
    return alist[:]

# validation/conversion functions

def isPositiveInteger(n):
    return (type(n) == int or (type(n) == str and n.isnumeric())) and int(n)>=1

# globals/initialisation

algorithms = {
    'sel': selectionSort,
}

datafuncs = {
    'shuffle': [dataShuffle, isPositiveInteger, int],
    'rand': [dataRand, isPositiveInteger, int],
    'order': [dataOrder, isPositiveInteger, int],
    'reverse': [dataReverse, isPositiveInteger, int],
    'lit': [dataLit, lambda *n: all(isPositiveInteger(i) for i in n), lambda *n: [int(i) for i in n]]
}

prevcmd = ""
datafunc = dataShuffle
datafuncargs = 5

#
#   Main Loop
#

while True:
    args = input(">>> ").lower().split()
    cmd = args.pop(0)
    if cmd == "":
        cmd = prevcmd
        if cmd == "":
            print(errorText("No command specified."))
            continue
    prevcmd = ""

#
#   (h)elp
#

    if cmd == "h" or cmd == "help":
        print("Displaying Help:")
        print("\t(h)elp: displays this message.")
        print("\t(r)un METHOD: run the specified sorting algorithm. Only the first three characters of METHOD need to be specified.")
        print("\t\tCurrently supported algorithms are:")
        print("\t\t - Selection Sort")
        print("\t(q)uit: stop executing the current algorithm. If no algorithm is running, exit the program.")
        print("\t(d)ata: specify the data to be passed to the next algorithm.")
        print("\t\tshuffle N: the numbers 1-N in a random order.")
        print()
        print(colourString('NOT IMPLEMENTED', 'r'))
        print("\t(s)tep: move to the next step of the inner loop.")
        print("\t(n)ext: move to the next step of the outer loop, stepping over the inner loop.")
        print("\t(e)nd: run the current algorithm until its completion.")
        print("\t\trand N: a list of N random numbers, between 1 and 100.")
        print("\t\torder N: the numbers 1-N in order.")
        print("\t\treverse N: the numbers 1-N in reverse order.")
        print("\t\tlit N [M ...]: the list given, in the order it is given.")

#
#   (r)un
#

    elif cmd == "r" or cmd == "run":
        if len(args) == 0:
            print(errorText("No algorithm specified."))
            continue
        if args[0][:3] not in algorithms:
            print(errorText("Algorithm not found."))
            continue
        print(algorithms[args[0][:3]](datafunc(datafuncargs)))

#
#   (d)ata
#

    elif cmd == "d" or cmd == "data":
        if len(args) == 0:
            print(errorText("No data specified."))
            continue
        if len(args) == 1:
            print(errorText("No argument specified."))
            continue
        if args[0] not in datafuncs:
            print(errorText("Data type not found."))
            continue

        record = datafuncs[args[0]]

        try:
            if record[1](*args[1:]):
                datafunc = record[0]
                datafuncargs = record[2](*args[1:])
                print("Data type set.")
            else:
                print(errorText("Argument not valid."))
                continue
        except TypeError:
            print(errorText('Argument not valid.'))
            continue

#
#   (q)uit
#

    elif cmd == "q" or cmd == "quit":
        exit()
