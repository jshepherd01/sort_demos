from utilities import *
from random import shuffle, randint

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

algorithms = {
    'sel': selectionSort,
}

prevcmd = ""
data = list(range(1,6))
shuffle(data)

while True:
    args = input(">>> ").lower().split()
    cmd = args.pop(0)
    if cmd == "":
        cmd = prevcmd
        if cmd == "":
            print(errorText("No command specified."))
            continue
    prevcmd = ""

    if cmd == "h" or cmd == "help":
        print("Displaying Help:")
        print("\t(h)elp: displays this message.")
        print("\t(r)un METHOD: run the specified sorting algorithm. Only the first three characters of METHOD need to be specified.")
        print("\t\tCurrently supported algorithms are:")
        print("\t\t - Selection Sort")
        print()
        print(colourString('NOT IMPLEMENTED', 'r'))
        print("\t(q)uit: stop executing the current algorithm. If no algorithm is running, exit the program.")
        print("\t(s)tep: move to the next step of the inner loop.")
        print("\t(n)ext: move to the next step of the outer loop, stepping over the inner loop.")
        print("\t(e)nd: run the current algorithm until its completion.")
        print("\t(d)ata: specify the data to be passed to the next algorithm.")
        print("\t\trand N: a list of N random numbers, between 1 and 100.")
        print("\t\torder N: the numbers 1-N in order.")
        print("\t\treverse N: the numbers 1-N in reverse order.")
        print("\t\tshuffle N: the numbers 1-N in a random order.")
        print("\t\tlit N [M ...]: the list given, in the order it is given.")

    elif cmd == "r" or cmd == "run":
        if len(args) == 0:
            print(errorText("No algorithm specified."))
            continue
        if args[0][:3] not in algorithms:
            print(errorText("Algorithm not found."))
            continue
        print(algorithms[args[0][:3]](data))
